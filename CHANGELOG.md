
## 2026-10-09T07:20:00.793298+00:00 — Baseline: original workbook before approved review edits

Baseline of the original workbook before the approved OLS split.

## 2026-10-09T07:21:04.591176+00:00 — 25QB398J: approved Table 5A OLS-FE split and comparison relink

33 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1143",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1143",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1143",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1143",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K7",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1143",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1143",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1143",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1143",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1143",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1143",
    "before": null,
    "after": "Introduction, p. 4135: \"We find that a one standard-deviation increase in AQR exposure reduces loan supply by 25%. The decline is economically meaningful, given the average annual growth in bank credit of 13.13% in the pre-AQR years.\" Table 5A column 1, p. 4155: exposure coefficient -3.4217; economic significance -24.76%; no FE. Benchmark is average annual pre-AQR bank-credit growth, not an outcome-SD benchmark."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1143",
    "before": null,
    "after": "Qualifies under Jia's growth-rate clarification. No division by the 13.13% benchmark is reported. Alignment=0: the focal outcome contrasts collapsed pre/post lending periods, whereas the benchmark is annual pre-AQR credit growth; no common-horizon adjustment is established (Sections 5.1.1 and 5.1.4, pp. 4154-4157). Moved from s1/c1, not an additional duplicate comparison."
  },
  {
    "sheet": "Comparisons",
    "cell": "R7",
    "before": null,
    "after": "Wrong-setting attachment after approved OLS/FE split. Headline approximately 25% (24.76%) effect is Table 5A column 1, without FE, not retained FE columns 2-4. Qualifying comparison re-entered as h1/hc1 linked to h1/hy1; original model record preserved."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4209",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4209",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4209",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4209",
    "before": null,
    "after": "Post-minus-pre difference in the natural logarithm of one plus total loan amount lent by a lender to a firm; underlying loan amount is in Indian rupees. Table 5, Panel A, column 1, p. 4155. Outcome-type labels left blank because h1 has nonbinary treatment."
  },
  {
    "sheet": "Settings",
    "cell": "A1747",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Settings",
    "cell": "B1747",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Settings",
    "cell": "I15",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I1747",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J15",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "J1747",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K15",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "K1747",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L15",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1747",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M15",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M1747",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N15",
    "before": null,
    "after": "Table 5, Panel A, columns 2-4 (article p. 4155): effect of the post-minus-pre change in average lender AQR exposure (additional provisions divided by lender assets) on the post-minus-pre difference in log(1+loan amount), at the firm-lender level, with identifying firm fixed effects. Columns 3-4 add pre-AQR lender controls; column 4 excludes PCA observations. Column 1 is a separate OLS setting h1."
  },
  {
    "sheet": "Settings",
    "cell": "N1747",
    "before": null,
    "after": "Table 5, Panel A, column 1 (article p. 4155; Section 5.1.1, p. 4154): no-FE OLS at the firm-lender level, regressing the post-minus-pre difference in log(1+loan amount) on the change in average lender AQR exposure (additional provisions divided by lender total assets). No additional lender controls; lender-clustered inference. Exposure coefficient -3.4217; authors report a 24.76% lending decline for a one-treatment-SD increase."
  },
  {
    "sheet": "Settings",
    "cell": "O15",
    "before": null,
    "after": "Approved split: retain identifying-FE columns 2-4 here; no-FE column 1 and its headline comparison are recorded under h1. Original model fields preserved."
  },
  {
    "sheet": "Settings",
    "cell": "O1747",
    "before": null,
    "after": "Separated from s1 because column 1 has no fixed effects. Main-result status follows the headline approximately 25% credit-supply contraction in the introduction (p. 4135). Treatment remains nonbinary."
  }
]
```

## 2026-10-09T07:33:28.768052+00:00 — Saved Excel changes

0 populated-cell value changes. The XLSX also preserves formatting.


## 2026-10-09T07:34:26.624515+00:00 — 25QB398J s2: approved human labels for Table 5B

5 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I16",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J16",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K16",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L16",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M16",
    "before": null,
    "after": "n/a"
  }
]
```

## 2026-10-09T07:48:58.145075+00:00 — Saved Excel changes

0 populated-cell value changes. The XLSX also preserves formatting.

