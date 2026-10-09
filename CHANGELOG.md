
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


## 2026-10-09T08:13:40.435748+00:00 — 25QB398J s3: approved labels, reject effect comparison, remove personal attribution

8 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K8",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "R1143",
    "before": "Qualifies under Jia's growth-rate clarification. No division by the 13.13% benchmark is reported. Alignment=0: the focal outcome contrasts collapsed pre/post lending periods, whereas the benchmark is annual pre-AQR credit growth; no common-horizon adjustment is established (Sections 5.1.1 and 5.1.4, pp. 4154-4157). Moved from s1/c1, not an additional duplicate comparison.",
    "after": "Qualifies as a growth-rate comparison under the coding rules. No division by the 13.13% benchmark is reported. Alignment=0: the focal outcome contrasts collapsed pre/post lending periods, whereas the benchmark is annual pre-AQR credit growth; no common-horizon adjustment is established (Sections 5.1.1 and 5.1.4, pp. 4154-4157). Moved from s1/c1, not an additional duplicate comparison."
  },
  {
    "sheet": "Comparisons",
    "cell": "R8",
    "before": null,
    "after": "Section 5.2, p. 4159: compares estimated lending effects and the interaction's offset of the main effect, not an outcome mean, outcome SD, or other stated outcome level. Does not qualify as an outcome-benchmark comparison."
  },
  {
    "sheet": "Settings",
    "cell": "I17",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J17",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K17",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L17",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M17",
    "before": null,
    "after": "n/a"
  }
]
```

## 2026-10-09T08:21:38.683487+00:00 — 25QB398J s4: approved human labels and interaction-column correction

6 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I18",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J18",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K18",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L18",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M18",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N18",
    "before": null,
    "after": "Table 8, p. 4164: exposure × public-bank interactions appear in both columns 2 and 4, for capital additions and capital additions divided by assets, respectively. The remaining setting description is retained."
  }
]
```

## 2026-10-09T08:48:38.210549+00:00 — 25QB398J s5: approved review, human labels and linked corrections

5 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I19",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J19",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K19",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L19",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M19",
    "before": null,
    "after": "n/a"
  }
]
```

## 2026-10-09T08:48:49.880145+00:00 — 25QB398J s6: approved review, human labels and linked corrections

47 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K10",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K11",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "K9",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "L10",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "M10",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N10",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O10",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P10",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q10",
    "before": null,
    "after": "Table 10 col. 4, p. 4168: high-exposure coefficient -60.7650 on annual change in gross PP&E, in INR millions. Section 6.1.1, p. 4169: \"The decline translates to 34% of the average value of property, plant, and machinery in any year.\" Benchmark: the stated average PP&E measure; exact mean value, population, exposure group, period weights and untreated-counterfactual construction are not specified."
  },
  {
    "sheet": "Comparisons",
    "cell": "R10",
    "before": null,
    "after": "Alignment unknown: Table 2 defines PP&E as an annual change, whereas the comparison prose says average value. The source does not clearly establish whether the denominator is mean investment or a stock level, or whether it represents the focal high-exposure firms' untreated outcome. Do not infer alignment from a shared sample or invent the denominator."
  },
  {
    "sheet": "Comparisons",
    "cell": "R11",
    "before": null,
    "after": "Section 6.1.1, p. 4169; Table 10 col. 7, p. 4168: the effect is on STALLED/nonworking project value, but the stated 12.2% denominator is the average value of RUNNING projects. As written this is not a same-outcome benchmark and other_level does not waive that requirement. The prose also says decline despite a positive coefficient; do not silently repair the source or substitute a stalled-project mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R9",
    "before": null,
    "after": "Section 6.1, p. 4167; Table 10 col. 1, p. 4168: the approximately 38% statement interprets the log1p coefficient -0.3848. Other firms identify the treatment contrast, not a separate stated outcome mean, SD or level. Log-percentage interpretation alone does not qualify."
  },
  {
    "sheet": "Outcomes",
    "cell": "H27",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H28",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H29",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H30",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H31",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H32",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H33",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I27",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "I28",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I29",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I30",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I31",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I32",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I33",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J27",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J28",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J29",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J30",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J31",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J32",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J33",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K27",
    "before": null,
    "after": "Table 10 col. 1, p. 4168. Zero mass supported by the MCA zero-new-loan construction (p. 4148) and inclusion of firms with active relationships but no new loans (Table 3, p. 4150)."
  },
  {
    "sheet": "Outcomes",
    "cell": "K28",
    "before": null,
    "after": "Table 10 col. 2, p. 4168: log(1+borrowings from related parties). Zero mass unknown: no explicit zero frequency for this regression outcome is established. The generic RPT-loans summary is not enough to identify zeros in the inward-borrowing regression sample."
  },
  {
    "sheet": "Outcomes",
    "cell": "K29",
    "before": null,
    "after": "Unit correction: additions to paid-up equity capital are in INR millions, defined as current minus previous paid-up equity capital, net of forfeited capital (Table 2, p. 4149; Table 10 col. 3, p. 4168). Zero mass is not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K30",
    "before": null,
    "after": "Table 2, p. 4149, and Table 10 col. 4, p. 4168: annual change in gross PP&E, in INR millions. Zero mass is not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K31",
    "before": null,
    "after": "Table 2, p. 4149, and Table 10 col. 5, p. 4168: annual change in gross fixed assets, in INR millions. Zero mass is not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K32",
    "before": null,
    "after": "Table 10 col. 6, p. 4168: log(1+fixed-asset additions). Adding one does not establish observed zero mass; no explicit zero frequency is reported."
  },
  {
    "sheet": "Outcomes",
    "cell": "K33",
    "before": null,
    "after": "Table 10 col. 7, p. 4168: value of stalled/nonworking projects in INR millions, not a binary stalling indicator. Zero mass is not established by the reported definition or estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I20",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J20",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K20",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L20",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M20",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N20",
    "before": null,
    "after": "Table 10 / Equation (4), pp. 4167-4169: lender weights use pre-AQR average OUTSTANDING loan amounts, not new lending flows (Table 2, p. 4149; Section 4, p. 4154). Other treatment, FE and outcome definitions are retained."
  },
  {
    "sheet": "Settings",
    "cell": "O20",
    "before": null,
    "after": "Table 10 col. 6: the log1p fixed-asset-additions coefficient is negative but not statistically significant at the table's reported levels. Comparison alignment and uncertain zero masses are coded separately rather than inferred."
  }
]
```

## 2026-10-09T08:49:01.563777+00:00 — 25QB398J s7: approved review, human labels and linked corrections

20 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4210",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4210",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4210",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4210",
    "before": null,
    "after": "Post-minus-pre difference in log(1+total bank lending to a given NBFC/nonbank borrower), firm-lender level; underlying loan amount in INR. Table 11 col. 1, p. 4170. Nonbinary treatment; outcome-type labels left blank."
  },
  {
    "sheet": "Settings",
    "cell": "A1748",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Settings",
    "cell": "B1748",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Settings",
    "cell": "I1748",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I21",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1748",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "J21",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K1748",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "K21",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L1748",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L21",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M1748",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M21",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1748",
    "before": null,
    "after": "Table 11, p. 4170, column 1: no-FE OLS on firm-lender pairs restricted to NBFC/nonbank borrowers. Treatment is the post-minus-pre change in average lender AQR exposure (provision divergence divided by bank assets). Outcome is the post-minus-pre difference in log(1+loan amount). Exposure coefficient -8.1644; reported economic significance -50.65% for a one-treatment-SD change; lender-clustered inference."
  },
  {
    "sheet": "Settings",
    "cell": "N21",
    "before": null,
    "after": "Table 11, p. 4170, columns 2-4 only: nonbinary change in average bank AQR exposure affects the post-minus-pre difference in log(1+loans) to NBFC borrowers, using borrower firm FE; cols. 3-4 add pre-AQR lender controls, col. 4 excludes PCA observations. Column 1 has no FE and is separated into h2."
  },
  {
    "sheet": "Settings",
    "cell": "O1748",
    "before": null,
    "after": "OLS specification separated from s7 rather than pooling it with identifying borrower-FE columns. Supports the central shadow-bank-contagion finding (abstract p. 4132; conclusion p. 4173). No qualifying outcome-benchmark comparison found in Table 11 or Section 6.2.1."
  },
  {
    "sheet": "Settings",
    "cell": "O21",
    "before": null,
    "after": "Human_main=1: shadow-bank contagion is explicitly a central finding in the abstract (p. 4132), introduction (pp. 4135-4136), and conclusion (p. 4173); Section 6.2.1 / Table 11 supplies direct evidence. Economic-significance rows use treatment SD, not outcome benchmarks."
  }
]
```

## 2026-10-09T08:49:13.035454+00:00 — 25QB398J s8: approved review, human labels and linked corrections

33 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K12",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "R12",
    "before": null,
    "after": "Table 12 col. 4 / Section 6.3, p. 4171: the approximately 8% sentence interprets coefficient 0.0789 on growth in the MNREGA wage bill. It provides no separate mean, SD or stated level benchmark. It also belongs to binary treatment h3, not retained continuous s8. Do not add a replacement comparison under h3 because it fails eligibility."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4211",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4212",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4211",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4212",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4211",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4212",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4211",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4212",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4211",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4212",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4211",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4212",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K36",
    "before": null,
    "after": "Growth in the district MNREGA wage bill, not a wage level measured in INR; Table 12 col. 3 and note, p. 4171. Continuous-treatment setting s8 retains columns 1/3; binary columns 2/4 have their own outcomes under h3."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4211",
    "before": null,
    "after": "Growth in district nighttime luminosity score (average DNB radiance using VIIRS), Table 12 col. 2, p. 4171. Transformation is growth rate; the exact arithmetic-versus-log growth formula and observed zero mass are not established by Table 2 or Section 6.3. Do not assume a log transformation."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4212",
    "before": null,
    "after": "Growth in the total district MNREGA wage bill disbursed to bank accounts, Table 12 col. 4, p. 4171; this is a growth measure, not a wage level in INR. Transformation is growth rate; the exact arithmetic-versus-log growth formula and observed zero mass are not established by Table 2 or Section 6.3. Do not assume a log transformation."
  },
  {
    "sheet": "Settings",
    "cell": "A1749",
    "before": null,
    "after": "25QB398J"
  },
  {
    "sheet": "Settings",
    "cell": "B1749",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Settings",
    "cell": "I1749",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I22",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1749",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "J22",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K1749",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "K22",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L1749",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L22",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M1749",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M22",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1749",
    "before": null,
    "after": "Table 12, p. 4171, columns 2 and 4: district-year FE regressions of growth in nighttime luminosity and growth in the MNREGA wage bill on a binary indicator for above-median branch-weighted district AQR exposure. District and year FE; district-clustered inference. Coefficients -0.0154 and 0.0789, respectively."
  },
  {
    "sheet": "Settings",
    "cell": "N22",
    "before": null,
    "after": "Table 12, p. 4171, columns 1 and 3 only: continuous branch-weighted district AQR exposure, using bank-branch counts as weights, affects growth in nighttime luminosity and growth in the district MNREGA wage bill. District and year FE; district-clustered inference. Coefficients -0.1084 and 0.8810. Binary high-exposure columns 2 and 4 are separated into h3."
  },
  {
    "sheet": "Settings",
    "cell": "O1749",
    "before": null,
    "after": "Binary treatment separated from continuous s8. Supports the regional-growth/distress conclusions in the introduction (p. 4136). The approximately 8% sentence merely interprets the growth-outcome coefficient and supplies no separate outcome benchmark."
  },
  {
    "sheet": "Settings",
    "cell": "O22",
    "before": null,
    "after": "Replaces pooled binary=unknown with the known continuous treatment. Table 2, p. 4149, and Table 12 distinguish the continuous score from its above-median indicator. No qualifying mean/SD/level benchmark found for the continuous columns."
  }
]
```
