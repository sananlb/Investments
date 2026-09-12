"""Offline regressions for financial-report-only SEC fact selection."""

import datetime as dt
import unittest
from unittest.mock import patch

import build_fy_norm as norm
import fetch_anchor_fundamentals as anchor


AS_OF = dt.date(2026, 9, 11)
ANNUAL = dict(start="2025-06-01", end="2026-05-31", val=4433000000,
              form="10-K", filed="2026-07-20")
PROXY = dict(ANNUAL, val=4433, form="DEF 14A", filed="2026-08-17")
YTD = [
    dict(start="2025-06-01", end=end, val=value, form="10-Q", filed=filed)
    for end, value, filed in [
        ("2025-08-31", 824000000, "2025-09-18"),
        ("2025-11-30", 1780000000, "2025-12-18"),
        ("2026-02-28", 2836000000, "2026-03-19"),
    ]
]


class FinancialReportFactsTest(unittest.TestCase):
    def test_whitelist_preserves_reports_and_amendments(self):
        for form in ("10-K", "10-K/A", "10-Q", "10-Q/A", "20-F", "20-F/A",
                     "40-F", "40-F/A", "6-K", "6-K/A"):
            with self.subTest(form=form):
                report = dict(ANNUAL, form=form)
                self.assertEqual(norm.annual_by_end_year([report]), {2026: report})
        self.assertFalse(norm.is_financial_report_fact({}))

    def test_proxy_cannot_replace_annual_or_corrupt_derived_q4(self):
        for form in ("DEF 14A", "DEFA14A", "ARS", "8-K", "", None):
            with self.subTest(form=form):
                bad = dict(PROXY, form=form)
                points = YTD + [ANNUAL, bad]
                self.assertEqual(norm.annual_by_end_year(points)[2026], ANNUAL)
                self.assertEqual(norm.ttm_from_points(points, AS_OF)[0], 4433000000)
                self.assertEqual(norm.build_quarter_facts(points, AS_OF),
                                 norm.build_quarter_facts(YTD + [ANNUAL], AS_OF))
                self.assertEqual(anchor.ttm_sum(points, AS_OF)[0], 4433000000)
                self.assertIsNone(norm.ttm_from_points([bad], AS_OF)[0])

    def test_proxy_quarter_and_ytd_facts_are_excluded(self):
        bad_ytd = [dict(p, val=p["val"] / 1e6, form="DEF 14A", filed="2026-08-17")
                   for p in YTD]
        expected = norm.build_quarter_facts(YTD + [ANNUAL], AS_OF)
        self.assertEqual(norm.build_quarter_facts(YTD + bad_ytd + [ANNUAL], AS_OF),
                         expected)

    def test_series_filters_before_tag_and_period_selection(self):
        candidates = [("us-gaap", "ProxyOnly"), ("us-gaap", "NetIncomeLoss")]
        def units(_cik, _taxonomy, tag):
            return {"USD": [PROXY] if tag == "ProxyOnly" else YTD + [ANNUAL, PROXY]}

        with patch.object(norm, "fetch_concept_units", side_effect=units):
            self.assertEqual(norm.fetch_series("FDX", 1048911, candidates),
                             ("USD", YTD + [ANNUAL]))
            for cutoff in (dt.date(2026, 8, 10), dt.date(2026, 9, 10), AS_OF):
                with self.subTest(cutoff=cutoff):
                    _, points = norm.fetch_series_asof("FDX", 1048911, candidates, cutoff)
                    self.assertEqual(norm.ttm_from_points(points, cutoff)[0], 4433000000)
            _, points = norm.fetch_series_asof("FDX", 1048911, candidates, dt.date(2026, 7, 19))
            self.assertNotIn(ANNUAL, points)
        with patch.object(anchor, "fetch_concept", side_effect=lambda cik, tax, tag: units(cik, tax, tag)["USD"]):
            self.assertEqual(anchor.fetch_best_series(1048911, candidates, AS_OF),
                             YTD + [ANNUAL])

    def test_current_and_norm_shares_and_balance_sheet_instants(self):
        report = dict(end="2026-05-31", val=236581188, form="10-K", filed="2026-07-20")
        proxies = [dict(report, val=236, form="DEF 14A", filed=filed)
                   for filed in ("2026-06-01", "2026-08-17")]
        points = [report] + proxies
        self.assertEqual(norm.instant_by_end_year(points, {2026: report["end"]}), {2026: report})
        self.assertEqual(norm.latest_instant_point(points, AS_OF), report)
        self.assertEqual(norm.latest_current_shares_point(points, AS_OF), report)
        self.assertEqual(norm.share_point_near_fy_end(points, report["end"], "instant"), report)
        self.assertEqual(norm.share_point_near_fy_end([ANNUAL, PROXY], ANNUAL["end"], "annual"), ANNUAL)
        self.assertEqual(anchor.latest_instant(points, AS_OF), (report["val"], report["end"]))
        with patch.object(norm, "fetch_concept_units", return_value={"shares": points}):
            self.assertEqual(norm.fetch_current_shares_point("FDX", 1048911, AS_OF)[1], report)
            self.assertEqual(norm.fetch_shares_by_year("FDX", 1048911, {2026: report["end"]}),
                             {2026: report})

    def test_proxy_only_units_do_not_hide_report_currency(self):
        units = {"USD": [PROXY], "EUR": [ANNUAL]}
        self.assertEqual(norm.pick_unit_points(units, "TEST"), ("EUR", [ANNUAL]))
        self.assertEqual(units["USD"], [PROXY])  # Raw cache input is not mutated.
        self.assertEqual(norm.pick_unit_points({"USD": [PROXY]}, "FDX"), (None, []))


if __name__ == "__main__":
    unittest.main()
