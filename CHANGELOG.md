
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

## 2026-10-09T10:01:16.394541+00:00 — Review 2Q8UL8QQ s1: split Table 2 treatments and correct linked outcomes/comparisons

69 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1144",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1145",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1144",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1145",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1144",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1145",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1144",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1145",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K17",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K18",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1144",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1145",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L17",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1144",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1145",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M17",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1144",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1145",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N17",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1144",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1145",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O17",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1144",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1145",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P17",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1144",
    "before": null,
    "after": "Section 3, p. 7 and Table 2 column 2, p. 9. Table reports elasticity -0.4179, home-price change -14.4%, share explained 31.8%. Table formula: Elasticity x Change / change in log defaults, where the 2007-2010 aggregate default rise is 18.9%. Prose says the home-price collapse can explain approximately 32% of the contemporaneous rise in student-loan defaults."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1145",
    "before": null,
    "after": "Table 2 column 3 and notes, p. 9: employment elasticity -0.0004; employment change -4.7%; Share explained 0.0%. Notes define share explained as Elasticity x Change / change in log defaults, with overall new-default-rate rise of 18.9% from 2007 to 2010. Benchmark refers to the study aggregate default rise."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q17",
    "before": null,
    "after": "Section 3, p. 7 and Table 2 column 1, p. 9. Borrower-composition elasticity 0.3282 multiplied by reported 16.9% change, divided by the overall 18.9% rise in new student-loan defaults from 2007 to 2010, gives the reported 29.3% share explained. Prose explicitly says composition shifts can explain approximately 29% of the rise. Benchmark is the observed aggregate rise in defaults in the study, not an untreated outcome mean or SD."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1144",
    "before": null,
    "after": "Benchmark is the observed aggregate outcome rise, not an untreated mean or SD. Source prose prints 14.4 x -0.4179 / 18.9 = 0.318 (sign inconsistency); Table 2 reports the change as -14.4%. This record uses table values without silently correcting the quoted prose. Replaces wrong-setting s1/c2."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1145",
    "before": null,
    "after": "Omitted table-based effect/benchmark comparison. Preserve reported rounding to 0.0%; not an exactly zero coefficient. Formula establishes division; prose about virtually zero explanatory power does not explicitly pair the effect with the 18.9% benchmark. other_level, so alignment is n/a."
  },
  {
    "sheet": "Comparisons",
    "cell": "R17",
    "before": null,
    "after": "Retain as a same-outcome growth comparison, not merely interpretation of a log coefficient. other_level denotes the stated aggregate rise; no mean/SD alignment judgment applies."
  },
  {
    "sheet": "Comparisons",
    "cell": "R18",
    "before": null,
    "after": "Wrong setting after treatment split: Table 2 column 2 home-price comparison retained as h1/hc1, linked to h1/hy1. Original model fields preserved."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4213",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4214",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4213",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4214",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4213",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4214",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H65",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I65",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J65",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4213",
    "before": null,
    "after": "Change in log new student-loan default rate from 2007 to 2010 at zip-code level; Table 2, p. 9. Same dependent variable as original s1/y1. Detailed outcome-type labels left blank because treatment is nonbinary."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4214",
    "before": null,
    "after": "Change in log new student-loan default rate from 2007 to 2010 at zip-code level; Table 2, p. 9. Same dependent variable as original s1/y1. Detailed outcome-type labels left blank because treatment is nonbinary."
  },
  {
    "sheet": "Outcomes",
    "cell": "K65",
    "before": null,
    "after": "spurious: share of the rise explained is an effect/benchmark decomposition statistic, not a separate dependent variable. The dependent variable is y1. See Table 2, p. 9; record the share-explained results under Comparisons."
  },
  {
    "sheet": "Settings",
    "cell": "A1750",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Settings",
    "cell": "A1751",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Settings",
    "cell": "B1750",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Settings",
    "cell": "B1751",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Settings",
    "cell": "I1750",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I1751",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I46",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1750",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "J1751",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "J46",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K1750",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "K1751",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "K46",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L1750",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1751",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L46",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M1750",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M1751",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M46",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1750",
    "before": null,
    "after": "Table 2 column 2, Section 3, pp. 7-9: change in log zip-code home prices, 2006-2009, explaining change in log new student-loan default rate, 2007-2010. Separate zip-code weighted OLS regression, weighted by total student-loan balances; standard errors clustered by zip code. Coefficient -0.4179, home-price change -14.4%, reported share of 18.9% aggregate default rise explained 31.8%. Authors interpret the elasticity as potentially capturing effects through multiple channels; causal attribution remains vulnerable to correlated local shocks."
  },
  {
    "sheet": "Settings",
    "cell": "N1751",
    "before": null,
    "after": "Table 2 column 3, Section 3, pp. 7-9: change in log zip-code employment, 2006-2009, explaining change in log new student-loan default rate, 2007-2010. Separate zip-code weighted OLS regression, weighted by total student-loan balances; standard errors clustered by zip code. Reported coefficient -0.0004, employment change -4.7%, share explained 0.0% (rounded as reported)."
  },
  {
    "sheet": "Settings",
    "cell": "N46",
    "before": null,
    "after": "Restricted to Table 2 column 1 (Section 3, pp. 7-9): change in log share of nontraditional borrowers, 2006-2009, explaining change in log new student-loan default rate, 2007-2010. Zip-code weighted OLS, weighted by total student-loan balances; zip-code clustered standard errors. Coefficient 0.3282; reported composition change 16.9%; share of overall default increase explained 29.3%. Home-price and employment regressions split to h1 and h2."
  },
  {
    "sheet": "Settings",
    "cell": "O1750",
    "before": null,
    "after": "Treatment-specific split from s1, not a different estimator. Headline home-price contribution in abstract. One-year outcome lag reflects default reporting delay."
  },
  {
    "sheet": "Settings",
    "cell": "O1751",
    "before": null,
    "after": "Supporting substantive alternative-explanation analysis, not a diagnostic: authors discuss why aggregate employment has virtually zero explanatory power and may poorly proxy individual unemployment. Distinct treatment split from s1; weak explanatory power does not itself exclude a setting."
  },
  {
    "sheet": "Settings",
    "cell": "O46",
    "before": null,
    "after": "Distinct treatments require separate settings. Composition contribution is a headline result in the abstract. Decomposition does not establish exogenous treatment variation."
  }
]
```

## 2026-10-09T10:06:28.211444+00:00 — Saved Excel changes

0 populated-cell value changes. The XLSX also preserves formatting.


## 2026-10-09T10:07:54.398350+00:00 — Review 2Q8UL8QQ s2: confirm FE and restrict scope to Table 3 Panel B

7 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I47",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J47",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K47",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L47",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M47",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N47",
    "before": null,
    "after": "Scope restricted to Table 3, Panel B, columns 1-3 (Section 4, pp. 9-10): annual regional panel regressions of the new student-loan default rate in year t+1 on log home prices in year t, with region and year fixed effects. Regions are zip codes, counties, or commuting zones; observations are weighted by total student-loan balances and standard errors clustered at the corresponding regional level. Home prices cover 2006-2009 and recorded defaults 2007-2010. Coefficients are -0.00614, -0.00639, and -0.00728, respectively. Panel A long-difference results are outside this setting."
  },
  {
    "sheet": "Settings",
    "cell": "O47",
    "before": null,
    "after": "Region FE absorb time-invariant regional heterogeneity and year FE absorb common annual shocks. Regional clustering addresses within-region error dependence for inference; it does not eliminate omitted time-varying regional confounders. Supporting regional evidence preceding the main borrower-level Table 4. No qualifying outcome-benchmark comparison found for Panel B. The p. 10 footnote 10 conversion using the 3.6% default rate refers to the Panel A elasticity, not this setting; Panel A coverage is deferred."
  }
]
```

## 2026-10-09T11:33:41.511374+00:00 — Review 2Q8UL8QQ s3: validate labels and linked records

33 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1146",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1146",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1146",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1146",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K19",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1146",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1146",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1146",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1146",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1146",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1146",
    "before": null,
    "after": "Section 4, p. 10 footnote 10, referring to Table 3 Panel A column 1 (the -0.4179 elasticity repeated from Table 2 column 2): \"The rate of new student loan defaults is 3.6% in 2006.\" The footnote says a 1% home-price decline implies \"0.004179 x 3.6 = 0.0150 percentage point\" increase. Benchmark is the 2006 new-default rate; the authors multiply by the base rate to convert a proportional effect into percentage points, not divide by it."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1146",
    "before": null,
    "after": "Moved from wrong-estimate s3/c1 without duplicating the repeated zip-code setting. Benchmark weighting and correspondence to the long-difference regression target are not established clearly enough to assess alignment. Conversion uses a level rate for a proportional/log-change estimate; do not assume alignment from a common dataset."
  },
  {
    "sheet": "Comparisons",
    "cell": "R19",
    "before": null,
    "after": "Wrong focal estimate: p. 10 footnote 10 multiplies the Table 3 Panel A elasticity -0.4179 by the 2006 default rate of 3.6%; it does not benchmark the Table 4 FE coefficient -0.0113. The prose compares two estimates. The actual mean-based conversion is recorded under h1/hc2, because the Table 3 zip-code elasticity repeats Table 2 column 2. Also, -0.0113 is a default-probability coefficient per log-price unit, not -0.0113 percentage points per log-price unit."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4215",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4215",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4215",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4215",
    "before": null,
    "after": "Indicator for new student-loan default in year t+1, equal to one on default and zero otherwise. Dependent variable is untransformed; not a change in default sensitivity, which is a coefficient/estimand rather than another dependent variable."
  },
  {
    "sheet": "Settings",
    "cell": "A1752",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Settings",
    "cell": "B1752",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Settings",
    "cell": "I1752",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I48",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1752",
    "before": null,
    "after": "HDFE"
  },
  {
    "sheet": "Settings",
    "cell": "J48",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K1752",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "K48",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L1752",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L48",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M1752",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M48",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1752",
    "before": null,
    "after": "Table 4 column 4, pp. 10-11: log zip-code home price in year t explaining new borrower default in t+1. Three separately included FE dimensions: zip code, repayment cohort (year first entering repayment), and calendar year. Cohort FE address shifts in borrower composition and default propensity by repayment cohort. Weighted linear regression using individual loan balances, zip-code clustered standard errors. Home-price coefficient -0.0105 (SE 0.00281). Substantive robustness for the baseline home-price effect; no qualifying magnitude comparison."
  },
  {
    "sheet": "Settings",
    "cell": "N48",
    "before": null,
    "after": "Table 4 columns 1-3, 5 and 6, Section 4, pp. 10-11: continuous log zip-code home prices in year t explaining individual new default in t+1, weighted by individual loan balances. Columns 1-3 use zip-code and calendar-year FE; column 5 uses zip-code x repayment-cohort FE plus calendar-year FE; column 6 uses individual and calendar-year FE. Column 4 is split to h3 because it separately includes zip-code, repayment-cohort and calendar-year FE. Baseline coefficient -0.0113; the paper interprets a 1% home-price decline as a 0.0113 percentage-point rise in new defaults."
  },
  {
    "sheet": "Settings",
    "cell": "O1752",
    "before": null,
    "after": "Split from s3 to distinguish HDFE from standard FE under the project taxonomy. Supporting robustness, not a separate headline result."
  },
  {
    "sheet": "Settings",
    "cell": "O48",
    "before": null,
    "after": "An interacted zip-code x cohort FE set counts as one dimension, not two. Table 4 column 4 has three separately included FE dimensions and a borrower-composition identification rationale (p. 10), satisfying the project HDFE definition. No valid benchmark comparison found for the retained FE estimates."
  }
]
```

## 2026-10-09T11:34:00.373881+00:00 — Review 2Q8UL8QQ s4: validate labels and linked records

27 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1147",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1148",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1147",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1148",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1147",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1148",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1147",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1148",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1147",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1148",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1147",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1148",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1147",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1148",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1147",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1148",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1147",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1148",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1147",
    "before": null,
    "after": "Section 4, p. 10 discussion of Table 5 (p. 11), for-profit institutions, column 3, coefficient -0.0377. Authors note for-profit institutions and community colleges have the largest point estimates, but \"also tend to have much higher default rates\" and \"the implied elasticities are ultimately quite similar to those at (not-for-profit) public and private four-year colleges.\" Benchmark is the respective institution-type default rate; no numerical benchmark value is supplied in this passage. The stated elasticity interpretation normalizes the level response by the outcome rate."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1148",
    "before": null,
    "after": "Section 4, p. 10 discussion of Table 5 (p. 11), community colleges, column 4, coefficient -0.0220. Authors note for-profit institutions and community colleges have the largest point estimates, but \"also tend to have much higher default rates\" and \"the implied elasticities are ultimately quite similar to those at (not-for-profit) public and private four-year colleges.\" Benchmark is the respective institution-type default rate; no numerical benchmark value is supplied in this passage. The stated elasticity interpretation normalizes the level response by the outcome rate."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1147",
    "before": null,
    "after": "Qualitative but explicit outcome-rate scaling, not an invented numerical ratio. Exact rate, reference period, weighting and regression-target match are not reported; alignment unknown. Separate institution populations/focal estimates require separate records."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1148",
    "before": null,
    "after": "Qualitative but explicit outcome-rate scaling, not an invented numerical ratio. Exact rate, reference period, weighting and regression-target match are not reported; alignment unknown. Separate institution populations/focal estimates require separate records."
  },
  {
    "sheet": "Settings",
    "cell": "I49",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J49",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K49",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L49",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M49",
    "before": null,
    "after": "n/a"
  }
]
```

## 2026-10-09T11:34:13.611515+00:00 — Review 2Q8UL8QQ s5: validate labels and linked records

7 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I50",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J50",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K50",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L50",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M50",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N50",
    "before": null,
    "after": "Table 6 columns 1-4, Section 5.1, pp. 11-12: log zip-code home prices in year t explaining new borrower default in t+1, separately by individual labor-earnings bands shown in the table. Zip-code and year FE, individual loan-balance weights, zip-code clustered standard errors. Coefficients -0.0176, -0.0129, -0.0113 and -0.00498 (last not significant)."
  },
  {
    "sheet": "Settings",
    "cell": "O50",
    "before": null,
    "after": "Remove unsupported model claim that earnings groups are pre-existing/predetermined: the cited table and discussion do not establish a fixed pre-recession classification. Do not infer an exogenous low-income treatment from subgrouping. Central labor-market-channel evidence; no qualifying magnitude comparison found."
  }
]
```

## 2026-10-09T11:34:26.736491+00:00 — Review 2Q8UL8QQ s6: validate labels and linked records

5 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I51",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J51",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K51",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L51",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M51",
    "before": null,
    "after": "n/a"
  }
]
```

## 2026-10-09T11:34:39.853957+00:00 — Review 2Q8UL8QQ s7: validate labels and linked records

20 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4216",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4216",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4216",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4216",
    "before": null,
    "after": "Indicator for new student-loan default in year t+1, equal to one on default and zero otherwise. Dependent variable is untransformed; not a change in default sensitivity, which is a coefficient/estimand rather than another dependent variable."
  },
  {
    "sheet": "Settings",
    "cell": "A1753",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Settings",
    "cell": "B1753",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Settings",
    "cell": "I1753",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I52",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1753",
    "before": null,
    "after": "HDFE"
  },
  {
    "sheet": "Settings",
    "cell": "J52",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K1753",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "K52",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L1753",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L52",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M1753",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M52",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1753",
    "before": null,
    "after": "Table 8 column 4, pp. 13-14: continuous log home price in year t and its interaction with Owner explaining new default in t+1. Three separately included FE sets: zip code, repayment cohort and calendar year, mirroring Table 4 composition controls. Loan-balance weighted linear regression, zip-code clustered standard errors. Home-price coefficient -0.0105; Home price x Owner 0.000832 (insignificant). Substantive robustness of the direct-liquidity-channel test."
  },
  {
    "sheet": "Settings",
    "cell": "N52",
    "before": null,
    "after": "Table 8 columns 1-3, 5 and 6, Section 5.2, pp. 13-14: continuous log home-price effect on new borrower default in t+1, with Owner and Home price x Owner testing heterogeneity. Owner indicates mortgage-interest payments reported on Form 1098, not all legal homeownership. Columns 1-3 use zip-code and calendar-year FE; column 5 uses zip-code x cohort FE plus year FE; column 6 uses individual plus year FE. Column 4 split to h4 (HDFE). Baseline home-price coefficient -0.0112 and interaction 0.000972 (insignificant). Loan-balance weighted linear regression."
  },
  {
    "sheet": "Settings",
    "cell": "O1753",
    "before": null,
    "after": "Split from s7 because three FE dimensions and the linked borrower-composition rationale meet HDFE definition. Interacted FE in Table 8 column 5 is instead one set. No qualifying magnitude comparison found."
  },
  {
    "sheet": "Settings",
    "cell": "O52",
    "before": null,
    "after": "Focal treatment remains continuous home prices; a binary moderator does not make the price treatment binary. Small insignificant homeowner interactions are evidence of no detected differential sensitivity, not proof of identical effects. Owner level coefficients are conditional intercept differences, not unconditional homeowner default gaps. No qualifying outcome-benchmark comparison found."
  }
]
```

## 2026-10-09T11:34:52.418230+00:00 — Review 2Q8UL8QQ s8: validate labels and linked records

5 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I53",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J53",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K53",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L53",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M53",
    "before": null,
    "after": "n/a"
  }
]
```

## 2026-10-09T11:35:05.057806+00:00 — Review 2Q8UL8QQ s9: validate labels and linked records

5 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I54",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J54",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K54",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L54",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M54",
    "before": null,
    "after": "n/a"
  }
]
```

## 2026-10-09T11:35:17.862559+00:00 — Review 2Q8UL8QQ s10: validate labels and linked records

40 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4217",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4218",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4217",
    "before": null,
    "after": "h5"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4218",
    "before": null,
    "after": "h6"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4217",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4218",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4218",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H74",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4218",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "I74",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4218",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J74",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4217",
    "before": null,
    "after": "Indicator for new student-loan default in year t+1, equal to one on default and zero otherwise. Dependent variable is untransformed; not a change in default sensitivity, which is a coefficient/estimand rather than another dependent variable."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4218",
    "before": null,
    "after": "Indicator for new student-loan default in year t+1, equal to one on default and zero otherwise. Dependent variable is untransformed; not a change in default sensitivity, which is a coefficient/estimand rather than another dependent variable."
  },
  {
    "sheet": "Outcomes",
    "cell": "K74",
    "before": null,
    "after": "New-default indicator in year t+1, with t=2006-2011 and recorded default outcomes 2007-2012, per Eq. (2) and Section 6, pp. 15-17. Table 11 heading Default_t is inconsistent with the explicit timing; retain t+1. Untransformed 0/1 individual outcome, not the aggregate rate or a sensitivity coefficient. Nondefault observations (zeros) are supported by the nondegenerate default-rate discussion/Fig. 5."
  },
  {
    "sheet": "Settings",
    "cell": "A1754",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Settings",
    "cell": "A1755",
    "before": null,
    "after": "2Q8UL8QQ"
  },
  {
    "sheet": "Settings",
    "cell": "B1754",
    "before": null,
    "after": "h5"
  },
  {
    "sheet": "Settings",
    "cell": "B1755",
    "before": null,
    "after": "h6"
  },
  {
    "sheet": "Settings",
    "cell": "I1754",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I1755",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "I55",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1754",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "J1755",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "J55",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1754",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "K1755",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "K55",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1754",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L1755",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L55",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M1754",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M1755",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "M55",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1754",
    "before": null,
    "after": "Table 11 column 1, pp. 15-16: extended-sample FE regression of new borrower default in t+1 on continuous log home prices in t, controlling for IBR eligibility, with zip-code and calendar-year FE. Treatment years 2006-2011, default years 2007-2012; individual loan-balance weights and zip-code clustered standard errors. Home-price coefficient -0.00419 (SE 0.00209), 1,556,296 observations."
  },
  {
    "sheet": "Settings",
    "cell": "N1755",
    "before": null,
    "after": "Fig. 6 Panel A and Section 6, pp. 17-18: dynamic conventional DDD variant of Eq. (2), replacing Home price x IBR eligible x Post with Home price x IBR eligible x year interactions for 2007-2011, relative to baseline 2006. Binary policy eligibility is the exposure; continuous home prices measure shock sensitivity. Outcome is new borrower default in t+1; coefficients for treatment year t are plotted at t+1. Year and zip-code FE; underlying loan-balance weighted specification with zip-code clustered standard errors."
  },
  {
    "sheet": "Settings",
    "cell": "N55",
    "before": null,
    "after": "Restricted to Table 11 columns 2-4, Eq. (2), Section 6, pp. 15-17: conventional DiD/DDD for binary IBR eligibility under the means test, with Post equal to one beginning in 2009. Outcome is new borrower default in t+1; treatment years 2006-2011 and default years 2007-2012. Full interactions of log home price, eligibility and Post; zip-code plus calendar-year FE in columns 2-3, individual plus year FE in column 4. Individual loan-balance weights and zip-code clustered standard errors. Column 3 restricts to relatively high debt/discretionary-income borrowers. Column 1 is a separate FE specification (h5)."
  },
  {
    "sheet": "Settings",
    "cell": "O1754",
    "before": null,
    "after": "Split from s10: no Post interactions or DDD estimator in column 1. Supporting extended-period home-price result. Eligibility coefficient 0.0256 is a conditional group association here, not an identified policy receipt effect. No qualifying outcome-benchmark comparison found."
  },
  {
    "sheet": "Settings",
    "cell": "O1755",
    "before": null,
    "after": "Include because the authors substantively interpret the post-2009 jump and subsequent growth in insurance against home-price shocks, not solely a pretrend diagnostic. Pre-2009 coefficients are diagnostic components of this same dynamic setting. Numerical coefficient values not tabulated in the text; do not invent them from the qualitative discussion. Figure 6 Panel B take-up rates alone are descriptive, not outcome benchmarks. No qualifying magnitude comparison found."
  },
  {
    "sheet": "Settings",
    "cell": "O55",
    "before": null,
    "after": "Eligibility, not actual enrollment, defines exposure; no IV receipt effect is estimated. In column 2, eligibility x Post is -0.0404 and the triple interaction is 0.00314. With the triple interaction, the post-policy change in the eligibility gap at log price h is beta4 + beta6*h; -0.0404 alone is not an unconditional average program effect. Similarly beta2=0.0425 is not an unconditional baseline gap. Post includes 2009, not only years after 2009. Table heading Default_t conflicts with Eq. (2), text and reporting lag; use t+1. No qualifying benchmark comparison found. Fig. 6 substantive dynamic effects added as h6; do not treat selected take-up groups in Fig. 5 as randomized or IV receipt estimates."
  }
]
```

## 2026-10-09T12:10:25.244015+00:00 — Saved Excel changes

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Papers",
    "cell": "E10",
    "before": null,
    "after": "Done"
  },
  {
    "sheet": "Papers",
    "cell": "E8",
    "before": null,
    "after": "Done"
  }
]
```

## 2026-10-09T12:36:46.066768+00:00 — Review 24DPCTZ3 s1: causal scope, outcomes and benchmark evidence

11 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4219",
    "before": null,
    "after": "24DPCTZ3"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4219",
    "before": null,
    "after": "s1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4219",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4219",
    "before": null,
    "after": "Relative end-of-day filtered VIX level versus CX, VIX*_t/CX_t - 1, in the analogous regression of Section 3.4, p. 2920 footnote 18. Effective range for RX proxies that of VIX* where their index values are close; other observations excluded. Exact coefficient not reported. Continuous-treatment setting, so detailed outcome-type labels left blank."
  },
  {
    "sheet": "Settings",
    "cell": "I7",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J7",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K7",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L7",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M7",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N7",
    "before": null,
    "after": "Section 3.4, printed pp. 2919-2920: daily OLS regression of Z_t = RX_t/CX_t - 1 on DR_t, the difference in effective strike-range widths, with Newey-West standard errors using 20 lags. Reported equation Z_t = 0.0340 + 0.0089 DR_t; the authors explicitly interpret an exogenous one-treatment-SD widening as inflating RX relative to CX by an additional 1.7%. Include the same-location alternative VIX*/CX regression reported in footnote 18: RX strike range proxies the VIX* range, using observations where RX and VIX* values are close; other VIX* observations excluded. Footnote reports almost identical results but no separate coefficient."
  },
  {
    "sheet": "Settings",
    "cell": "O7",
    "before": null,
    "after": "Retain because p. 2920 explicitly attributes distortions to exogenous/idiosyncratic strike-range variation unrelated to option prices, rather than merely describing covariance. Supporting measurement result. Adjusted R-squared 67.2 is on a percent scale. DR SD=1.88 is treatment SD, not outcome SD; the 1.7% interpretation and construction of ratio-minus-one Y do not separately benchmark the focal slope against a mean/SD/level of that same Y. No qualifying comparison. Footnote 18 alternate outcome added as hy1."
  }
]
```

## 2026-10-09T12:36:59.008700+00:00 — Review 24DPCTZ3 s2: causal scope, outcomes and benchmark evidence

6 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H8",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I8",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J8",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K8",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s2 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Settings",
    "cell": "I8",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O8",
    "before": null,
    "after": "Section 4.1.2, Table 4/Fig. 5, pp. 2924-2926: conditional mean returns, densities and a fitted scatterplot line document a contemporaneous negative association/cojump distribution. Authors conclude a negative monotone association, not a directional effect of an intervention in CX on equity returns. Model language about a causal effect is unsupported. Exclude as descriptive under the causal-setting gate, not because OLS is inherently inadmissible."
  }
]
```

## 2026-10-09T12:37:12.290241+00:00 — Review 24DPCTZ3 s3: causal scope, outcomes and benchmark evidence

6 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H9",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I9",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J9",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K9",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s3 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Settings",
    "cell": "I9",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O9",
    "before": null,
    "after": "Section 4.1.2, Table 5/Fig. 6, pp. 2926-2928: authors explicitly reverse the conditioning direction to describe volatility increments conditional on equity-return bins and conclude a contemporaneous inverse cojumping relation. Reversing the conditioning direction does not identify either causal direction. Conditional densities/group means are descriptive, not a separate causal treatment-response setting."
  }
]
```

## 2026-10-09T12:37:25.181596+00:00 — Review 24DPCTZ3 s4: causal scope, outcomes and benchmark evidence

10 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H10",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "H11",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I10",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I11",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J10",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J11",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K10",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s4 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Outcomes",
    "cell": "K11",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s4 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Settings",
    "cell": "I10",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O10",
    "before": null,
    "after": "Sections 4.2.1-4.2.2, Eqs. (17)-(20), Fig. 7, pp. 2928-2931: leverage is explicitly defined as limiting contemporaneous return-spot-volatility CORRELATION; integrated leverage averages local correlations. One-factor assumptions identify this latent correlation from observable prices, not a directional causal response. Section 4.2 discusses alternative causal explanations without identifying between them. Exclude from causal settings; neither an OLS causal coefficient nor a causal outcome-SD effect."
  }
]
```

## 2026-10-09T12:37:39.043668+00:00 — Review 24DPCTZ3 s5: causal scope, outcomes and benchmark evidence

10 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H12",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "H13",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I12",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I13",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J12",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J13",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K12",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s5 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Outcomes",
    "cell": "K13",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s5 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Settings",
    "cell": "I11",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O11",
    "before": null,
    "after": "Section 4.2.3, Table 6, p. 2932: jump-exclusion cutoffs, bias correction and alternative price series check robustness of the estimated contemporaneous leverage CORRELATION. They do not estimate a causal effect of equity-return treatment on volatility. Main scientific importance does not satisfy the causal-setting inclusion rule."
  }
]
```

## 2026-10-09T12:37:59.342528+00:00 — Review 24DPCTZ3 s6: causal scope, outcomes and benchmark evidence

10 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H14",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "H15",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I14",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I15",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J14",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J15",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K14",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s6 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Outcomes",
    "cell": "K15",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s6 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Settings",
    "cell": "I12",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O12",
    "before": null,
    "after": "Section 4.2.3, Fig. 8/Table 7, pp. 2933-2935: distribution of leverage-correlation estimates across option maturities is a measurement/robustness exercise, not a causally interpreted treatment-response estimator. The mean/SD rows summarize estimated correlations, not a focal causal effect paired with a same-outcome benchmark. Discussion of liquidity/noise is an explanation of estimator precision, not a separately identified maturity intervention."
  }
]
```

## 2026-10-09T12:38:12.082897+00:00 — Review 24DPCTZ3 s7: causal scope, outcomes and benchmark evidence

6 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H16",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I16",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J16",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K16",
    "before": null,
    "after": "spurious as a causal-outcome record: parent s7 is rejected under the causal-setting inclusion rule. The underlying descriptive statistic remains valid; original model fields are preserved. See Settings Notes for the source and exclusion rationale."
  },
  {
    "sheet": "Settings",
    "cell": "I13",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O13",
    "before": null,
    "after": "Section 4.2.4, Figs. 10-11, pp. 2935-2936: centered 21-day averages and scatterplots show the leverage correlation co-varies with CX. Authors state the short sample prevents firm conclusions and suggest association with risk pricing. No implemented directional causal regression or intervention in turbulence is established; the model invents an OLS treatment-effect setting from a descriptive time-series pattern."
  }
]
```

## 2026-10-09T12:38:24.812800+00:00 — Review 24DPCTZ3 s8: causal scope, outcomes and benchmark evidence

34 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1149",
    "before": null,
    "after": "24DPCTZ3"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1150",
    "before": null,
    "after": "24DPCTZ3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1149",
    "before": null,
    "after": "s8"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1150",
    "before": null,
    "after": "s8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1149",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1150",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1149",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1150",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1149",
    "before": null,
    "after": "y2"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1150",
    "before": null,
    "after": "y2"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1149",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1150",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1149",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1150",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1149",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1150",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1149",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1150",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1149",
    "before": null,
    "after": "Section 4.3, Fig. 12 (p. 2937) and p. 2938: strike-range instability results in \"a downward bias in VIX of up to 5% during the crash phase\". Figure labels the comparison VIX/CX* - 1. Benchmark is contemporaneous scaled CX* during the May 6 crash, calibrated to VIX before 13:30; numerical benchmark index level at the extreme is not tabulated."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1150",
    "before": null,
    "after": "Section 4.3, Fig. 12 (p. 2937) and p. 2938: authors attribute \"periodic 10% to 15% overvaluation thereafter\" to oscillating effective strike ranges after the crash. Figure reports VIX/CX* - 1. Benchmark is contemporaneous scaled CX* in the post-crash period on May 6, using the same pre-13:30 calibration."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1149",
    "before": null,
    "after": "An explicit index-level distortion relative to an alternative same-market volatility-level reference, not a coefficient-only percent interpretation. Keep separate from subsequent overvaluation because the focal period/contrast differs. other_level alignment=n/a; no claim CX* is ground-truth volatility."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1150",
    "before": null,
    "after": "Same-outcome index-level reference comparison with explicit division. This is post-crash overvaluation, not the separate within-VIX spikes exceeding 10%, and not a mean/SD comparison. Numerical benchmark level at each extreme not reported."
  },
  {
    "sheet": "Outcomes",
    "cell": "H17",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I17",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J17",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K17",
    "before": null,
    "after": "spurious as a causal outcome: Table 8 correlations summarize measurement coherence and are descriptive diagnostics; they are not the outcome of the retained strike-range distortion analysis. Retained level outcome is y2."
  },
  {
    "sheet": "Outcomes",
    "cell": "K18",
    "before": null,
    "after": "VIX implied-volatility index LEVEL during May 6, 2010, quoted as annualized volatility (plots use decimal units). Focal distortion is the difference from contemporaneous CX*, the corridor index scaled to match VIX before 13:30; Fig. 12 bottom right reports VIX/CX* - 1. CX* is the benchmark, not unscaled CX. Section 4.3, pp. 2937-2938."
  },
  {
    "sheet": "Settings",
    "cell": "I14",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J14",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K14",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L14",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M14",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N14",
    "before": null,
    "after": "Section 4.3, Fig. 12 and discussion, pp. 2937-2938: measurement-mechanism case study of how changing CBOE effective strike-range truncation distorts the VIX level during May 6, 2010. Authors reconstruct major VIX movements using the underlying option quotes and truncation rule, and compare with CX*, the corridor index scaled to match pre-13:30 VIX levels. The range varies continuously/nonbinarly; the 13:30 split is not a treated/post causal DiD design. VIX is reportedly downward biased by up to 5% during the crash and overvalued by 10%-15% subsequently relative to CX*."
  },
  {
    "sheet": "Settings",
    "cell": "O14",
    "before": null,
    "after": "Other = formula-based index reconstruction and same-market measurement-counterfactual comparison, not OLS/IV/DiD. Retain only the explicit causal attribution of artificial index movements to strike-range truncation (p. 2938); Table 8 return correlations are supporting descriptive diagnostics, not the causal estimator. Main=1 because real-time robustness during market stress is a central abstract/introduction/conclusion claim. CX* is a scaled reference proxy, not observed true volatility; attribution depends on that maintained measurement argument. Comparisons use other_level, not a mean/SD benchmark."
  }
]
```

## 2026-10-09T12:38:37.868591+00:00 — Review 24DPCTZ3 h1: causal scope, outcomes and benchmark evidence

28 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1151",
    "before": null,
    "after": "24DPCTZ3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1151",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1151",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1151",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1151",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1151",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1151",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1151",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1151",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1151",
    "before": null,
    "after": "Section 3.2, p. 2915 and Fig. 2 p. 2916: RX \"starts out, at 8:30, around 23.5, more than 2% below the RX* value of 24.\" The gap persists until about 11:00, when the RX strike range expands and the indices coincide. Benchmark is same-time RX* from all positive-bid OTM options on February 16, 2010."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1151",
    "before": null,
    "after": "Authors explicitly express the index-level discrepancy as a percent of the alternate-rule level: verbal=1, divided=1. Benchmark is other_level, not an outcome mean/SD; alignment=n/a. Approximate levels and the authors stated more-than-2% comparison preserved without inventing an exact ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4220",
    "before": null,
    "after": "24DPCTZ3"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4220",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4220",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4220",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4220",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4220",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4220",
    "before": null,
    "after": "Computed RX/RX* implied-volatility index level under the two option-inclusion rules on February 16, 2010. Annualized volatility: prose around 23.5 versus 24, Fig. 2 axis about 0.22-0.24 in decimal units. Untransformed positive index level; displayed full-day paths stay strictly above zero (pp. 2915-2916)."
  },
  {
    "sheet": "Papers",
    "cell": "E7",
    "before": null,
    "after": "Human review complete for main article and included appendices. Retained s1 (OLS strike-range distortion, with omitted VIX* alternative outcome added), corrected s8 (Other: flash-crash reconstruction), added h1 (Other: binary index-rule contrast, Fig. 2). Rejected s2-s7 as descriptive cojump/correlation/leverage analyses, not directional causal treatment settings. Three magnitude comparisons added for the construction-based level contrasts; no qualifying comparison for s1 treatment-SD interpretation. Theoretical pricing identities, descriptive jump distributions/symmetry tests, and data-filter/volatility-estimation procedures do not add causal settings. See per-setting evidence and limitations; original model fields preserved."
  },
  {
    "sheet": "Settings",
    "cell": "A1756",
    "before": null,
    "after": "24DPCTZ3"
  },
  {
    "sheet": "Settings",
    "cell": "B1756",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Settings",
    "cell": "I1756",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1756",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1756",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1756",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1756",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1756",
    "before": null,
    "after": "Omitted Section 3.2 measurement-rule comparison, Fig. 2, pp. 2915-2916, February 16, 2010: compute RX with the CBOE cutoff after two consecutive zero-bid strikes versus RX* using all out-of-the-money options with positive bid quotes, on the same underlying market data. This is a two-rule construction contrast. Around 08:30 RX is about 23.5, more than 2% below RX* at 24. Just before 11:00 RX jumps as its lower strike range expands; RX* has no corresponding jump. Authors explicitly attribute the discontinuity solely to the changing option set, not to a meaningful shift in option prices."
  },
  {
    "sheet": "Settings",
    "cell": "O1756",
    "before": null,
    "after": "Other = direct nonlinear index-formula recomputation under alternative inclusion rules, not OLS or randomized assignment. Binary refers to the two implemented calculation rules, not a high/low volatility dummy. Supporting construction-mechanism result at a distinct date/location from s8. RX* is a wider-range comparator, not guaranteed true volatility; both rules can exhibit truncation problems elsewhere (footnote 13)."
  }
]
```

## 2026-10-09T13:32:08.239529+00:00 — Saved Excel changes

0 populated-cell value changes. The XLSX also preserves formatting.


## 2026-10-09T13:33:14.355873+00:00 — Mark 24DPCTZ3 DONE on Papers sheet; preserve review note

1 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Papers",
    "cell": "E7",
    "before": "Human review complete for main article and included appendices. Retained s1 (OLS strike-range distortion, with omitted VIX* alternative outcome added), corrected s8 (Other: flash-crash reconstruction), added h1 (Other: binary index-rule contrast, Fig. 2). Rejected s2-s7 as descriptive cojump/correlation/leverage analyses, not directional causal treatment settings. Three magnitude comparisons added for the construction-based level contrasts; no qualifying comparison for s1 treatment-SD interpretation. Theoretical pricing identities, descriptive jump distributions/symmetry tests, and data-filter/volatility-estimation procedures do not add causal settings. See per-setting evidence and limitations; original model fields preserved.",
    "after": "DONE — Human review complete for main article and included appendices. Retained s1 (OLS strike-range distortion, with omitted VIX* alternative outcome added), corrected s8 (Other: flash-crash reconstruction), added h1 (Other: binary index-rule contrast, Fig. 2). Rejected s2-s7 as descriptive cojump/correlation/leverage analyses, not directional causal treatment settings. Three magnitude comparisons added for the construction-based level contrasts; no qualifying comparison for s1 treatment-SD interpretation. Theoretical pricing identities, descriptive jump distributions/symmetry tests, and data-filter/volatility-estimation procedures do not add causal settings. See per-setting evidence and limitations; original model fields preserved."
  }
]
```

## 2026-10-09T13:40:09.180649+00:00 — Saved Excel changes

1 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Papers",
    "cell": "E7",
    "before": "DONE — Human review complete for main article and included appendices. Retained s1 (OLS strike-range distortion, with omitted VIX* alternative outcome added), corrected s8 (Other: flash-crash reconstruction), added h1 (Other: binary index-rule contrast, Fig. 2). Rejected s2-s7 as descriptive cojump/correlation/leverage analyses, not directional causal treatment settings. Three magnitude comparisons added for the construction-based level contrasts; no qualifying comparison for s1 treatment-SD interpretation. Theoretical pricing identities, descriptive jump distributions/symmetry tests, and data-filter/volatility-estimation procedures do not add causal settings. See per-setting evidence and limitations; original model fields preserved.",
    "after": "Done"
  }
]
```

## 2026-10-10T03:55:52.142882+00:00 — Review 3B6VC3AP s1: causal scope, outcomes and benchmark evidence

19 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H166",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H167",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H168",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I166",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I167",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I168",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J166",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J167",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J168",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K166",
    "before": null,
    "after": "Ratio of announcement-window CAR to CAR[-63,2]; other transformation. Zero mass is not established by the source. Table 2."
  },
  {
    "sheet": "Outcomes",
    "cell": "K167",
    "before": null,
    "after": "Ratio of announcement-window CAR to CAR[-63,2]; other transformation. Zero mass is not established by the source. Table 2."
  },
  {
    "sheet": "Outcomes",
    "cell": "K168",
    "before": null,
    "after": "Ratio of announcement-window CAR to CAR[-63,2]; other transformation. Zero mass is not established by the source. Table 2."
  },
  {
    "sheet": "Settings",
    "cell": "I68",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J68",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K68",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L68",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M68",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N68",
    "before": null,
    "after": "Table 2, pp. 323-324, all six columns. Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Firm FE in all columns; quarter FE in columns 2,4,6. Earnings-announcement observations two years before and after each reduction. The one-year exclusion around the event governs control eligibility, not the regression observation window. Five-or-fewer pre-event analysts. Outcomes are three announcement CAR/full-cycle CAR ratios. Preferred effects 0.051, 0.049, 0.057. More information arrives at the announcement rather than beforehand."
  },
  {
    "sheet": "Settings",
    "cell": "O68",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:56:05.034158+00:00 — Review 3B6VC3AP s2: causal scope, outcomes and benchmark evidence

20 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K27",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L27",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M27",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N27",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O27",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P27",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q27",
    "before": null,
    "after": "Section 4.2.1 p. 323; Table 3 Panel A column 1: participation probability rises by 5.2 percentage points; authors compare with average participation probability 15.4% in our sample. No effect/mean ratio is reported."
  },
  {
    "sheet": "Comparisons",
    "cell": "R27",
    "before": null,
    "after": "The prose does not identify an untreated mean for the treated target, benchmark timing or weighting clearly enough to establish alignment. Do not invent a ratio or attach this comparison to column 2."
  },
  {
    "sheet": "Outcomes",
    "cell": "H169",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H170",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I169",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "I170",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "J169",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J170",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Settings",
    "cell": "I69",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J69",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K69",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L69",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M69",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O69",
    "before": null,
    "after": "Table 3 Panel A. Firm FE throughout; quarter FE in columns 2 and 4. Retain c1 for column 1 coefficient 0.052, not column 2 coefficient 0.051. Panel B added separately. Zero participation implies zero participating-analyst count in this same call sample."
  }
]
```

## 2026-10-10T03:56:18.002110+00:00 — Review 3B6VC3AP s3: causal scope, outcomes and benchmark evidence

26 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K28",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "R28",
    "before": null,
    "after": "Spurious benchmark: p. 324 reports only a log-coefficient percentage interpretation. No separate same-outcome mean, SD or level is compared. The model inferred an untreated benchmark that is not reported."
  },
  {
    "sheet": "Outcomes",
    "cell": "H171",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H172",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H173",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H174",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H175",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H176",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I171",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I172",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I173",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I174",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I175",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I176",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J171",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J172",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J173",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J174",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J175",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J176",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Settings",
    "cell": "I70",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J70",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K70",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L70",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M70",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O70",
    "before": null,
    "after": "Table 4 Panel A, February 2003-December 2010. The 18.7% statement is the authors approximate interpretation of a 0.187 coefficient on log(1+search count), not a separate outcome-level benchmark. Reject c1. Panel B added separately. log1p alone does not establish observed zeros."
  }
]
```

## 2026-10-10T03:56:30.918369+00:00 — Review 3B6VC3AP s4: causal scope, outcomes and benchmark evidence

26 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K29",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L29",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M29",
    "before": null,
    "after": "outcome_sd"
  },
  {
    "sheet": "Comparisons",
    "cell": "N29",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O29",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P29",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q29",
    "before": null,
    "after": "pp. 325-326, Table 5 col. 3: 0.091 times SUE SD 4.32 gives about 0.39 percentage points, described as roughly one-eighth of the SD of abnormal hedge-fund holdings. Table 1 p. 321 identifies holdings SD 3.00 for treated firms in the TWO-YEAR PRE-REDUCTION period, not a pooled full-sample SD."
  },
  {
    "sheet": "Comparisons",
    "cell": "R29",
    "before": null,
    "after": "Qualifies because of the explicit outcome-SD fraction, not merely the SUE increment. Treated pre-period population and outcome scale are identified; correspondence of that reference distribution/weighting to the regression slope-change target is not fully established, so alignment unknown."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4221",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4221",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4221",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H177",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4221",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I177",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4221",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J177",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4221",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K177",
    "before": null,
    "after": "Abnormal aggregate hedge-fund holdings: current holdings minus the mean of the preceding four quarters, percentage points of shares outstanding. other = deviation from trailing mean, not a log. Zero mass for the regression outcome is unresolved."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4221",
    "before": null,
    "after": "Table 5 columns 4-6: abnormal aggregate NONHEDGE-fund holdings at the quarter end before earnings announcement; current holdings minus preceding-four-quarter mean, percentage points of shares outstanding."
  },
  {
    "sheet": "Settings",
    "cell": "I71",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J71",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K71",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L71",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M71",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N71",
    "before": null,
    "after": "Table 5, pp. 325-327. Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. DiD change in the slope of pre-announcement abnormal institutional holdings on future SUE, not the causal effect of an intervention in SUE. Hedge funds columns 1-3 and nonhedge funds columns 4-6 are grouped outcomes. Columns 1/4 have no FE; 2/5 firm FE; 3/6 firm and quarter FE. All remain conventional DiD, so no OLS-method split. Preferred hedge-fund slope change 0.091; nonhedge-fund slope change -0.160, insignificant. Holdings in percentage points of shares outstanding."
  },
  {
    "sheet": "Settings",
    "cell": "O71",
    "before": null,
    "after": "Correct the model assertion that every column has firm/quarter FE. Binary refers to analyst-exit exposure; continuous SUE is the slope variable. Nonhedge-fund outcome added as hy1. Keep c1 for the hedge-fund column 3 estimate only."
  }
]
```

## 2026-10-10T03:56:44.656955+00:00 — Review 3B6VC3AP s5: causal scope, outcomes and benchmark evidence

22 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H178",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H179",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "H180",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "H181",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I178",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I179",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I180",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "I181",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J178",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J179",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J180",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "J181",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Outcomes",
    "cell": "K178",
    "before": null,
    "after": "Table 8 Panel A columns 1-4: three-month stock CAR from quarter end t to t+1, percent units, adjusted by DGTW portfolio return. Same Y on purchase, large-purchase, sale and large-sale samples; coefficients 2.530, 3.731, -0.184, 0.023 respectively. No further log transformation."
  },
  {
    "sheet": "Outcomes",
    "cell": "K179",
    "before": null,
    "after": "duplicate of y1: same three-month CAR outcome in an alternative trading-direction/size subsample; preserve column variant in setting/y1 description."
  },
  {
    "sheet": "Outcomes",
    "cell": "K180",
    "before": null,
    "after": "duplicate of y1: same three-month CAR outcome in an alternative trading-direction/size subsample; preserve column variant in setting/y1 description."
  },
  {
    "sheet": "Outcomes",
    "cell": "K181",
    "before": null,
    "after": "duplicate of y1: same three-month CAR outcome in an alternative trading-direction/size subsample; preserve column variant in setting/y1 description."
  },
  {
    "sheet": "Settings",
    "cell": "I72",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J72",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K72",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L72",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M72",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O72",
    "before": null,
    "after": "Table 8 Panel A: purchase/large-purchase/sale/large-sale columns use the SAME dependent variable on different samples, grouped here. y2-y4 are duplicate outcome definitions, consolidated into y1. Returns proxy profitability of stocks selected by aggregate holdings changes, not actual transaction-level fund profits. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:56:57.462579+00:00 — Review 3B6VC3AP s6: causal scope, outcomes and benchmark evidence

18 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H182",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H183",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H184",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I182",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I183",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I184",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J182",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J183",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J184",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K182",
    "before": null,
    "after": "Table 9: CAR announcement-window/full-cycle ratio; other transformation. No evidence establishing zero mass."
  },
  {
    "sheet": "Outcomes",
    "cell": "K183",
    "before": null,
    "after": "Table 9: CAR announcement-window/full-cycle ratio; other transformation. No evidence establishing zero mass."
  },
  {
    "sheet": "Outcomes",
    "cell": "K184",
    "before": null,
    "after": "Table 9: CAR announcement-window/full-cycle ratio; other transformation. No evidence establishing zero mass."
  },
  {
    "sheet": "Settings",
    "cell": "I73",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J73",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K73",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L73",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M73",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O73",
    "before": null,
    "after": "Table 9. Binary top-quartile abnormal hedge-fund holdings interaction with the binary coverage shock; not an exogenously assigned participation treatment. Section 5.4 p. 334 explicitly disclaims direct causal identification of hedge-fund activity on efficiency. Retain the authors substantive mechanism interpretation, with endogenous participation/omitted-variable limitations. Insignificance of a coefficient sum is not proof of a zero true effect. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:57:10.627655+00:00 — Review 3B6VC3AP s7: causal scope, outcomes and benchmark evidence

18 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H185",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H186",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H187",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I185",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I186",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I187",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J185",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J186",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J187",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K185",
    "before": null,
    "after": "Table 10: CAR announcement-window/full-cycle ratio; other transformation. No evidence establishing zero mass."
  },
  {
    "sheet": "Outcomes",
    "cell": "K186",
    "before": null,
    "after": "Table 10: CAR announcement-window/full-cycle ratio; other transformation. No evidence establishing zero mass."
  },
  {
    "sheet": "Outcomes",
    "cell": "K187",
    "before": null,
    "after": "Table 10: CAR announcement-window/full-cycle ratio; other transformation. No evidence establishing zero mass."
  },
  {
    "sheet": "Settings",
    "cell": "I74",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J74",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K74",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L74",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M74",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O74",
    "before": null,
    "after": "Table 10. Binary top-quartile abnormal aggregate short interest interaction with the binary coverage shock; not an exogenously assigned participation treatment. Section 5.4 p. 334 explicitly disclaims direct causal identification of hedge-fund activity on efficiency. Retain the authors substantive mechanism interpretation, with endogenous participation/omitted-variable limitations. Insignificance of a coefficient sum is not proof of a zero true effect. Short interest is not a hedge-fund-only measure. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:57:23.908306+00:00 — Review 3B6VC3AP s8: causal scope, outcomes and benchmark evidence

31 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H188",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H189",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H190",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H191",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H192",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H193",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I188",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I189",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I190",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I191",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I192",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I193",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J188",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J189",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J190",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J191",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J192",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J193",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K188",
    "before": null,
    "after": "Table 11 Panel A: absolute deviation from one of a ratio of per-day quote-midpoint return variances. other transformation; zero mass not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K189",
    "before": null,
    "after": "Table 11 Panel A: absolute deviation from one of a ratio of per-day quote-midpoint return variances. other transformation; zero mass not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K190",
    "before": null,
    "after": "Table 11 Panel A: absolute deviation from one of a ratio of per-day quote-midpoint return variances. other transformation; zero mass not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K191",
    "before": null,
    "after": "Table 11 Panel A: absolute deviation from one of a ratio of per-day quote-midpoint return variances. other transformation; zero mass not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K192",
    "before": null,
    "after": "Table 11 Panel A: absolute deviation from one of a ratio of per-day quote-midpoint return variances. other transformation; zero mass not established."
  },
  {
    "sheet": "Outcomes",
    "cell": "K193",
    "before": null,
    "after": "Table 11 Panel A: absolute deviation from one of a ratio of per-day quote-midpoint return variances. other transformation; zero mass not established."
  },
  {
    "sheet": "Settings",
    "cell": "I75",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J75",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K75",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L75",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M75",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N75",
    "before": null,
    "after": "Restrict s8 to Table 11 PANEL A, p. 334: Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Effect on six absolute deviations |1-VR(n,m)|; firm and quarter FE and firm/quarter clustering. Preferred coefficients in column order 0.013, 0.030, 0.029, 0.008, 0.019, 0.024. Larger deviations imply lower efficiency. Panel B mitigation estimand separated as h1."
  },
  {
    "sheet": "Settings",
    "cell": "O75",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:57:36.902713+00:00 — Review 3B6VC3AP s9: causal scope, outcomes and benchmark evidence

11 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H194",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I194",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J194",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K194",
    "before": null,
    "after": "Table 12: next-year EBIT divided by CURRENT total assets; no log of dependent variable. other = asset scaling. log(M/A) is a right-hand-side variable. Zero mass not established."
  },
  {
    "sheet": "Settings",
    "cell": "I76",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J76",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K76",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L76",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M76",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N76",
    "before": null,
    "after": "Restrict s9 to Table 12 columns 1-2, pp. 333-335. Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Annual regression of next-year EBIT/current assets on current log(market capitalization/assets) and treated/post interactions. Firm FE throughout; year FE in column 2; clustering by firm and year. Coverage reduces the valuation-future-earnings slope by -0.013/-0.014. Not an unconditional 1.4-percentage-point earnings decline. Columns 3-4 mitigation estimand separated as h2."
  },
  {
    "sheet": "Settings",
    "cell": "O76",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:57:49.912796+00:00 — Review 3B6VC3AP h1: causal scope, outcomes and benchmark evidence

51 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4222",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4223",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4224",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4225",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4226",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4227",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4222",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4223",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4224",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4225",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4226",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4227",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4222",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4223",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4224",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4225",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4226",
    "before": null,
    "after": "hy5"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4227",
    "before": null,
    "after": "hy6"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4222",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4223",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4224",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4225",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4226",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4227",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4222",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4223",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4224",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4225",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4226",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4227",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4222",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4223",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4224",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4225",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4226",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4227",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4222",
    "before": null,
    "after": "|1-VR(1,5)|: absolute deviation of ratio of per-day quote-midpoint return variances; larger values mean less efficiency."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4223",
    "before": null,
    "after": "|1-VR(1,10)|: absolute deviation of ratio of per-day quote-midpoint return variances; larger values mean less efficiency."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4224",
    "before": null,
    "after": "|1-VR(1,20)|: absolute deviation of ratio of per-day quote-midpoint return variances; larger values mean less efficiency."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4225",
    "before": null,
    "after": "|1-VR(2,5)|: absolute deviation of ratio of per-day quote-midpoint return variances; larger values mean less efficiency."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4226",
    "before": null,
    "after": "|1-VR(2,10)|: absolute deviation of ratio of per-day quote-midpoint return variances; larger values mean less efficiency."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4227",
    "before": null,
    "after": "|1-VR(2,20)|: absolute deviation of ratio of per-day quote-midpoint return variances; larger values mean less efficiency."
  },
  {
    "sheet": "Settings",
    "cell": "A1757",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1757",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Settings",
    "cell": "I1757",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1757",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1757",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1757",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1757",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1757",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 11 Panel B p. 334: differential analyst-exit effect by top-quartile abnormal hedge-fund holdings. Six variance-ratio deviations; firm/quarter FE, firm/quarter clustering. Triple-interaction coefficients -0.024,-0.027,-0.031,-0.027,-0.038,-0.044. Supporting alternative-measure result split from s8."
  },
  {
    "sheet": "Settings",
    "cell": "O1757",
    "before": null,
    "after": "Section 5.4 p. 334 explicitly disclaims direct causal identification of hedge-fund activity on efficiency. Retain the authors substantive mechanism interpretation, with endogenous participation/omitted-variable limitations. Insignificance of a coefficient sum is not proof of a zero true effect. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:58:01.230472+00:00 — Review 3B6VC3AP h2: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4228",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4228",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4228",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4228",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4228",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4228",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4228",
    "before": null,
    "after": "Next-year EBIT/current total assets; no log of Y."
  },
  {
    "sheet": "Settings",
    "cell": "A1758",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1758",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Settings",
    "cell": "I1758",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1758",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1758",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1758",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1758",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1758",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 12 columns 3-4 p. 335: difference in the treatment-induced valuation/future-earnings slope change by high hedge-fund participation. Firm FE; year FE in col. 4; firm/year clustering. Col. 4 baseline slope change -0.019; extra high-participation slope change +0.028. High-participation net slope change +0.009, not the interaction alone. Supporting alternative-measure result split from s9."
  },
  {
    "sheet": "Settings",
    "cell": "O1758",
    "before": null,
    "after": "Section 5.4 p. 334 explicitly disclaims direct causal identification of hedge-fund activity on efficiency. Retain the authors substantive mechanism interpretation, with endogenous participation/omitted-variable limitations. Insignificance of a coefficient sum is not proof of a zero true effect. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:58:13.402297+00:00 — Review 3B6VC3AP h3: causal scope, outcomes and benchmark evidence

23 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4229",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4230",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4229",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4230",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4229",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4230",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4229",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4230",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4229",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4230",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4229",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4230",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4229",
    "before": null,
    "after": "Indicator that at least one nonhedge-fund analyst asks a question."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4230",
    "before": null,
    "after": "Log(1+number of nonhedge-fund analysts asking questions)."
  },
  {
    "sheet": "Settings",
    "cell": "A1759",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1759",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Settings",
    "cell": "I1759",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1759",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1759",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1759",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1759",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1759",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 3 Panel B p. 325: nonhedge-fund participation in conference calls. Firm FE; quarter FE in cols. 2/4; firm/quarter clustering. Preferred indicator effect 0.003; log-count effect 0.006; neither significant. Supporting comparison to the hedge-fund response."
  },
  {
    "sheet": "Settings",
    "cell": "O1759",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:58:25.142938+00:00 — Review 3B6VC3AP h4: causal scope, outcomes and benchmark evidence

51 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4231",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4232",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4233",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4234",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4235",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4236",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4231",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4232",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4233",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4234",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4235",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4236",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4231",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4232",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4233",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4234",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4235",
    "before": null,
    "after": "hy5"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4236",
    "before": null,
    "after": "hy6"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4231",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4232",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4233",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4234",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4235",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4236",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4231",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4232",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4233",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4234",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4235",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4236",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4231",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4232",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4233",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4234",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4235",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4236",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4231",
    "before": null,
    "after": "Log(1+nonhedge-fund quarterly EDGAR requests), all filings."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4232",
    "before": null,
    "after": "Log(1+nonhedge-fund quarterly EDGAR requests), 10-K."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4233",
    "before": null,
    "after": "Log(1+nonhedge-fund quarterly EDGAR requests), 10-Q."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4234",
    "before": null,
    "after": "Log(1+nonhedge-fund quarterly EDGAR requests), 8-K."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4235",
    "before": null,
    "after": "Log(1+nonhedge-fund quarterly EDGAR requests), insider Forms 3/4/5."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4236",
    "before": null,
    "after": "Log(1+nonhedge-fund quarterly EDGAR requests), other filings."
  },
  {
    "sheet": "Settings",
    "cell": "A1760",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1760",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Settings",
    "cell": "I1760",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1760",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1760",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1760",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1760",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1760",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 4 Panel B p. 326: quarterly nonhedge-fund EDGAR searches, February 2003-December 2010. Firm/quarter FE and clustering. All-filings coefficient 0.064 insignificant; insider-filings 0.079 weakly significant. Group six filing outcomes. Supporting institutional-type comparison."
  },
  {
    "sheet": "Settings",
    "cell": "O1760",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:58:37.326830+00:00 — Review 3B6VC3AP h5: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4237",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4237",
    "before": null,
    "after": "h5"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4237",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4237",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4237",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4237",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4237",
    "before": null,
    "after": "Abnormal hedge-fund holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements."
  },
  {
    "sheet": "Settings",
    "cell": "A1761",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1761",
    "before": null,
    "after": "h5"
  },
  {
    "sheet": "Settings",
    "cell": "I1761",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1761",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1761",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1761",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1761",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1761",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 6 Panel B p. 328: heterogeneity in analyst-exit-induced hedge-fund holdings/SUE slope changes by exited analyst career. Firm/quarter FE and clustering. Coefficients 0.143 (leave sell side), 0.043 (stay), 0.132 (join hedge fund), 0.108 (do not join). Group four sample variants. Career choices measured within two years AFTER reduction; not randomly assigned subgroups. Supporting mechanism."
  },
  {
    "sheet": "Settings",
    "cell": "O1761",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:58:48.903112+00:00 — Review 3B6VC3AP h6: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4238",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4238",
    "before": null,
    "after": "h6"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4238",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4238",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4238",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4238",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4238",
    "before": null,
    "after": "Abnormal hedge-fund holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements."
  },
  {
    "sheet": "Settings",
    "cell": "A1762",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1762",
    "before": null,
    "after": "h6"
  },
  {
    "sheet": "Settings",
    "cell": "I1762",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1762",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1762",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1762",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1762",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1762",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 6 Panel C p. 329: holdings/SUE slope-change heterogeneity by analyst accuracy, experience and workload. Firm/quarter FE and clustering. More accurate/experienced/less occupied coefficients 0.218/0.147/0.127; opposite groups 0.008/0.039/0.040. Group six sample variants, not six distinct treatments. Supporting information-loss mechanism."
  },
  {
    "sheet": "Settings",
    "cell": "O1762",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:59:00.516981+00:00 — Review 3B6VC3AP h7: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4239",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4239",
    "before": null,
    "after": "h7"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4239",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4239",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4239",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4239",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4239",
    "before": null,
    "after": "Abnormal hedge-fund holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements."
  },
  {
    "sheet": "Settings",
    "cell": "A1763",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1763",
    "before": null,
    "after": "h7"
  },
  {
    "sheet": "Settings",
    "cell": "I1763",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1763",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1763",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1763",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1763",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1763",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 7 p. 329: holdings/SUE slope changes by pre-event stock size, idiosyncratic volatility and bid-ask spread. Firm/quarter FE and clustering. Small/high-volatility/high-spread coefficients 0.141/0.127/0.144; opposite groups 0.020/0.048/0.054. Group six subsamples. Supports larger responses for opaque stocks; significance in one subgroup but not another alone is not a formal between-group test."
  },
  {
    "sheet": "Settings",
    "cell": "O1763",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:59:12.544511+00:00 — Review 3B6VC3AP h8: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4240",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4240",
    "before": null,
    "after": "h8"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4240",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4240",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4240",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4240",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4240",
    "before": null,
    "after": "Three-month DGTW-adjusted stock return from quarter end t to t+1, percentage units; nonhedge-fund trade-direction samples."
  },
  {
    "sheet": "Settings",
    "cell": "A1764",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1764",
    "before": null,
    "after": "h8"
  },
  {
    "sheet": "Settings",
    "cell": "I1764",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1764",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1764",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1764",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1764",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1764",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table 8 Panel B pp. 330-331: subsequent stock returns conditional on nonhedge-fund purchases, large purchases, sales and large sales. Firm/quarter FE and clustering. Effects 1.084,0.668,-0.521,-0.046 percentage points, all insignificant. Same outcome across four grouped sample variants; profitability proxy, not directly observed transaction profits."
  },
  {
    "sheet": "Settings",
    "cell": "O1764",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:59:24.113040+00:00 — Review 3B6VC3AP h9: causal scope, outcomes and benchmark evidence

30 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4241",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4242",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4243",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4241",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4242",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4243",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4241",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4242",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4243",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4241",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4242",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4243",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4241",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4242",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4243",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4241",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4242",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4243",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4241",
    "before": null,
    "after": "CAR[0,2]/CAR[-21,2], Fama-French 5x5 portfolio-adjusted return ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4242",
    "before": null,
    "after": "CAR[-1,2]/CAR[-21,2], Fama-French 5x5 portfolio-adjusted return ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4243",
    "before": null,
    "after": "CAR[-2,2]/CAR[-21,2], Fama-French 5x5 portfolio-adjusted return ratio."
  },
  {
    "sheet": "Settings",
    "cell": "A1765",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1765",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Settings",
    "cell": "I1765",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1765",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1765",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1765",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1765",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1765",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table A.1 p. 338: alternative price-discovery horizon, day -21 to +2 instead of -63 to +2. Firm FE all columns, quarter FE even columns, firm/quarter clustering. Preferred effects 0.071,0.063,0.067. Three grouped outcomes; supporting substantive horizon robustness."
  },
  {
    "sheet": "Settings",
    "cell": "O1765",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:59:35.889186+00:00 — Review 3B6VC3AP h10: causal scope, outcomes and benchmark evidence

44 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4244",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4245",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4246",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4247",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4248",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4244",
    "before": null,
    "after": "h10"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4245",
    "before": null,
    "after": "h10"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4246",
    "before": null,
    "after": "h10"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4247",
    "before": null,
    "after": "h10"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4248",
    "before": null,
    "after": "h10"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4244",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4245",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4246",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4247",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4248",
    "before": null,
    "after": "hy5"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4244",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4245",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4246",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4247",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4248",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4244",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4245",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4246",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4247",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4248",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4244",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4245",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4246",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4247",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4248",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4244",
    "before": null,
    "after": "Abnormal institutional holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements. Institution: banks."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4245",
    "before": null,
    "after": "Abnormal institutional holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements. Institution: insurance companies."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4246",
    "before": null,
    "after": "Abnormal institutional holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements. Institution: investment companies (mostly mutual funds)."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4247",
    "before": null,
    "after": "Abnormal institutional holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements. Institution: investment advisers."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4248",
    "before": null,
    "after": "Abnormal institutional holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements. Institution: others including university endowments."
  },
  {
    "sheet": "Settings",
    "cell": "A1766",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1766",
    "before": null,
    "after": "h10"
  },
  {
    "sheet": "Settings",
    "cell": "I1766",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1766",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1766",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1766",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1766",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1766",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table A.2 pp. 338-339: nonhedge-fund holdings/SUE slope changes separately for banks, insurers, investment companies, investment advisers and other institutions. Firm/quarter FE and clustering. Triple coefficients -0.001,-0.033,-0.112,-0.007,-0.008, all insignificant. Institution-specific outcomes grouped. Supporting analysis, not excluded for null estimates."
  },
  {
    "sheet": "Settings",
    "cell": "O1766",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:59:47.721519+00:00 — Review 3B6VC3AP h11: causal scope, outcomes and benchmark evidence

30 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4249",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4250",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4251",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4249",
    "before": null,
    "after": "h11"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4250",
    "before": null,
    "after": "h11"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4251",
    "before": null,
    "after": "h11"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4249",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4250",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4251",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4249",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4250",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4251",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4249",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4250",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4251",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4249",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4250",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4251",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4249",
    "before": null,
    "after": "CAR[0,2]/CAR[-63,2], announcement-window abnormal return divided by full-cycle abnormal return."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4250",
    "before": null,
    "after": "CAR[-1,2]/CAR[-63,2], announcement-window abnormal return divided by full-cycle abnormal return."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4251",
    "before": null,
    "after": "CAR[-2,2]/CAR[-63,2], announcement-window abnormal return divided by full-cycle abnormal return."
  },
  {
    "sheet": "Settings",
    "cell": "A1767",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1767",
    "before": null,
    "after": "h11"
  },
  {
    "sheet": "Settings",
    "cell": "I1767",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1767",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1767",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1767",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1767",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1767",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table A.3 Panel A p. 339: restrict treated firms to six-or-more pre-event analysts. Price-jump ratios, firm FE and optional quarter FE; firm/quarter clustering. Preferred effects -0.015,-0.013,-0.009 insignificant. Supporting substantive test that losing one analyst matters less with extensive initial coverage."
  },
  {
    "sheet": "Settings",
    "cell": "O1767",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T03:59:58.979990+00:00 — Review 3B6VC3AP h12: causal scope, outcomes and benchmark evidence

51 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4252",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4253",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4254",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4255",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4256",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4257",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4252",
    "before": null,
    "after": "h12"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4253",
    "before": null,
    "after": "h12"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4254",
    "before": null,
    "after": "h12"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4255",
    "before": null,
    "after": "h12"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4256",
    "before": null,
    "after": "h12"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4257",
    "before": null,
    "after": "h12"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4252",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4253",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4254",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4255",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4256",
    "before": null,
    "after": "hy5"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4257",
    "before": null,
    "after": "hy6"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4252",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4253",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4254",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4255",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4256",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4257",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4252",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4253",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4254",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4255",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4256",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4257",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4252",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4253",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4254",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4255",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4256",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4257",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4252",
    "before": null,
    "after": "Log(1+hedge-fund quarterly EDGAR requests), all filings."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4253",
    "before": null,
    "after": "Log(1+hedge-fund quarterly EDGAR requests), 10-K."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4254",
    "before": null,
    "after": "Log(1+hedge-fund quarterly EDGAR requests), 10-Q."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4255",
    "before": null,
    "after": "Log(1+hedge-fund quarterly EDGAR requests), 8-K."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4256",
    "before": null,
    "after": "Log(1+hedge-fund quarterly EDGAR requests), insider Forms 3/4/5."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4257",
    "before": null,
    "after": "Log(1+hedge-fund quarterly EDGAR requests), other filings."
  },
  {
    "sheet": "Settings",
    "cell": "A1768",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1768",
    "before": null,
    "after": "h12"
  },
  {
    "sheet": "Settings",
    "cell": "I1768",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1768",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1768",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1768",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1768",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1768",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table A.3 Panel B p. 339: six-or-more pre-event analysts; quarterly hedge-fund EDGAR search response, firm/quarter FE and clustering. All-filings effect 0.088; remaining 0.022,-0.029,0.013,0.057,0.071, all insignificant. Supporting substantive information-acquisition test."
  },
  {
    "sheet": "Settings",
    "cell": "O1768",
    "before": null,
    "after": "No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T04:00:11.134970+00:00 — Review 3B6VC3AP h13: causal scope, outcomes and benchmark evidence

30 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4258",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4259",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4260",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4258",
    "before": null,
    "after": "h13"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4259",
    "before": null,
    "after": "h13"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4260",
    "before": null,
    "after": "h13"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4258",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4259",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4260",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4258",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4259",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4260",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4258",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4259",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4260",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4258",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4259",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4260",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4258",
    "before": null,
    "after": "CAR[0,2]/CAR[-63,2], announcement-window abnormal return divided by full-cycle abnormal return."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4259",
    "before": null,
    "after": "CAR[-1,2]/CAR[-63,2], announcement-window abnormal return divided by full-cycle abnormal return."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4260",
    "before": null,
    "after": "CAR[-2,2]/CAR[-63,2], announcement-window abnormal return divided by full-cycle abnormal return."
  },
  {
    "sheet": "Settings",
    "cell": "A1769",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1769",
    "before": null,
    "after": "h13"
  },
  {
    "sheet": "Settings",
    "cell": "I1769",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1769",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1769",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1769",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1769",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1769",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Table A.4 p. 340: participation-mitigation DiD after excluding activist targets and separately prior earnings-guidance firms with their matched controls. Firm/quarter FE and clustering. Actual table columns 1-3 exclude activist targets; 4-6 exclude guiders (prose/header column references are inconsistent). Triple effects -0.133,-0.152,-0.139 and -0.125,-0.119,-0.107. Group two sample variants and three outcomes. Supporting alternative-explanation checks."
  },
  {
    "sheet": "Settings",
    "cell": "O1769",
    "before": null,
    "after": "Section 5.4 p. 334 explicitly disclaims direct causal identification of hedge-fund activity on efficiency. Retain the authors substantive mechanism interpretation, with endogenous participation/omitted-variable limitations. Insignificance of a coefficient sum is not proof of a zero true effect. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T04:00:23.044536+00:00 — Review 3B6VC3AP h14: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4261",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4261",
    "before": null,
    "after": "h14"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4261",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4261",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4261",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4261",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4261",
    "before": null,
    "after": "CAR[0,2]/CAR[-63,2], announcement-window abnormal return divided by full-cycle abnormal return."
  },
  {
    "sheet": "Settings",
    "cell": "A1770",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1770",
    "before": null,
    "after": "h14"
  },
  {
    "sheet": "Settings",
    "cell": "I1770",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1770",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1770",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1770",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1770",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1770",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Figure 1 Panel A, pp. 333-336: dynamic price discovery response. Seven half-year event-time interactions replace Post, baseline [-2,-1.5) years; window two years before/after. Firm/quarter FE and clustering. Authors interpret post-treatment responses as emerging after coverage loss. Supporting dynamic conventional DiD, not modern DiD. Exact point estimates not tabulated; no numerical graph estimates invented."
  },
  {
    "sheet": "Settings",
    "cell": "O1770",
    "before": null,
    "after": "Include substantive post-treatment dynamics discussed in Section 5.3; do not create a separate setting for pretrend diagnostics. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T04:00:34.887378+00:00 — Review 3B6VC3AP h15: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4262",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4262",
    "before": null,
    "after": "h15"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4262",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4262",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4262",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4262",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4262",
    "before": null,
    "after": "|1-VR(1,10)|: absolute deviation of ratio of per-day quote-midpoint return variances; larger values mean less efficiency."
  },
  {
    "sheet": "Settings",
    "cell": "A1771",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1771",
    "before": null,
    "after": "h15"
  },
  {
    "sheet": "Settings",
    "cell": "I1771",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1771",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1771",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1771",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1771",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1771",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Figure 1 Panel B, pp. 333-336: dynamic variance-ratio deviation response. Seven half-year event-time interactions replace Post, baseline [-2,-1.5) years; window two years before/after. Firm/quarter FE and clustering. Authors interpret post-treatment responses as emerging after coverage loss. Supporting dynamic conventional DiD, not modern DiD. Exact point estimates not tabulated; no numerical graph estimates invented."
  },
  {
    "sheet": "Settings",
    "cell": "O1771",
    "before": null,
    "after": "Include substantive post-treatment dynamics discussed in Section 5.3; do not create a separate setting for pretrend diagnostics. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T04:00:46.377995+00:00 — Review 3B6VC3AP h16: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4263",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4263",
    "before": null,
    "after": "h16"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4263",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4263",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4263",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4263",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4263",
    "before": null,
    "after": "Indicator of hedge-fund analyst question participation in conference call."
  },
  {
    "sheet": "Settings",
    "cell": "A1772",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1772",
    "before": null,
    "after": "h16"
  },
  {
    "sheet": "Settings",
    "cell": "I1772",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1772",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1772",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1772",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1772",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1772",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Figure 1 Panel C, pp. 333-336: dynamic conference-call participation response. Seven half-year event-time interactions replace Post, baseline [-2,-1.5) years; window two years before/after. Firm/quarter FE and clustering. Authors interpret post-treatment responses as emerging after coverage loss. Supporting dynamic conventional DiD, not modern DiD. Exact point estimates not tabulated; no numerical graph estimates invented."
  },
  {
    "sheet": "Settings",
    "cell": "O1772",
    "before": null,
    "after": "Include substantive post-treatment dynamics discussed in Section 5.3; do not create a separate setting for pretrend diagnostics. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T04:00:58.150314+00:00 — Review 3B6VC3AP h17: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4264",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4264",
    "before": null,
    "after": "h17"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4264",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4264",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4264",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4264",
    "before": null,
    "after": "log1p"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4264",
    "before": null,
    "after": "Log(1+quarterly hedge-fund EDGAR requests), all filings."
  },
  {
    "sheet": "Settings",
    "cell": "A1773",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1773",
    "before": null,
    "after": "h17"
  },
  {
    "sheet": "Settings",
    "cell": "I1773",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1773",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1773",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1773",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1773",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1773",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Figure 1 Panel D, pp. 333-336: dynamic EDGAR searches response. Seven half-year event-time interactions replace Post, baseline [-2,-1.5) years; window two years before/after. Firm/quarter FE and clustering. Authors interpret post-treatment responses as emerging after coverage loss. Supporting dynamic conventional DiD, not modern DiD. Exact point estimates not tabulated; no numerical graph estimates invented."
  },
  {
    "sheet": "Settings",
    "cell": "O1773",
    "before": null,
    "after": "Include substantive post-treatment dynamics discussed in Section 5.3; do not create a separate setting for pretrend diagnostics. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T04:01:09.705391+00:00 — Review 3B6VC3AP h18: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4265",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4265",
    "before": null,
    "after": "h18"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4265",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4265",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4265",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4265",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4265",
    "before": null,
    "after": "Abnormal hedge-fund holdings, percentage points of shares outstanding: current holdings minus preceding-four-quarter average, measured before earnings announcements."
  },
  {
    "sheet": "Settings",
    "cell": "A1774",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1774",
    "before": null,
    "after": "h18"
  },
  {
    "sheet": "Settings",
    "cell": "I1774",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1774",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1774",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1774",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1774",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1774",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Figure 1 Panel E, pp. 333-336: dynamic holdings sensitivity to future SUE response. Seven half-year event-time interactions replace Post, baseline [-2,-1.5) years; window two years before/after. Firm/quarter FE and clustering. Triple event-time interactions with SUE estimate holdings slope changes. Authors interpret post-treatment responses as emerging after coverage loss. Supporting dynamic conventional DiD, not modern DiD. Exact point estimates not tabulated; no numerical graph estimates invented."
  },
  {
    "sheet": "Settings",
    "cell": "O1774",
    "before": null,
    "after": "Include substantive post-treatment dynamics discussed in Section 5.3; do not create a separate setting for pretrend diagnostics. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T04:01:21.631047+00:00 — Review 3B6VC3AP h19: causal scope, outcomes and benchmark evidence

17 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4266",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4266",
    "before": null,
    "after": "h19"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4266",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4266",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4266",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4266",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4266",
    "before": null,
    "after": "Three-month DGTW-adjusted stock return for hedge-fund purchase sample, percentage units."
  },
  {
    "sheet": "Papers",
    "cell": "E12",
    "before": null,
    "after": "DONE — Human review of main article and included Appendix A. Retained s1-s9 with corrected scope; s8/s9 mitigation estimands separated; added substantive nonhedge-fund, heterogeneity, appendix and post-treatment dynamic analyses. Original model fields preserved. Two qualifying comparisons retained; EDGAR log-percent pseudo-comparison rejected. Benchmark alignment remains unknown where target/reference weighting is not established. Descriptive Table 1 balance and Table 6A career frequencies excluded; pretrend diagnostics not separate settings. No independently tabulated coefficients invented for Figure 1."
  },
  {
    "sheet": "Settings",
    "cell": "A1775",
    "before": null,
    "after": "3B6VC3AP"
  },
  {
    "sheet": "Settings",
    "cell": "B1775",
    "before": null,
    "after": "h19"
  },
  {
    "sheet": "Settings",
    "cell": "I1775",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1775",
    "before": null,
    "after": "DiD_conventional"
  },
  {
    "sheet": "Settings",
    "cell": "K1775",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1775",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1775",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1775",
    "before": null,
    "after": "Binary coverage-reduction exposure due to brokerage closures/mergers; matched treated/control conventional DiD under parallel trends, not randomized hedge-fund participation or an implemented IV. Figure 1 Panel F, pp. 333-336: dynamic profitability on purchased stocks response. Seven half-year event-time interactions replace Post, baseline [-2,-1.5) years; window two years before/after. Firm/quarter FE and clustering. Authors interpret post-treatment responses as emerging after coverage loss. Supporting dynamic conventional DiD, not modern DiD. Exact point estimates not tabulated; no numerical graph estimates invented."
  },
  {
    "sheet": "Settings",
    "cell": "O1775",
    "before": null,
    "after": "Include substantive post-treatment dynamics discussed in Section 5.3; do not create a separate setting for pretrend diagnostics. No qualifying same-outcome mean/SD/level comparison found at this location; significance and coefficient-only percentage interpretations do not qualify."
  }
]
```

## 2026-10-10T05:24:13.979533+00:00 — Saved Excel changes

0 populated-cell value changes. The XLSX also preserves formatting.


## 2026-10-11T01:24:04.192255+00:00 — Review 2LWSD69M s1: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I23",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O23",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 6 Panels A/B, Section 4.4, pp. 394-397: FM/BM portfolio-decile slopes measure univariate or incremental RETURN PREDICTABILITY. Conditioning on the other signal tests predictive spanning, not a causal intervention in firm fundamentals. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:24:22.641985+00:00 — Review 2LWSD69M s2: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I24",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O24",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 6 Panels A/B, Section 4.4, pp. 394-397: FM/BM portfolio-decile slopes measure univariate or incremental RETURN PREDICTABILITY. Conditioning on the other signal tests predictive spanning, not a causal intervention in firm fundamentals. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:24:39.967018+00:00 — Review 2LWSD69M s3: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I25",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O25",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 6 Panels A/B, Section 4.4, pp. 394-397: FM/BM portfolio-decile slopes measure univariate or incremental RETURN PREDICTABILITY. Conditioning on the other signal tests predictive spanning, not a causal intervention in firm fundamentals. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:24:58.028355+00:00 — Review 2LWSD69M s4: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I26",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O26",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 6 Panels A/B, Section 4.4, pp. 394-397: FM/BM portfolio-decile slopes measure univariate or incremental RETURN PREDICTABILITY. Conditioning on the other signal tests predictive spanning, not a causal intervention in firm fundamentals. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:25:15.540650+00:00 — Review 2LWSD69M s5: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I27",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O27",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 6 Panels A/B, Section 4.4, pp. 394-397: FM/BM portfolio-decile slopes measure univariate or incremental RETURN PREDICTABILITY. Conditioning on the other signal tests predictive spanning, not a causal intervention in firm fundamentals. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:25:32.963025+00:00 — Review 2LWSD69M s6: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I28",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O28",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 6 Panels A/B, Section 4.4, pp. 394-397: FM/BM portfolio-decile slopes measure univariate or incremental RETURN PREDICTABILITY. Conditioning on the other signal tests predictive spanning, not a causal intervention in firm fundamentals. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:25:50.435745+00:00 — Review 2LWSD69M s7: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I29",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O29",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel A, Section 5.1, pp. 395,397-398: Size-split portfolio sorts test robustness of return predictability among big/small firms. Neither ranking nor size-group membership is interpreted as an assigned treatment. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:26:07.707050+00:00 — Review 2LWSD69M s8: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I30",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O30",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel A, Section 5.1, pp. 395,397-398: Size-split portfolio sorts test robustness of return predictability among big/small firms. Neither ranking nor size-group membership is interpreted as an assigned treatment. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:26:24.422037+00:00 — Review 2LWSD69M s9: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I31",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O31",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel A, Section 5.1, pp. 395,397-398: Size-split portfolio sorts test robustness of return predictability among big/small firms. Neither ranking nor size-group membership is interpreted as an assigned treatment. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:26:42.118996+00:00 — Review 2LWSD69M s10: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I32",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O32",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel A, Section 5.1, pp. 395,397-398: Size-split portfolio sorts test robustness of return predictability among big/small firms. Neither ranking nor size-group membership is interpreted as an assigned treatment. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:26:59.767824+00:00 — Review 2LWSD69M s11: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I33",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O33",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel B, Section 5.1, pp. 395,398-399: Within/across-industry signal components describe sources of return predictability. These are not interventions on industry or valuation ratios. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:27:17.791239+00:00 — Review 2LWSD69M s12: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I34",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O34",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel B, Section 5.1, pp. 395,398-399: Within/across-industry signal components describe sources of return predictability. These are not interventions on industry or valuation ratios. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:27:34.833870+00:00 — Review 2LWSD69M s13: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I35",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O35",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel B, Section 5.1, pp. 395,398-399: Within/across-industry signal components describe sources of return predictability. These are not interventions on industry or valuation ratios. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:27:52.438817+00:00 — Review 2LWSD69M s14: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I36",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O36",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Table 7 Panel B, Section 5.1, pp. 395,398-399: Within/across-industry signal components describe sources of return predictability. These are not interventions on industry or valuation ratios. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:28:10.090537+00:00 — Review 2LWSD69M s15: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I37",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O37",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 8-9, Section 5.2, pp. 396-397,399-401: Alternative-signal and pooled early/late regressions compare predictive premia. Year indicators and decile-period interactions do not turn this into identifying FE or DiD. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:28:27.233923+00:00 — Review 2LWSD69M s16: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I38",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O38",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 8-9, Section 5.2, pp. 396-397,399-401: Alternative-signal and pooled early/late regressions compare predictive premia. Year indicators and decile-period interactions do not turn this into identifying FE or DiD. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:28:44.922492+00:00 — Review 2LWSD69M s17: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I39",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O39",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 8-9, Section 5.2, pp. 396-397,399-401: Alternative-signal and pooled early/late regressions compare predictive premia. Year indicators and decile-period interactions do not turn this into identifying FE or DiD. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:29:02.846600+00:00 — Review 2LWSD69M s18: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I40",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O40",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 8-9, Section 5.2, pp. 396-397,399-401: Alternative-signal and pooled early/late regressions compare predictive premia. Year indicators and decile-period interactions do not turn this into identifying FE or DiD. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:29:20.594105+00:00 — Review 2LWSD69M s19: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I41",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O41",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 10-11 Panel A, Section 5.4, pp. 398,402-403: Authors explicitly call this the return predictability effect of BM controlling for size, investment, profitability and quality. Predictive covariate adjustment is not causally interpreted regression adjustment. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:29:38.170861+00:00 — Review 2LWSD69M s20: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I42",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O42",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 10-11 Panel A, Section 5.4, pp. 398,402-403: Authors explicitly call this the return predictability effect of BM controlling for size, investment, profitability and quality. Predictive covariate adjustment is not causally interpreted regression adjustment. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:29:55.825840+00:00 — Review 2LWSD69M s21: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I43",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O43",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 10-11 Panel B, Section 5.4, pp. 398,402-403: Composite in-sample/out-of-sample signals are evaluated for combined predictive power; in-sample overfitting/look-ahead is explicitly discussed. This is forecasting/portfolio sorting, not a causal treatment effect. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:30:13.572692+00:00 — Review 2LWSD69M s22: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I44",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O44",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Tables 10-11 Panel B, Section 5.4, pp. 398,402-403: Composite in-sample/out-of-sample signals are evaluated for combined predictive power; in-sample overfitting/look-ahead is explicitly discussed. This is forecasting/portfolio sorting, not a causal treatment effect. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:30:31.706725+00:00 — Review 2LWSD69M s23: causal scope, outcomes and benchmark evidence

11 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K13",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "K14",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "K15",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "K16",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "R13",
    "before": null,
    "after": "Outside causal scope: linked parent s23 is a descriptive/predictive portfolio-sort comparison, not a qualifying causal setting. Preserve the original reported premium comparisons; do not treat them as causal effect/benchmark records."
  },
  {
    "sheet": "Comparisons",
    "cell": "R14",
    "before": null,
    "after": "Outside causal scope: linked parent s23 is a descriptive/predictive portfolio-sort comparison, not a qualifying causal setting. Preserve the original reported premium comparisons; do not treat them as causal effect/benchmark records."
  },
  {
    "sheet": "Comparisons",
    "cell": "R15",
    "before": null,
    "after": "Outside causal scope: linked parent s23 is a descriptive/predictive portfolio-sort comparison, not a qualifying causal setting. Preserve the original reported premium comparisons; do not treat them as causal effect/benchmark records."
  },
  {
    "sheet": "Comparisons",
    "cell": "R16",
    "before": null,
    "after": "Outside causal scope: linked parent s23 is a descriptive/predictive portfolio-sort comparison, not a qualifying causal setting. Preserve the original reported premium comparisons; do not treat them as causal effect/benchmark records."
  },
  {
    "sheet": "Papers",
    "cell": "E9",
    "before": null,
    "after": "DONE — Main-article review: s1-s23 excluded as predictive portfolio sorts/regressions rather than causally interpreted changes in valuation signals. Four linked comparisons excluded with parent s23. Original model fields preserved; rejected-row secondary fields and outcome labels left blank as permitted. Omissions audit covered Tables 1-11, Figures 1-4 and Sections 2-6: VAR/valuation machinery forecasts or constructs FE; correlations, portfolio premia and Figure 4 covariance identity are descriptive/predictive rather than implemented causal estimators. No qualifying missing causal setting identified in the main article. Separate online supplement was not reviewed."
  },
  {
    "sheet": "Settings",
    "cell": "I45",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O45",
    "before": null,
    "after": "Exclude under the pure prediction/descriptive exclusion in the supplied instructions. Figure 1 and Table 5, Section 4.3, pp. 383,391-394: High-minus-low returns summarize portfolios selected by valuation signals. High/low decile membership is not treatment assignment. Comparing FM and BM predictive premia does not by itself establish a causal setting. The paper provides an economic explanation for the apparent premium decline, but does not interpret these signal coefficients as effects of changing X on Y. This decision is about interpretation, not the absence of randomization or remaining endogeneity."
  }
]
```

## 2026-10-11T01:37:02.103533+00:00 — Review 2RLBINN9 s1: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I56",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O56",
    "before": null,
    "after": "Section 5.1 pp. 789-790, Table 2: explicitly in-sample OLS predictive regressions of next-month currency-factor returns on lagged predictors. Economic stories motivate forecasting variables, but coefficients are not implemented causal interventions. Exclude pure prediction; no OLS causal setting is created merely because OLS is used."
  }
]
```

## 2026-10-11T01:37:21.942086+00:00 — Review 2RLBINN9 s2: causal scope, outcomes and benchmark evidence

356 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1152",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1153",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1154",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1155",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1156",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1157",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1158",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1159",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1160",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1161",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1162",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1163",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1164",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1165",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1166",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1167",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1168",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1169",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1170",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1171",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1172",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1173",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1174",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1175",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1176",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1177",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1152",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1153",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1154",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1155",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1156",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1157",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1158",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1159",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1160",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1161",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1162",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1163",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1164",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1165",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1166",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1167",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1168",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1169",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1170",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1171",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1172",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1173",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1174",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1175",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1176",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1177",
    "before": null,
    "after": "s2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1152",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1153",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1154",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1155",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1156",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1157",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1158",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1159",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1160",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1161",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1162",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1163",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1164",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1165",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1166",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1167",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1168",
    "before": null,
    "after": "hc17"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1169",
    "before": null,
    "after": "hc18"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1170",
    "before": null,
    "after": "hc19"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1171",
    "before": null,
    "after": "hc20"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1172",
    "before": null,
    "after": "hc21"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1173",
    "before": null,
    "after": "hc22"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1174",
    "before": null,
    "after": "hc23"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1175",
    "before": null,
    "after": "hc24"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1176",
    "before": null,
    "after": "hc25"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1177",
    "before": null,
    "after": "hc26"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1152",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1153",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1154",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1155",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1156",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1157",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1158",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1159",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1160",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1161",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1162",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1163",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1164",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1165",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1166",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1167",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1168",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1169",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1170",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1171",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1172",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1173",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1174",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1175",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1176",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1177",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K20",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K21",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1152",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1153",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1154",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1155",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1156",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1157",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1158",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1159",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1160",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1161",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1162",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1163",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1164",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1165",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1166",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1167",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1168",
    "before": null,
    "after": "y7"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1169",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1170",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1171",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1172",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1173",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1174",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1175",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1176",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1177",
    "before": null,
    "after": "y8"
  },
  {
    "sheet": "Comparisons",
    "cell": "L20",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L21",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1152",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1153",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1154",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1155",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1156",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1157",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1158",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1159",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1160",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1161",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1162",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1163",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1164",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1165",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1166",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1167",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1168",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1169",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1170",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1171",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1172",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1173",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1174",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1175",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1176",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1177",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M20",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M21",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1152",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1153",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1154",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1155",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1156",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1157",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1158",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1159",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1160",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1161",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1162",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1163",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1164",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1165",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1166",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1167",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1168",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1169",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1170",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1171",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1172",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1173",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1174",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1175",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1176",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1177",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N20",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N21",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1152",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1153",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1154",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1155",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1156",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1157",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1158",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1159",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1160",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1161",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1162",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1163",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1164",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1165",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1166",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1167",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1168",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1169",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1170",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1171",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1172",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1173",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1174",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1175",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1176",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1177",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O20",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O21",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1152",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1153",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1154",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1155",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1156",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1157",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1158",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1159",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1160",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1161",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1162",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1163",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1164",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1165",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1166",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1167",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1168",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1169",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1170",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1171",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1172",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1173",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1174",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1175",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1176",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1177",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P20",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P21",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1152",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, No hedge column: CEQ 0.12%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -4.28 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1153",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Full hedge column: CEQ 2.19%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -2.21 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1154",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Carry column: Sharpe 0.39, DCF Sharpe 0.52, printed DeltaSharpe (alternative minus DCF) -0.13. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1155",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Carry column: CEQ 2.39%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -2.01 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1156",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Value column: Sharpe 0.33, DCF Sharpe 0.52, printed DeltaSharpe (alternative minus DCF) -0.19. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1157",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Value column: CEQ 1.48%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -2.92 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1158",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Momentum column: Sharpe 0.4, DCF Sharpe 0.52, printed DeltaSharpe (alternative minus DCF) -0.12. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1159",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Momentum column: CEQ 2.66%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -1.74 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1160",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, UIP column: Sharpe 0.38, DCF Sharpe 0.52, printed DeltaSharpe (alternative minus DCF) -0.14. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1161",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, UIP column: CEQ 2.33%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -2.07 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1162",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Random walk column: Sharpe 0.39, DCF Sharpe 0.52, printed DeltaSharpe (alternative minus DCF) -0.13. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1163",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Random walk column: CEQ 2.45%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -1.95 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1164",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Interest rates column: Sharpe 0.38, DCF Sharpe 0.52, printed DeltaSharpe (alternative minus DCF) -0.14. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1165",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Interest rates column: CEQ 2.38%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -2.02 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1166",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Model combination column: Sharpe 0.4, DCF Sharpe 0.52, printed DeltaSharpe (alternative minus DCF) -0.12. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1167",
    "before": null,
    "after": "Table 3A p. 792 equal-weight equity, Model combination column: CEQ 2.69%, DCF CEQ 4.4%, printed DeltaCEQ (alternative minus DCF) -1.71 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1168",
    "before": null,
    "after": "p. 792 Table 3A: DCF Sortino 0.76 versus second-best momentum 0.57, described as over 30% larger. Same equal-weight equity OOS path."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1169",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus No hedge theta -0.2%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1170",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus Full hedge theta 2.04%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1171",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus Carry theta 2.16%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1172",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus Value theta 1.33%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1173",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus Momentum theta 2.52%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1174",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus UIP theta 2.2%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1175",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus Random walk theta 2.27%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1176",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus Interest rates theta 2.16%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1177",
    "before": null,
    "after": "p. 792 Table 3A: DCF theta 4.28% versus Model combination theta 2.47%. Prose says around twice as large as all other strategies."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q20",
    "before": null,
    "after": "“We find an equal-weighted global equity portfolio has a statistically higher Sharpe ratio under DCF hedging relative to all nine alternative frameworks. The improvement is over 90% relative to an unhedged portfolio and over 40% relative to a portfolio that fully hedges FX exposure…” [ … ] Table 3 Panel A: “Sharpe 0.52” under DCF, “0.27” under “No hedge”. Location: pp. 782,792 Table 3A. Same portfolio/weighting and Jan 1997-Jul 2017 path."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q21",
    "before": null,
    "after": "“We find an equal-weighted global equity portfolio has a statistically higher Sharpe ratio under DCF hedging relative to all nine alternative frameworks. The improvement is over 90% relative to an unhedged portfolio and over 40% relative to a portfolio that fully hedges FX exposure…” [ … ] Table 3 Panel A: “Sharpe 0.52” under DCF, “0.37” under “Full hedge”. Location: pp. 782,792 Table 3A. Same portfolio/weighting and Jan 1997-Jul 2017 path."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1152",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1153",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1154",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1155",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1156",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1157",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1158",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1159",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1160",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1161",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1162",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1163",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1164",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1165",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1166",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1167",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1169",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1170",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1171",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1172",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1173",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1174",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1175",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1176",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1177",
    "before": null,
    "after": "Broad source wording is not numerically accurate for every comparator, especially negative unhedged theta. Preserve it as an author comparison, not a verified exact multiple."
  },
  {
    "sheet": "Outcomes",
    "cell": "H77",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H78",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H79",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H80",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H81",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H82",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H83",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H84",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H85",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H86",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H87",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H88",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H89",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I77",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I78",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I79",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I80",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I81",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I82",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I83",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I84",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I85",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I86",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I87",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I88",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I89",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J77",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J78",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J79",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J80",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J81",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J82",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J83",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J84",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J85",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J86",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J87",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J88",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J89",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K78",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation of the hedged global equity portfolio, in percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K79",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Out-of-sample Sharpe ratio of the hedged global equity portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K80",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio skewness. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K81",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio kurtosis. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K82",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Maximum drawdown of the portfolio, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K83",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sortino ratio of the portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K84",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Theta performance measure, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K85",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to unhedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K86",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to fully hedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K87",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return (CEQ), percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K88",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee a risk-averse investor would pay to switch to DCF hedging, percent per annum, with relative risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K89",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee a risk-averse investor would pay to switch to DCF hedging, percent per annum, with relative risk aversion 6. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I57",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J57",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K57",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L57",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M57",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O57",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Sections 5.2-5.3 pp. 790-794, Table 3 Panel A. Underlying asset positions held fixed; reported differences attributed to the hedging rule (explicit on p. 791). Retain pairwise DCF-versus-alternative contrasts. Detailed outcome labels reflect reported performance statistics, not raw binary trading signals. Added omitted benchmark comparisons; linked Delta rows are not division."
  }
]
```

## 2026-10-11T01:37:41.024415+00:00 — Review 2RLBINN9 s3: causal scope, outcomes and benchmark evidence

271 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1178",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1179",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1180",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1181",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1182",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1183",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1184",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1185",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1186",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1187",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1188",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1189",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1190",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1191",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1192",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1193",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1194",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1195",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1178",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1179",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1180",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1181",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1182",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1183",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1184",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1185",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1186",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1187",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1188",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1189",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1190",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1191",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1192",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1193",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1194",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1195",
    "before": null,
    "after": "s3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1178",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1179",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1180",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1181",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1182",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1183",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1184",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1185",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1186",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1187",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1188",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1189",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1190",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1191",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1192",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1193",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1194",
    "before": null,
    "after": "hc17"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1195",
    "before": null,
    "after": "hc18"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1178",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1179",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1180",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1181",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1182",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1183",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1184",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1185",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1186",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1187",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1188",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1189",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1190",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1191",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1192",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1193",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1194",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1195",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K22",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K23",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1178",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1179",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1180",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1181",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1182",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1183",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1184",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1185",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1186",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1187",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1188",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1189",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1190",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1191",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1192",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1193",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1194",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1195",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L22",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L23",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1178",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1179",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1180",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1181",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1182",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1183",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1184",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1185",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1186",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1187",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1188",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1189",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1190",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1191",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1192",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1193",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1194",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1195",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M22",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M23",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1178",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1179",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1180",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1181",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1182",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1183",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1184",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1185",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1186",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1187",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1188",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1189",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1190",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1191",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1192",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1193",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1194",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1195",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N22",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N23",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1178",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1179",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1180",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1181",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1182",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1183",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1184",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1185",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1186",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1187",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1188",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1189",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1190",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1191",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1192",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1193",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1194",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1195",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O22",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O23",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1178",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1179",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1180",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1181",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1182",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1183",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1184",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1185",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1186",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1187",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1188",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1189",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1190",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1191",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1192",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1193",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1194",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1195",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P22",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P23",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1178",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, No hedge column: Sharpe 0.2, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.2. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1179",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, No hedge column: CEQ -0.84%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -3.5 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1180",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Full hedge column: Sharpe 0.31, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.09. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1181",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Full hedge column: CEQ 1.29%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -1.37 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1182",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Carry column: Sharpe 0.33, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.07. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1183",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Carry column: CEQ 1.47%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -1.19 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1184",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Value column: Sharpe 0.25, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.15. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1185",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Value column: CEQ 0.35%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -2.31 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1186",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Momentum column: Sharpe 0.36, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.04. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1187",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Momentum column: CEQ 1.92%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -0.74 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1188",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, UIP column: Sharpe 0.33, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.07. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1189",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, UIP column: CEQ 1.72%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -0.94 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1190",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Random walk column: Sharpe 0.32, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.08. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1191",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Random walk column: CEQ 1.55%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -1.11 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1192",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Interest rates column: Sharpe 0.31, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.09. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1193",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Interest rates column: CEQ 1.18%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -1.48 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1194",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Model combination column: Sharpe 0.34, DCF Sharpe 0.4, printed DeltaSharpe (alternative minus DCF) -0.06. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1195",
    "before": null,
    "after": "Table 3B p. 792 GDP-weight equity, Model combination column: CEQ 1.69%, DCF CEQ 2.66%, printed DeltaCEQ (alternative minus DCF) -0.97 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q22",
    "before": null,
    "after": "“Nonetheless, DCF hedging is still found to generate the highest average annualized return of 6.16%, which is over 80% higher than the unhedged portfolio (3.36%) and over 35% higher than the fully hedged portfolio (4.51%).” Location: pp. 792-793 Table 3B. Same portfolio/weighting and Jan 1997-Jul 2017 path."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q23",
    "before": null,
    "after": "“Nonetheless, DCF hedging is still found to generate the highest average annualized return of 6.16%, which is over 80% higher than the unhedged portfolio (3.36%) and over 35% higher than the fully hedged portfolio (4.51%).” Location: pp. 792-793 Table 3B. Same portfolio/weighting and Jan 1997-Jul 2017 path."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1178",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1179",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1180",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1181",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1182",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1183",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1184",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1185",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1186",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1187",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1188",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1189",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1190",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1191",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1192",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1193",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1194",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1195",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R22",
    "before": null,
    "after": "Benchmark is explicitly the annualized mean return under the comparator rule, not other_level. Matched within the fixed-price-path strategy counterfactual; not a general-population causal identification claim."
  },
  {
    "sheet": "Comparisons",
    "cell": "R23",
    "before": null,
    "after": "Benchmark is explicitly the annualized mean return under the comparator rule, not other_level. Matched within the fixed-price-path strategy counterfactual; not a general-population causal identification claim."
  },
  {
    "sheet": "Outcomes",
    "cell": "H100",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H101",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H102",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H90",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H91",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H92",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H93",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H94",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H95",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H96",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H97",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H98",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H99",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I100",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I101",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I102",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I90",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I91",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I92",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I93",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I94",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I95",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I96",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I97",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I98",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I99",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J100",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J101",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J102",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J90",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J91",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J92",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J93",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J94",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J95",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J96",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J97",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J98",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J99",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K100",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K101",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to DCF, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K102",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to DCF, percent per annum, risk aversion 6. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K91",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K92",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Out-of-sample Sharpe ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K93",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio skewness. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K94",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio kurtosis. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K95",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Maximum drawdown, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K96",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sortino ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K97",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Theta performance measure, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K98",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to unhedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K99",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to fully hedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I58",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J58",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K58",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L58",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M58",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O58",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Sections 5.2-5.3 pp. 790-794, Table 3 Panel B. Underlying asset positions held fixed; reported differences attributed to the hedging rule (explicit on p. 791). Retain pairwise DCF-versus-alternative contrasts. Detailed outcome labels reflect reported performance statistics, not raw binary trading signals. Added omitted benchmark comparisons; linked Delta rows are not division. The p. 793 3% performance fee versus 3.36% mean return compares different outcomes and is not added as a same-outcome benchmark."
  }
]
```

## 2026-10-11T01:38:00.683924+00:00 — Review 2RLBINN9 s4: causal scope, outcomes and benchmark evidence

438 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1196",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1197",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1198",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1199",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1200",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1201",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1202",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1203",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1204",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1205",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1206",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1207",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1208",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1209",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1210",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1211",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1212",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1213",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1214",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1215",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1216",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1217",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1218",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1219",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1220",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1221",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1222",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1223",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1224",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1225",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1226",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1227",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1228",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1229",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1196",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1197",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1198",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1199",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1200",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1201",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1202",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1203",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1204",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1205",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1206",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1207",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1208",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1209",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1210",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1211",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1212",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1213",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1214",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1215",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1216",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1217",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1218",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1219",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1220",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1221",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1222",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1223",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1224",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1225",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1226",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1227",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1228",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1229",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1196",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1197",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1198",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1199",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1200",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1201",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1202",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1203",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1204",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1205",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1206",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1207",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1208",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1209",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1210",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1211",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1212",
    "before": null,
    "after": "hc17"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1213",
    "before": null,
    "after": "hc18"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1214",
    "before": null,
    "after": "hc19"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1215",
    "before": null,
    "after": "hc20"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1216",
    "before": null,
    "after": "hc21"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1217",
    "before": null,
    "after": "hc22"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1218",
    "before": null,
    "after": "hc23"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1219",
    "before": null,
    "after": "hc24"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1220",
    "before": null,
    "after": "hc25"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1221",
    "before": null,
    "after": "hc26"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1222",
    "before": null,
    "after": "hc27"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1223",
    "before": null,
    "after": "hc28"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1224",
    "before": null,
    "after": "hc29"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1225",
    "before": null,
    "after": "hc30"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1226",
    "before": null,
    "after": "hc31"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1227",
    "before": null,
    "after": "hc32"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1228",
    "before": null,
    "after": "hc33"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1229",
    "before": null,
    "after": "hc34"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1196",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1197",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1198",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1199",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1200",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1201",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1202",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1203",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1204",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1205",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1206",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1207",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1208",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1209",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1210",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1211",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1212",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1213",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1214",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1215",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1216",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1217",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1218",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1219",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1220",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1221",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1222",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1223",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1224",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1225",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1226",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1227",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1228",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1229",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K24",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1196",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1197",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1198",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1199",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1200",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1201",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1202",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1203",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1204",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1205",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1206",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1207",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1208",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1209",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1210",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1211",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1212",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1213",
    "before": null,
    "after": "y2"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1214",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1215",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1216",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1217",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1218",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1219",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1220",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1221",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1222",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1223",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1224",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1225",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1226",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1227",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1228",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1229",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L24",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1196",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1197",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1198",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1199",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1200",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1201",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1202",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1203",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1204",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1205",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1206",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1207",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1208",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1209",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1210",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1211",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1212",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1213",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1214",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1215",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1216",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1217",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1218",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1219",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1220",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1221",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1222",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1223",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1224",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1225",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1226",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1227",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1228",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1229",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M24",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1196",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1197",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1198",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1199",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1200",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1201",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1202",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1203",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1204",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1205",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1206",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1207",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1208",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1209",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1210",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1211",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1212",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1213",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1214",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1215",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1216",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1217",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1218",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1219",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1220",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1221",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1222",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1223",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1224",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1225",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1226",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1227",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1228",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1229",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N24",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1196",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1197",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1198",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1199",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1200",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1201",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1202",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1203",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1204",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1205",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1206",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1207",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1208",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1209",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1210",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1211",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1212",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1213",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1214",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1215",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1216",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1217",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1218",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1219",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1220",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1221",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1222",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1223",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1224",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1225",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1226",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1227",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1228",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1229",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O24",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1196",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1197",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1198",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1199",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1200",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1201",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1202",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1203",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1204",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1205",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1206",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1207",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1208",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1209",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1210",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1211",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1212",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1213",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1214",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1215",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1216",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1217",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1218",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1219",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1220",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1221",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1222",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1223",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1224",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1225",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1226",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1227",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1228",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1229",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P24",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1196",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, No hedge column: Sharpe 0.25, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.52. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1197",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, No hedge column: CEQ 1.06%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -3.46 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1198",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Full hedge column: CEQ 2.19%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -2.33 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1199",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Carry column: Sharpe 0.57, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.2. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1200",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Carry column: CEQ 3.18%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -1.34 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1201",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Value column: Sharpe 0.34, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.43. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1202",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Value column: CEQ 1.65%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -2.87 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1203",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Momentum column: Sharpe 0.54, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.23. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1204",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Momentum column: CEQ 2.96%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -1.56 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1205",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, UIP column: Sharpe 0.42, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.35. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1206",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, UIP column: CEQ 1.62%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -2.9 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1207",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Random walk column: Sharpe 0.53, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.24. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1208",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Random walk column: CEQ 2.65%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -1.87 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1209",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Interest rates column: Sharpe 0.49, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.28. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1210",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Interest rates column: CEQ 2.5%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -2.02 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1211",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Model combination column: Sharpe 0.5, DCF Sharpe 0.77, printed DeltaSharpe (alternative minus DCF) -0.27. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1212",
    "before": null,
    "after": "Table 4A p. 794 equal-weight bond, Model combination column: CEQ 2.64%, DCF CEQ 4.52%, printed DeltaCEQ (alternative minus DCF) -1.88 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1213",
    "before": null,
    "after": "p. 793 and Table 4: full hedge volatility 4.66% versus unhedged 9.23%, described as a 50% reduction. Same weighting and OOS path. This is an alternative-rule contrast included in this multi-arm setting."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1214",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Full hedge 0.01, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1215",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Carry 0.11, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1216",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Value 0.0, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1217",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Momentum 0.07, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1218",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, UIP -0.02, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1219",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Random walk 0.05, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1220",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Interest rates 0.04, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1221",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Model combination 0.05, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1222",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, No hedge -0.01, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1223",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Carry 0.07, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1224",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Value -0.01, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1225",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Momentum 0.07, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1226",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, UIP -0.12, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1227",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Random walk 0.05, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1228",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Interest rates 0.04, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1229",
    "before": null,
    "after": "p. 793 Table 4A: DCF information ratio 0.15, Model combination 0.05, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q24",
    "before": null,
    "after": "“Furthermore, fully hedging FX exposure is often viewed as the optimal approach to managing global bond portfolios (Campbell et al., 2010); yet when evaluating a global bond portfolio, DCF hedging is found to deliver a Sharpe ratio that is over 40% higher than the fully hedged portfolio.” [ … ] Table 4 Panel A: “Sharpe 0.77” under DCF and “0.54” under “Full hedge”. Location: pp. 783,794 Table 4A. Same portfolio/weighting and Jan 1997-Jul 2017 path."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1196",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1197",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1198",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1199",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1200",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1201",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1202",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1203",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1204",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1205",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1206",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1207",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1208",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1209",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1210",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1211",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1212",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1213",
    "before": null,
    "after": "Benchmark is a LEVEL of the volatility outcome, not an SD of that volatility statistic. Thus other_level, not outcome_sd."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1214",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1215",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1216",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1217",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1218",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1219",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1220",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1221",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1222",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1223",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1224",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1225",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1226",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1227",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1228",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1229",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "H103",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H104",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H105",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H106",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H107",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H108",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H109",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H110",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H111",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H112",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H113",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H114",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H115",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I103",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I104",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I105",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I106",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I107",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I108",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I109",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I110",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I111",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I112",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I113",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I114",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I115",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J103",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J104",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J105",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J106",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J107",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J108",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J109",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J110",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J111",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J112",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J113",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J114",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J115",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K104",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K105",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Out-of-sample Sharpe ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K106",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio skewness. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K107",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio kurtosis. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K108",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Maximum drawdown, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K109",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sortino ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K110",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Theta performance measure, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K111",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to unhedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K112",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to fully hedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K113",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K114",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to DCF, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K115",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to DCF, percent per annum, risk aversion 6. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I59",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J59",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K59",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L59",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M59",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O59",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Sections 5.2-5.3 pp. 790-794, Table 4 Panel A. Underlying asset positions held fixed; reported differences attributed to the hedging rule (explicit on p. 791). Retain pairwise DCF-versus-alternative contrasts. Detailed outcome labels reflect reported performance statistics, not raw binary trading signals. Added omitted benchmark comparisons; linked Delta rows are not division."
  }
]
```

## 2026-10-11T01:38:19.653233+00:00 — Review 2RLBINN9 s5: causal scope, outcomes and benchmark evidence

442 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1230",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1231",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1232",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1233",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1234",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1235",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1236",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1237",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1238",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1239",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1240",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1241",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1242",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1243",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1244",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1245",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1246",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1247",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1248",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1249",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1250",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1251",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1252",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1253",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1254",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1255",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1256",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1257",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1258",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1259",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1260",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1261",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1262",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1263",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1264",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1230",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1231",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1232",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1233",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1234",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1235",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1236",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1237",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1238",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1239",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1240",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1241",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1242",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1243",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1244",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1245",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1246",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1247",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1248",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1249",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1250",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1251",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1252",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1253",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1254",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1255",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1256",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1257",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1258",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1259",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1260",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1261",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1262",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1263",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1264",
    "before": null,
    "after": "s5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1230",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1231",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1232",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1233",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1234",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1235",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1236",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1237",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1238",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1239",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1240",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1241",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1242",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1243",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1244",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1245",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1246",
    "before": null,
    "after": "hc17"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1247",
    "before": null,
    "after": "hc18"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1248",
    "before": null,
    "after": "hc19"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1249",
    "before": null,
    "after": "hc20"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1250",
    "before": null,
    "after": "hc21"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1251",
    "before": null,
    "after": "hc22"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1252",
    "before": null,
    "after": "hc23"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1253",
    "before": null,
    "after": "hc24"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1254",
    "before": null,
    "after": "hc25"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1255",
    "before": null,
    "after": "hc26"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1256",
    "before": null,
    "after": "hc27"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1257",
    "before": null,
    "after": "hc28"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1258",
    "before": null,
    "after": "hc29"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1259",
    "before": null,
    "after": "hc30"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1260",
    "before": null,
    "after": "hc31"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1261",
    "before": null,
    "after": "hc32"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1262",
    "before": null,
    "after": "hc33"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1263",
    "before": null,
    "after": "hc34"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1264",
    "before": null,
    "after": "hc35"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1230",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1231",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1232",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1233",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1234",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1235",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1236",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1237",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1238",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1239",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1240",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1241",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1242",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1243",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1244",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1245",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1246",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1247",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1248",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1249",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1250",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1251",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1252",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1253",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1254",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1255",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1256",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1257",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1258",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1259",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1260",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1261",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1262",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1263",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1264",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1230",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1231",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1232",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1233",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1234",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1235",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1236",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1237",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1238",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1239",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1240",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1241",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1242",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1243",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1244",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1245",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1246",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1247",
    "before": null,
    "after": "y11"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1248",
    "before": null,
    "after": "y2"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1249",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1250",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1251",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1252",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1253",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1254",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1255",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1256",
    "before": null,
    "after": "y9"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1257",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1258",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1259",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1260",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1261",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1262",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1263",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1264",
    "before": null,
    "after": "y10"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1230",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1231",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1232",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1233",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1234",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1235",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1236",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1237",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1238",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1239",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1240",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1241",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1242",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1243",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1244",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1245",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1246",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1247",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1248",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1249",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1250",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1251",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1252",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1253",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1254",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1255",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1256",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1257",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1258",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1259",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1260",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1261",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1262",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1263",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1264",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1230",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1231",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1232",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1233",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1234",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1235",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1236",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1237",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1238",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1239",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1240",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1241",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1242",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1243",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1244",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1245",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1246",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1247",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1248",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1249",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1250",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1251",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1252",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1253",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1254",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1255",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1256",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1257",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1258",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1259",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1260",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1261",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1262",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1263",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1264",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1230",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1231",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1232",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1233",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1234",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1235",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1236",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1237",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1238",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1239",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1240",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1241",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1242",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1243",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1244",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1245",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1246",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1247",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1248",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1249",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1250",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1251",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1252",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1253",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1254",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1255",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1256",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1257",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1258",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1259",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1260",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1261",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1262",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1263",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1264",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1230",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1231",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1232",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1233",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1234",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1235",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1236",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1237",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1238",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1239",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1240",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1241",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1242",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1243",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1244",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1245",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1246",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1247",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1248",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1249",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1250",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1251",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1252",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1253",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1254",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1255",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1256",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1257",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1258",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1259",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1260",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1261",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1262",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1263",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1264",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1230",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, No hedge column: Sharpe 0.18, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.57. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1231",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, No hedge column: CEQ 0.47%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -3.23 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1232",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Full hedge column: Sharpe 0.64, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.11. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1233",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Full hedge column: CEQ 2.42%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -1.28 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1234",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Carry column: Sharpe 0.61, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.14. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1235",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Carry column: CEQ 2.94%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -0.76 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1236",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Value column: Sharpe 0.3, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.45. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1237",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Value column: CEQ 1.33%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -2.37 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1238",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Momentum column: Sharpe 0.57, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.18. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1239",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Momentum column: CEQ 3.03%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -0.67 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1240",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, UIP column: Sharpe 0.54, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.21. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1241",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, UIP column: CEQ 2.0%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -1.7 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1242",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Random walk column: Sharpe 0.59, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.16. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1243",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Random walk column: CEQ 2.57%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -1.13 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1244",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Interest rates column: Sharpe 0.46, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.29. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1245",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Interest rates column: CEQ 2.17%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -1.53 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1246",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Model combination column: Sharpe 0.52, DCF Sharpe 0.75, printed DeltaSharpe (alternative minus DCF) -0.23. Paired level benchmark for this strategy contrast; Jan 1997-Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1247",
    "before": null,
    "after": "Table 4B p. 794 GDP-weight bond, Model combination column: CEQ 2.53%, DCF CEQ 3.7%, printed DeltaCEQ (alternative minus DCF) -1.17 percentage points. Same fixed asset portfolio/path; gamma=3."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1248",
    "before": null,
    "after": "p. 793 and Table 4: full hedge volatility 4.23% versus unhedged 8.48%, described as a 50% reduction. Same weighting and OOS path. This is an alternative-rule contrast included in this multi-arm setting."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1249",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, Full hedge 0.05, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1250",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, Carry 0.11, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1251",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, Value 0.03, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1252",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, Momentum 0.13, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1253",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, UIP 0.03, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1254",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, Random walk 0.07, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1255",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, Interest rates 0.06, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1256",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.14, Model combination 0.08, relative to unhedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1257",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, No hedge -0.05, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1258",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, Carry 0.06, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1259",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, Value -0.04, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1260",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, Momentum 0.06, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1261",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, UIP -0.1, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1262",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, Random walk 0.03, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1263",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, Interest rates 0.0, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1264",
    "before": null,
    "after": "p. 793 Table 4B: DCF information ratio 0.11, Model combination 0.03, relative to fully hedged. Prose describes DCF as over twice the magnitude of any other strategy."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1230",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1231",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1232",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1233",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1234",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1235",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1236",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1237",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1238",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1239",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1240",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1241",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1242",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1243",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1244",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1245",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1246",
    "before": null,
    "after": "Explicit contrast/level pairing; no ratio computed by authors in this record. Original prose-normalized triples are not duplicated."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1247",
    "before": null,
    "after": "Utility-equivalent return level, not an unconditional mean return; other_level. Printed delta preserved."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1248",
    "before": null,
    "after": "Benchmark is a LEVEL of the volatility outcome, not an SD of that volatility statistic. Thus other_level, not outcome_sd."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1249",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1250",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1251",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1252",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1253",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1254",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1255",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1256",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1257",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1258",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1259",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1260",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1261",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1262",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1263",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1264",
    "before": null,
    "after": "Author wording is broader than the table supports (some benchmarks are zero/negative or more than half the DCF value). Preserve statement and source values; do not endorse an exact ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "H116",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H117",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H118",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H119",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H120",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H121",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H122",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H123",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H124",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H125",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H126",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H127",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H128",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I116",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I117",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I118",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I119",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I120",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I121",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I122",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I123",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I124",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I125",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I126",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I127",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I128",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J116",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J117",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J118",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J119",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J120",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J121",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J122",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J123",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J124",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J125",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J126",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J127",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J128",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K117",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K118",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Out-of-sample Sharpe ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K119",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio skewness. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K120",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Portfolio kurtosis. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K121",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Maximum drawdown, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K122",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sortino ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K123",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Theta performance measure, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K124",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to unhedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K125",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to fully hedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K126",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K127",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to DCF, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K128",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to DCF, percent per annum, risk aversion 6. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I60",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J60",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K60",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L60",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M60",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O60",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Sections 5.2-5.3 pp. 790-794, Table 4 Panel B. Underlying asset positions held fixed; reported differences attributed to the hedging rule (explicit on p. 791). Retain pairwise DCF-versus-alternative contrasts. Detailed outcome labels reflect reported performance statistics, not raw binary trading signals. Added omitted benchmark comparisons; linked Delta rows are not division."
  }
]
```

## 2026-10-11T01:38:39.161465+00:00 — Review 2RLBINN9 s6: causal scope, outcomes and benchmark evidence

382 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1265",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1266",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1267",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1268",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1269",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1270",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1271",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1272",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1273",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1274",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1275",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1276",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1277",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1278",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1279",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1280",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1281",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1282",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1283",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1284",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1285",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1286",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1287",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1288",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1289",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1290",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1291",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1292",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1293",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1294",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1295",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1296",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1265",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1266",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1267",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1268",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1269",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1270",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1271",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1272",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1273",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1274",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1275",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1276",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1277",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1278",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1279",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1280",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1281",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1282",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1283",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1284",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1285",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1286",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1287",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1288",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1289",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1290",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1291",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1292",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1293",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1294",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1295",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1296",
    "before": null,
    "after": "s6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1265",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1266",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1267",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1268",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1269",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1270",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1271",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1272",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1273",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1274",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1275",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1276",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1277",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1278",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1279",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1280",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1281",
    "before": null,
    "after": "hc17"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1282",
    "before": null,
    "after": "hc18"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1283",
    "before": null,
    "after": "hc19"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1284",
    "before": null,
    "after": "hc20"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1285",
    "before": null,
    "after": "hc21"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1286",
    "before": null,
    "after": "hc22"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1287",
    "before": null,
    "after": "hc23"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1288",
    "before": null,
    "after": "hc24"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1289",
    "before": null,
    "after": "hc25"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1290",
    "before": null,
    "after": "hc26"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1291",
    "before": null,
    "after": "hc27"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1292",
    "before": null,
    "after": "hc28"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1293",
    "before": null,
    "after": "hc29"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1294",
    "before": null,
    "after": "hc30"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1295",
    "before": null,
    "after": "hc31"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1296",
    "before": null,
    "after": "hc32"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1265",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1266",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1267",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1268",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1269",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1270",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1271",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1272",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1273",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1274",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1275",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1276",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1277",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1278",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1279",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1280",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1281",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1282",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1283",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1284",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1285",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1286",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1287",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1288",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1289",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1290",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1291",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1292",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1293",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1294",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1295",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1296",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1265",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1266",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1267",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1268",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1269",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1270",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1271",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1272",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1273",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1274",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1275",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1276",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1277",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1278",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1279",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1280",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1281",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1282",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1283",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1284",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1285",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1286",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1287",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1288",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1289",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1290",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1291",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1292",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1293",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1294",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1295",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1296",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1265",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1266",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1267",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1268",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1269",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1270",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1271",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1272",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1273",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1274",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1275",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1276",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1277",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1278",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1279",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1280",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1281",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1282",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1283",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1284",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1285",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1286",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1287",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1288",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1289",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1290",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1291",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1292",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1293",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1294",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1295",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1296",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1265",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1266",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1267",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1268",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1269",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1270",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1271",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1272",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1273",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1274",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1275",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1276",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1277",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1278",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1279",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1280",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1281",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1282",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1283",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1284",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1285",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1286",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1287",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1288",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1289",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1290",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1291",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1292",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1293",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1294",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1295",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1296",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1265",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1266",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1267",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1268",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1269",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1270",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1271",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1272",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1273",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1274",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1275",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1276",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1277",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1278",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1279",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1280",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1281",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1282",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1283",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1284",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1285",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1286",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1287",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1288",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1289",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1290",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1291",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1292",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1293",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1294",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1295",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1296",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1265",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1266",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1267",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1268",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1269",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1270",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1271",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1272",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1273",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1274",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1275",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1276",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1277",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1278",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1279",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1280",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1281",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1282",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1283",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1284",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1285",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1286",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1287",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1288",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1289",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1290",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1291",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1292",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1293",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1294",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1295",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1296",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1265",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Realized: Sharpe 0.47 versus baseline 0.52; printed DeltaSharpe -0.05."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1266",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Realized: CEQ 3.62% versus baseline 4.4%; printed DeltaCEQ -0.78 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1267",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Realized with shrinkage: Sharpe 0.47 versus baseline 0.52; printed DeltaSharpe -0.05."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1268",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Realized with shrinkage: CEQ 3.65% versus baseline 4.4%; printed DeltaCEQ -0.75 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1269",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Diagonal: Sharpe 0.49 versus baseline 0.52; printed DeltaSharpe -0.03."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1270",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Diagonal: CEQ 4.01% versus baseline 4.4%; printed DeltaCEQ -0.39 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1271",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Actual future covariance: Sharpe 0.47 versus baseline 0.52; printed DeltaSharpe -0.05."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1272",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Actual future covariance: CEQ 3.62% versus baseline 4.4%; printed DeltaCEQ -0.78 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1273",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Realized: Sharpe 0.76 versus baseline 0.77; printed DeltaSharpe -0.01."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1274",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Realized: CEQ 4.48% versus baseline 4.52%; printed DeltaCEQ -0.04 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1275",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Realized with shrinkage: Sharpe 0.76 versus baseline 0.77; printed DeltaSharpe -0.01."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1276",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Realized with shrinkage: CEQ 4.47% versus baseline 4.52%; printed DeltaCEQ -0.05 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1277",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Diagonal: Sharpe 0.73 versus baseline 0.77; printed DeltaSharpe -0.04."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1278",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Diagonal: CEQ 4.44% versus baseline 4.52%; printed DeltaCEQ -0.08 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1279",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Actual future covariance: Sharpe 0.73 versus baseline 0.77; printed DeltaSharpe -0.04."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1280",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Actual future covariance: CEQ 4.27% versus baseline 4.52%; printed DeltaCEQ -0.25 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1281",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Realized: Sharpe 0.35 versus baseline 0.4; printed DeltaSharpe -0.05."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1282",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Realized: CEQ 1.83% versus baseline 2.66%; printed DeltaCEQ -0.83 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1283",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Realized with shrinkage: Sharpe 0.35 versus baseline 0.4; printed DeltaSharpe -0.05."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1284",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Realized with shrinkage: CEQ 1.89% versus baseline 2.66%; printed DeltaCEQ -0.77 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1285",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Diagonal: Sharpe 0.38 versus baseline 0.4; printed DeltaSharpe -0.02."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1286",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Diagonal: CEQ 2.35% versus baseline 2.66%; printed DeltaCEQ -0.31 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1287",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Actual future covariance: Sharpe 0.37 versus baseline 0.4; printed DeltaSharpe -0.03."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1288",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Actual future covariance: CEQ 2.14% versus baseline 2.66%; printed DeltaCEQ -0.52 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1289",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Realized: Sharpe 0.73 versus baseline 0.75; printed DeltaSharpe -0.02."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1290",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Realized: CEQ 3.57% versus baseline 3.7%; printed DeltaCEQ -0.13 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1291",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Realized with shrinkage: Sharpe 0.73 versus baseline 0.75; printed DeltaSharpe -0.02."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1292",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Realized with shrinkage: CEQ 3.56% versus baseline 3.7%; printed DeltaCEQ -0.14 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1293",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Diagonal: Sharpe 0.72 versus baseline 0.75; printed DeltaSharpe -0.03."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1294",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Diagonal: CEQ 3.7% versus baseline 3.7%; printed DeltaCEQ 0.0 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1295",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Actual future covariance: Sharpe 0.71 versus baseline 0.75; printed DeltaSharpe -0.04."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1296",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Actual future covariance: CEQ 3.44% versus baseline 3.7%; printed DeltaCEQ -0.26 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1265",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1266",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1267",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1268",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1269",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1270",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1271",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1272",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1273",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1274",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1275",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1276",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1277",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1278",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1279",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1280",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1281",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1282",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1283",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1284",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1285",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1286",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1287",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1288",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1289",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1290",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1291",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1292",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1293",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1294",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1295",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1296",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Outcomes",
    "cell": "H129",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H130",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H131",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H132",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H133",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H134",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I129",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I130",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I131",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I132",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I133",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I134",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J129",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J130",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J131",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J132",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J133",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J134",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K130",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K131",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sharpe ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K132",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K133",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to baseline DCF, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K134",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to baseline DCF, percent per annum, risk aversion 6. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I61",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J61",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K61",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L61",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M61",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N61",
    "before": null,
    "after": "Table 5, p. 795: restrict s6 to covariance-input replacements relative to historical 60-month DCF covariance: realized, realized with shrinkage, diagonal, and actual future covariance. Group equity/bond and equal/GDP variants, but move Actual rets to h1 because it changes the expected-return information instead. Actual covar is an infeasible perfect-foresight comparison, not an implementable forecast."
  },
  {
    "sheet": "Settings",
    "cell": "O61",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Section 6.1 pp. 793-796. Covariance construction is the focal rule component; no claim of a market-price response. Keep reported delta rows literally where rounded levels differ."
  }
]
```

## 2026-10-11T01:38:57.864018+00:00 — Review 2RLBINN9 s7: causal scope, outcomes and benchmark evidence

22 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H135",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H136",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H137",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H138",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I135",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I136",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I137",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I138",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J135",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J136",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J137",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J138",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K135",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sharpe ratio of the DCF-hedged global portfolio from the given investor's home-country perspective. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K136",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return of the DCF-hedged global portfolio, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K137",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch from an unhedged portfolio to DCF hedging, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K138",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch from a fully hedged portfolio to DCF hedging, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I62",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J62",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K62",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L62",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M62",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O62",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Table 6 pp. 796-797: same DCF adoption comparisons across home-currency perspectives; routine country/weight variants grouped. Ranks such as 1/10 or 95% of tests are NOT effect/outcome-level ratios. Comparator Sharpe/CEQ levels are not reported in this table; do not invent them."
  }
]
```

## 2026-10-11T01:39:16.261745+00:00 — Review 2RLBINN9 s8: causal scope, outcomes and benchmark evidence

15 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "H139",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H140",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H141",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I139",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I140",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I141",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J139",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J140",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J141",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Settings",
    "cell": "I63",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J63",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K63",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L63",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M63",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O63",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Table 7 pp. 797-798: substantive hedging-rule return attribution. Total hedging increment equals hedged minus unhedged portfolio return; fp and fx are additive components, not separate macro causal treatments. Preserve equity/bond and weighting variants. Comparing incremental effects across rules and component/total shares is not automatically a same-outcome baseline comparison. The 25%-95% higher increment, FX component/total 65%-90%, and twice-momentum FX increment compare effects/components rather than an outcome baseline; not added as benchmark rows."
  }
]
```

## 2026-10-11T01:39:34.776192+00:00 — Review 2RLBINN9 s9: causal scope, outcomes and benchmark evidence

205 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1297",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1298",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1299",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1300",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1301",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1302",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1303",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1304",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1305",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1306",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1307",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1308",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1309",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1310",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1311",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1312",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1297",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1298",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1299",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1300",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1301",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1302",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1303",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1304",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1305",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1306",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1307",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1308",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1309",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1310",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1311",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1312",
    "before": null,
    "after": "s9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1297",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1298",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1299",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1300",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1301",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1302",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1303",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1304",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1305",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1306",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1307",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1308",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1309",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1310",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1311",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1312",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1297",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1298",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1299",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1300",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1301",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1302",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1303",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1304",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1305",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1306",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1307",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1308",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1309",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1310",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1311",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1312",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1297",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1298",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1299",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1300",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1301",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1302",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1303",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1304",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1305",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1306",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1307",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1308",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1309",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1310",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1311",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1312",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1297",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1298",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1299",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1300",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1301",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1302",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1303",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1304",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1305",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1306",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1307",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1308",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1309",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1310",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1311",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1312",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1297",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1298",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1299",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1300",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1301",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1302",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1303",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1304",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1305",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1306",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1307",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1308",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1309",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1310",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1311",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1312",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1297",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1298",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1299",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1300",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1301",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1302",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1303",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1304",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1305",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1306",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1307",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1308",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1309",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1310",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1311",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1312",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1297",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1298",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1299",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1300",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1301",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1302",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1303",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1304",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1305",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1306",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1307",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1308",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1309",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1310",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1311",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1312",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1297",
    "before": null,
    "after": "Table 8 p. 799 Panel A equity, Factor betas only: Sharpe 0.31 versus baseline 0.52; printed DeltaSharpe -0.21."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1298",
    "before": null,
    "after": "Table 8 p. 799 Panel A equity, Factor betas only: CEQ 1.1% versus baseline 4.4%; printed DeltaCEQ -3.3 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1299",
    "before": null,
    "after": "Table 8 p. 799 Panel A equity, Predictable factor returns with constant betas: Sharpe 0.51 versus baseline 0.52; printed DeltaSharpe -0.01."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1300",
    "before": null,
    "after": "Table 8 p. 799 Panel A equity, Predictable factor returns with constant betas: CEQ 4.26% versus baseline 4.4%; printed DeltaCEQ -0.14 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1301",
    "before": null,
    "after": "Table 8 p. 799 Panel A bond, Factor betas only: Sharpe 0.29 versus baseline 0.77; printed DeltaSharpe -0.48."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1302",
    "before": null,
    "after": "Table 8 p. 799 Panel A bond, Factor betas only: CEQ 1.32% versus baseline 4.52%; printed DeltaCEQ -3.2 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1303",
    "before": null,
    "after": "Table 8 p. 799 Panel A bond, Predictable factor returns with constant betas: Sharpe 0.77 versus baseline 0.77; printed DeltaSharpe 0.0."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1304",
    "before": null,
    "after": "Table 8 p. 799 Panel A bond, Predictable factor returns with constant betas: CEQ 4.58% versus baseline 4.52%; printed DeltaCEQ 0.06 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1305",
    "before": null,
    "after": "Table 8 p. 799 Panel B equity, Factor betas only: Sharpe 0.28 versus baseline 0.4; printed DeltaSharpe -0.12."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1306",
    "before": null,
    "after": "Table 8 p. 799 Panel B equity, Factor betas only: CEQ 0.67% versus baseline 2.66%; printed DeltaCEQ -1.99 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1307",
    "before": null,
    "after": "Table 8 p. 799 Panel B equity, Predictable factor returns with constant betas: Sharpe 0.41 versus baseline 0.4; printed DeltaSharpe 0.01."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1308",
    "before": null,
    "after": "Table 8 p. 799 Panel B equity, Predictable factor returns with constant betas: CEQ 2.81% versus baseline 2.66%; printed DeltaCEQ 0.15 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1309",
    "before": null,
    "after": "Table 8 p. 799 Panel B bond, Factor betas only: Sharpe 0.38 versus baseline 0.75; printed DeltaSharpe -0.37."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1310",
    "before": null,
    "after": "Table 8 p. 799 Panel B bond, Factor betas only: CEQ 1.78% versus baseline 3.7%; printed DeltaCEQ -1.92 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1311",
    "before": null,
    "after": "Table 8 p. 799 Panel B bond, Predictable factor returns with constant betas: Sharpe 0.78 versus baseline 0.75; printed DeltaSharpe -0.03."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1312",
    "before": null,
    "after": "Table 8 p. 799 Panel B bond, Predictable factor returns with constant betas: CEQ 3.85% versus baseline 3.7%; printed DeltaCEQ 0.15 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1297",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1298",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1299",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1300",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1301",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1302",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1303",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1304",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1305",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1306",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1307",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1308",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1309",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division. Panel B bond Factor returns delta has a printed negative sign inconsistent with the displayed levels; not silently corrected."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1310",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division. Panel B bond Factor returns delta has a printed negative sign inconsistent with the displayed levels; not silently corrected."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1311",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division. Panel B bond Factor returns delta has a printed negative sign inconsistent with the displayed levels; not silently corrected."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1312",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division. Panel B bond Factor returns delta has a printed negative sign inconsistent with the displayed levels; not silently corrected."
  },
  {
    "sheet": "Outcomes",
    "cell": "H142",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H143",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H144",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H145",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H146",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H147",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I142",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I143",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I144",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I145",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I146",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I147",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J142",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J143",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J144",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J145",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J146",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J147",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K143",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K144",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sharpe ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K145",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K146",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to baseline DCF, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K147",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to baseline DCF, percent per annum, risk aversion 6. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I64",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J64",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K64",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L64",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M64",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O64",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Table 8 pp. 797-799: algorithm ablations, not interventions in the underlying factor realizations. Factor betas column removes factor-return predictability; Factor returns column removes beta time variation. Pairwise baseline contrasts retained with grouped portfolio variants. Table 8B bond Factor returns prints DeltaSharpe -0.03 despite levels 0.78 versus 0.75; source inconsistency preserved and flagged."
  }
]
```

## 2026-10-11T01:39:53.862077+00:00 — Review 2RLBINN9 s10: causal scope, outcomes and benchmark evidence

558 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1313",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1314",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1315",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1316",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1317",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1318",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1319",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1320",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1321",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1322",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1323",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1324",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1325",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1326",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1327",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1328",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1329",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1330",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1331",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1332",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1333",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1334",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1335",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1336",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1337",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1338",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1339",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1340",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1341",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1342",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1343",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1344",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1345",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1346",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1347",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1348",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1349",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1350",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1351",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1352",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1353",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1354",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1355",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1356",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1357",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1358",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1359",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1360",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1361",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1362",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1363",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1364",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1313",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1314",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1315",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1316",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1317",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1318",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1319",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1320",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1321",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1322",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1323",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1324",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1325",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1326",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1327",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1328",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1329",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1330",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1331",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1332",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1333",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1334",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1335",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1336",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1337",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1338",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1339",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1340",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1341",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1342",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1343",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1344",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1345",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1346",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1347",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1348",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1349",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1350",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1351",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1352",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1353",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1354",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1355",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1356",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1357",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1358",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1359",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1360",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1361",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1362",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1363",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1364",
    "before": null,
    "after": "s10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1313",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1314",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1315",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1316",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1317",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1318",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1319",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1320",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1321",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1322",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1323",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1324",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1325",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1326",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1327",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1328",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1329",
    "before": null,
    "after": "hc17"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1330",
    "before": null,
    "after": "hc18"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1331",
    "before": null,
    "after": "hc19"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1332",
    "before": null,
    "after": "hc20"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1333",
    "before": null,
    "after": "hc21"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1334",
    "before": null,
    "after": "hc22"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1335",
    "before": null,
    "after": "hc23"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1336",
    "before": null,
    "after": "hc24"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1337",
    "before": null,
    "after": "hc25"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1338",
    "before": null,
    "after": "hc26"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1339",
    "before": null,
    "after": "hc27"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1340",
    "before": null,
    "after": "hc28"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1341",
    "before": null,
    "after": "hc29"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1342",
    "before": null,
    "after": "hc30"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1343",
    "before": null,
    "after": "hc31"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1344",
    "before": null,
    "after": "hc32"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1345",
    "before": null,
    "after": "hc33"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1346",
    "before": null,
    "after": "hc34"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1347",
    "before": null,
    "after": "hc35"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1348",
    "before": null,
    "after": "hc36"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1349",
    "before": null,
    "after": "hc37"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1350",
    "before": null,
    "after": "hc38"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1351",
    "before": null,
    "after": "hc39"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1352",
    "before": null,
    "after": "hc40"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1353",
    "before": null,
    "after": "hc41"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1354",
    "before": null,
    "after": "hc42"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1355",
    "before": null,
    "after": "hc43"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1356",
    "before": null,
    "after": "hc44"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1357",
    "before": null,
    "after": "hc45"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1358",
    "before": null,
    "after": "hc46"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1359",
    "before": null,
    "after": "hc47"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1360",
    "before": null,
    "after": "hc48"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1361",
    "before": null,
    "after": "hc49"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1362",
    "before": null,
    "after": "hc50"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1363",
    "before": null,
    "after": "hc51"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1364",
    "before": null,
    "after": "hc52"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1313",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1314",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1315",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1316",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1317",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1318",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1319",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1320",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1321",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1322",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1323",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1324",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1325",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1326",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1327",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1328",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1329",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1330",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1331",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1332",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1333",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1334",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1335",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1336",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1337",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1338",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1339",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1340",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1341",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1342",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1343",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1344",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1345",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1346",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1347",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1348",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1349",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1350",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1351",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1352",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1353",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1354",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1355",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1356",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1357",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1358",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1359",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1360",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1361",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1362",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1363",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1364",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1313",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1314",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1315",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1316",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1317",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1318",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1319",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1320",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1321",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1322",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1323",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1324",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1325",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1326",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1327",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1328",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1329",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1330",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1331",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1332",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1333",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1334",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1335",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1336",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1337",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1338",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1339",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1340",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1341",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1342",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1343",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1344",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1345",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1346",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1347",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1348",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1349",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1350",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1351",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1352",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1353",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1354",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1355",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1356",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1357",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1358",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1359",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1360",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1361",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1362",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1363",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1364",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1313",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1314",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1315",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1316",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1317",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1318",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1319",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1320",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1321",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1322",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1323",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1324",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1325",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1326",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1327",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1328",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1329",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1330",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1331",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1332",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1333",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1334",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1335",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1336",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1337",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1338",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1339",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1340",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1341",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1342",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1343",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1344",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1345",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1346",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1347",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1348",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1349",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1350",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1351",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1352",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1353",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1354",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1355",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1356",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1357",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1358",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1359",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1360",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1361",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1362",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1363",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1364",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1313",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1314",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1315",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1316",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1317",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1318",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1319",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1320",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1321",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1322",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1323",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1324",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1325",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1326",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1327",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1328",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1329",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1330",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1331",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1332",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1333",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1334",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1335",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1336",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1337",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1338",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1339",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1340",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1341",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1342",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1343",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1344",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1345",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1346",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1347",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1348",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1349",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1350",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1351",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1352",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1353",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1354",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1355",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1356",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1357",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1358",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1359",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1360",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1361",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1362",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1363",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1364",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1313",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1314",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1315",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1316",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1317",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1318",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1319",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1320",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1321",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1322",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1323",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1324",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1325",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1326",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1327",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1328",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1329",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1330",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1331",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1332",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1333",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1334",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1335",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1336",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1337",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1338",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1339",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1340",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1341",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1342",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1343",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1344",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1345",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1346",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1347",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1348",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1349",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1350",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1351",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1352",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1353",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1354",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1355",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1356",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1357",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1358",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1359",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1360",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1361",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1362",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1363",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1364",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1313",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1314",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1315",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1316",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1317",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1318",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1319",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1320",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1321",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1322",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1323",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1324",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1325",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1326",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1327",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1328",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1329",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1330",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1331",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1332",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1333",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1334",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1335",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1336",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1337",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1338",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1339",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1340",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1341",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1342",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1343",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1344",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1345",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1346",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1347",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1348",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1349",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1350",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1351",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1352",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1353",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1354",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1355",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1356",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1357",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1358",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1359",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1360",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1361",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1362",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1363",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1364",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1313",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Afd: Sharpe 0.4, baseline 0.52, printed DeltaSharpe -0.12."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1314",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Afd: CEQ 2.55%, baseline 4.4%, printed DeltaCEQ -1.85 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1315",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Com: Sharpe 0.48, baseline 0.52, printed DeltaSharpe -0.04. Prose p. 798 describes Com-only Sharpe as over 90% of baseline."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1316",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Com: CEQ 3.87%, baseline 4.4%, printed DeltaCEQ -0.53 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1317",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Vol: Sharpe 0.4, baseline 0.52, printed DeltaSharpe -0.12."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1318",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Vol: CEQ 2.61%, baseline 4.4%, printed DeltaCEQ -1.79 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1319",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Afd+Com: Sharpe 0.53, baseline 0.52, printed DeltaSharpe 0.01."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1320",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Afd+Com: CEQ 4.56%, baseline 4.4%, printed DeltaCEQ 0.16 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1321",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Afd+Vol: Sharpe 0.45, baseline 0.52, printed DeltaSharpe -0.07."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1322",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Afd+Vol: CEQ 3.38%, baseline 4.4%, printed DeltaCEQ -1.02 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1323",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Com+Vol: Sharpe 0.49, baseline 0.52, printed DeltaSharpe -0.03."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1324",
    "before": null,
    "after": "Table 9 p. 800 Panel A equity, Com+Vol: CEQ 3.98%, baseline 4.4%, printed DeltaCEQ -0.42 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1325",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Afd: Sharpe 0.49, baseline 0.77, printed DeltaSharpe -0.28."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1326",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Afd: CEQ 2.71%, baseline 4.52%, printed DeltaCEQ -1.81 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1327",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Com: Sharpe 0.67, baseline 0.77, printed DeltaSharpe -0.1. Prose p. 798 describes Com-only Sharpe as over 90% of baseline."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1328",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Com: CEQ 4.01%, baseline 4.52%, printed DeltaCEQ -0.51 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1329",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Vol: Sharpe 0.45, baseline 0.77, printed DeltaSharpe -0.32."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1330",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Vol: CEQ 2.35%, baseline 4.52%, printed DeltaCEQ -2.17 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1331",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Afd+Com: Sharpe 0.78, baseline 0.77, printed DeltaSharpe 0.01."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1332",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Afd+Com: CEQ 4.56%, baseline 4.52%, printed DeltaCEQ 0.04 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1333",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Afd+Vol: Sharpe 0.6, baseline 0.77, printed DeltaSharpe -0.17."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1334",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Afd+Vol: CEQ 3.3%, baseline 4.52%, printed DeltaCEQ -1.22 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1335",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Com+Vol: Sharpe 0.69, baseline 0.77, printed DeltaSharpe -0.08."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1336",
    "before": null,
    "after": "Table 9 p. 800 Panel A bond, Com+Vol: CEQ 4.1%, baseline 4.52%, printed DeltaCEQ -0.42 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1337",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Afd: Sharpe 0.31, baseline 0.4, printed DeltaSharpe -0.09."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1338",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Afd: CEQ 1.32%, baseline 2.66%, printed DeltaCEQ -1.34 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1339",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Com: Sharpe 0.37, baseline 0.4, printed DeltaSharpe -0.03. Prose p. 798 describes Com-only Sharpe as over 90% of baseline."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1340",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Com: CEQ 2.16%, baseline 2.66%, printed DeltaCEQ 0.5 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1341",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Vol: Sharpe 0.33, baseline 0.4, printed DeltaSharpe -0.07."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1342",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Vol: CEQ 1.54%, baseline 2.66%, printed DeltaCEQ -1.12 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1343",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Afd+Com: Sharpe 0.4, baseline 0.4, printed DeltaSharpe 0.0."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1344",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Afd+Com: CEQ 2.68%, baseline 2.66%, printed DeltaCEQ 0.02 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1345",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Afd+Vol: Sharpe 0.36, baseline 0.4, printed DeltaSharpe -0.04."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1346",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Afd+Vol: CEQ 2.01%, baseline 2.66%, printed DeltaCEQ -0.65 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1347",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Com+Vol: Sharpe 0.37, baseline 0.4, printed DeltaSharpe -0.03."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1348",
    "before": null,
    "after": "Table 9 p. 800 Panel B equity, Com+Vol: CEQ 2.21%, baseline 2.66%, printed DeltaCEQ -0.45 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1349",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Afd: Sharpe 0.51, baseline 0.75, printed DeltaSharpe -0.24."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1350",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Afd: CEQ 2.42%, baseline 3.7%, printed DeltaCEQ -1.28 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1351",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Com: Sharpe 0.68, baseline 0.75, printed DeltaSharpe -0.07. Prose p. 798 describes Com-only Sharpe as over 90% of baseline."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1352",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Com: CEQ 3.41%, baseline 3.7%, printed DeltaCEQ -0.29 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1353",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Vol: Sharpe 0.47, baseline 0.75, printed DeltaSharpe -0.28."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1354",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Vol: CEQ 2.13%, baseline 3.7%, printed DeltaCEQ -1.57 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1355",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Afd+Com: Sharpe 0.81, baseline 0.75, printed DeltaSharpe 0.06."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1356",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Afd+Com: CEQ 3.96%, baseline 3.7%, printed DeltaCEQ 0.26 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1357",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Afd+Vol: Sharpe 0.6, baseline 0.75, printed DeltaSharpe -0.15."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1358",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Afd+Vol: CEQ 2.81%, baseline 3.7%, printed DeltaCEQ -0.89 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1359",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Com+Vol: Sharpe 0.65, baseline 0.75, printed DeltaSharpe -0.1."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1360",
    "before": null,
    "after": "Table 9 p. 800 Panel B bond, Com+Vol: CEQ 3.26%, baseline 3.7%, printed DeltaCEQ -0.44 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1361",
    "before": null,
    "after": "pp. 798,800 Table 9 Panel A equity: Com-only annualized mean return 7.4% versus full DCF 7.93%; prose says over 90% of benchmark."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1362",
    "before": null,
    "after": "pp. 798,800 Table 9 Panel A bond: Com-only annualized mean return 4.75% versus full DCF 5.21%; prose says over 90% of benchmark."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1363",
    "before": null,
    "after": "pp. 798,800 Table 9 Panel B equity: Com-only annualized mean return 5.6% versus full DCF 6.16%; prose says over 90% of benchmark."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1364",
    "before": null,
    "after": "pp. 798,800 Table 9 Panel B bond: Com-only annualized mean return 3.9% versus full DCF 4.16%; prose says over 90% of benchmark."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1315",
    "before": null,
    "after": "Prose over-90% wording is not accurate for every displayed Sharpe ratio; preserve author claim without repairing it."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1327",
    "before": null,
    "after": "Prose over-90% wording is not accurate for every displayed Sharpe ratio; preserve author claim without repairing it."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1339",
    "before": null,
    "after": "Prose over-90% wording is not accurate for every displayed Sharpe ratio; preserve author claim without repairing it."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1340",
    "before": null,
    "after": "Panel B equity Com prints +0.50 despite 2.16 versus 2.66. Literal source transcription, not a corrected sign."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1351",
    "before": null,
    "after": "Prose over-90% wording is not accurate for every displayed Sharpe ratio; preserve author claim without repairing it."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1361",
    "before": null,
    "after": "Same portfolio/weighting, OOS months and price paths under full versus restricted rule, within maintained backtest."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1362",
    "before": null,
    "after": "Same portfolio/weighting, OOS months and price paths under full versus restricted rule, within maintained backtest."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1363",
    "before": null,
    "after": "Same portfolio/weighting, OOS months and price paths under full versus restricted rule, within maintained backtest."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1364",
    "before": null,
    "after": "Same portfolio/weighting, OOS months and price paths under full versus restricted rule, within maintained backtest."
  },
  {
    "sheet": "Outcomes",
    "cell": "H148",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H149",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H150",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H151",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H152",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H153",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I148",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I149",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I150",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I151",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I152",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I153",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J148",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J149",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J150",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J151",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J152",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J153",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K149",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K150",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sharpe ratio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K151",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K152",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to baseline DCF, percent per annum, risk aversion 2. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K153",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Performance fee to switch to baseline DCF, percent per annum, risk aversion 6. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Settings",
    "cell": "I65",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J65",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K65",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L65",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M65",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O65",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Table 9 pp. 798-800: restricted forecasting input sets compared with full DCF. These are effects of algorithm inputs on simulated portfolio performance, not causal effects of commodity prices on currency returns. Table 9B equity Com prints DeltaCEQ +0.50 despite levels 2.16 versus 2.66; preserve source inconsistency. The prose over-90% claim is also too broad for every displayed Sharpe ratio."
  }
]
```

## 2026-10-11T01:40:12.250976+00:00 — Review 2RLBINN9 s11: causal scope, outcomes and benchmark evidence

51 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1365",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1366",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1365",
    "before": null,
    "after": "s11"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1366",
    "before": null,
    "after": "s11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1365",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1366",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1365",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1366",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1365",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1366",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1365",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1366",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1365",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1366",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1365",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1366",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1365",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1366",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1365",
    "before": null,
    "after": "p. 800: signal rule improves JPY/CHF returns by around 3%-4% relative to buy-and-hold in Table 1. JPY: Table 10A DCF mean 1.34% (1997-2017); Table 1 currency excess return mean -1.79% (1987-2017)."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1366",
    "before": null,
    "after": "p. 800: signal rule improves JPY/CHF returns by around 3%-4% relative to buy-and-hold in Table 1. CHF: Table 10A DCF mean 3.66% (1997-2017); Table 1 currency excess return mean -0.34% (1987-2017)."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1365",
    "before": null,
    "after": "Known sample-period mismatch. The 3%-4% language is an approximate percentage-point improvement, not division by the benchmark."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1366",
    "before": null,
    "after": "Known sample-period mismatch. The 3%-4% language is an approximate percentage-point improvement, not division by the benchmark."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4267",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4267",
    "before": null,
    "after": "s11"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4267",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H154",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H155",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H156",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H157",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4267",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I154",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I155",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I156",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I157",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4267",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J154",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J155",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J156",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J157",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4267",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K155",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K156",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sharpe ratio of the currency strategy. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K157",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Skewness of the currency strategy return distribution. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4267",
    "before": null,
    "after": "Figure 3 p. 802: cumulative dollar payoff to $1 invested in Jan 1997, compound strategy returns through July 2017. No numerical terminal values invented from graph."
  },
  {
    "sheet": "Settings",
    "cell": "I66",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J66",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K66",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L66",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M66",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N66",
    "before": null,
    "after": "Section 7, Table 10A and Figure 3, pp. 799-802: performance of a DCF signal-based currency rule relative to buy-and-hold and other currency rules. Monthly positive/negative expected return determines long/short positions; this signal is not randomly assigned. Pairwise policy adoption is binary. Group bilateral currency and aggregate variants; include separately reported cumulative-wealth outcome from Figure 3."
  },
  {
    "sheet": "Settings",
    "cell": "O66",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. The p. 800 JPY/CHF buy-and-hold comparison points to Table 1 (1987-2017), whereas DCF results cover 1997-2017: retain the explicit comparison but mark horizon mismatch. Strategy comparisons are accepted as the authors policy-counterfactual interpretation, not design-based causal identification."
  }
]
```

## 2026-10-11T01:40:30.680506+00:00 — Review 2RLBINN9 s12: causal scope, outcomes and benchmark evidence

242 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1367",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1368",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1369",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1370",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1371",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1372",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1373",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1374",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1375",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1376",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1377",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1378",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1379",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1380",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1381",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1382",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1383",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1384",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1367",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1368",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1369",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1370",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1371",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1372",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1373",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1374",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1375",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1376",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1377",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1378",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1379",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1380",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1381",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1382",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1383",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1384",
    "before": null,
    "after": "s12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1367",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1368",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1369",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1370",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1371",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1372",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1373",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1374",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1375",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1376",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1377",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1378",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1379",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1380",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1381",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1382",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1383",
    "before": null,
    "after": "hc17"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1384",
    "before": null,
    "after": "hc18"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1367",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1368",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1369",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1370",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1371",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1372",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1373",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1374",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1375",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1376",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1377",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1378",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1379",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1380",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1381",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1382",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1383",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1384",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K25",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K26",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1367",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1368",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1369",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1370",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1371",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1372",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1373",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1374",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1375",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1376",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1377",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1378",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1379",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1380",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1381",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1382",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1383",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1384",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L25",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L26",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1367",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1368",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1369",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1370",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1371",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1372",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1373",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1374",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1375",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1376",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1377",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1378",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1379",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1380",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1381",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1382",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1383",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1384",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M25",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M26",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1367",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1368",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1369",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1370",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1371",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1372",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1373",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1374",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1375",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1376",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1377",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1378",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1379",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1380",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1381",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1382",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1383",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1384",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N25",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N26",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1367",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1368",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1369",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1370",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1371",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1372",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1373",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1374",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1375",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1376",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1377",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1378",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1379",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1380",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1381",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1382",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1383",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1384",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O25",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O26",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1367",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1368",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1369",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1370",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1371",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1372",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1373",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1374",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1375",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1376",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1377",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1378",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1379",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1380",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1381",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1382",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1383",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1384",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P25",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P26",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1367",
    "before": null,
    "after": "Table 10B p. 801 equity, add Carry: Sharpe 0.41 versus fully hedged baseline 0.37; printed DeltaSharpe 0.04."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1368",
    "before": null,
    "after": "Table 10B p. 801 equity, add Carry: CEQ 2.46% versus fully hedged baseline 2.19%; printed DeltaCEQ 0.07 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1369",
    "before": null,
    "after": "Table 10B p. 801 equity, add Momentum: Sharpe 0.32 versus fully hedged baseline 0.37; printed DeltaSharpe -0.05."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1370",
    "before": null,
    "after": "Table 10B p. 801 equity, add Momentum: CEQ 1.38% versus fully hedged baseline 2.19%; printed DeltaCEQ -0.78 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1371",
    "before": null,
    "after": "Table 10B p. 801 equity, add Value: Sharpe 0.53 versus fully hedged baseline 0.37; printed DeltaSharpe 0.16."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1372",
    "before": null,
    "after": "Table 10B p. 801 equity, add Value: CEQ 4.54% versus fully hedged baseline 2.19%; printed DeltaCEQ 2.54 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1373",
    "before": null,
    "after": "Table 10B p. 801 equity, add Style combination: Sharpe 0.46 versus fully hedged baseline 0.37; printed DeltaSharpe 0.09. Prose calls style-equity improvement over 40%."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1374",
    "before": null,
    "after": "Table 10B p. 801 equity, add Style combination: CEQ 3.5% versus fully hedged baseline 2.19%; printed DeltaCEQ 1.31 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1375",
    "before": null,
    "after": "Table 10B p. 801 equity, add DCF time series: CEQ 7.3% versus fully hedged baseline 2.19%; printed DeltaCEQ 5.11 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1376",
    "before": null,
    "after": "Table 10B p. 801 bond, add Carry: Sharpe 0.61 versus fully hedged baseline 0.54; printed DeltaSharpe 0.07."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1377",
    "before": null,
    "after": "Table 10B p. 801 bond, add Carry: CEQ 4.16% versus fully hedged baseline 2.19%; printed DeltaCEQ 1.89 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1378",
    "before": null,
    "after": "Table 10B p. 801 bond, add Momentum: Sharpe 0.25 versus fully hedged baseline 0.54; printed DeltaSharpe -0.29."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1379",
    "before": null,
    "after": "Table 10B p. 801 bond, add Momentum: CEQ 1.02% versus fully hedged baseline 2.19%; printed DeltaCEQ -1.2 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1380",
    "before": null,
    "after": "Table 10B p. 801 bond, add Value: Sharpe 0.6 versus fully hedged baseline 0.54; printed DeltaSharpe 0.06."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1381",
    "before": null,
    "after": "Table 10B p. 801 bond, add Value: CEQ 4.1% versus fully hedged baseline 2.19%; printed DeltaCEQ 1.91 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1382",
    "before": null,
    "after": "Table 10B p. 801 bond, add Style combination: Sharpe 0.78 versus fully hedged baseline 0.54; printed DeltaSharpe 0.24."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1383",
    "before": null,
    "after": "Table 10B p. 801 bond, add Style combination: CEQ 3.79% versus fully hedged baseline 2.19%; printed DeltaCEQ 1.57 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1384",
    "before": null,
    "after": "Table 10B p. 801 bond, add DCF time series: CEQ 7.19% versus fully hedged baseline 2.19%; printed DeltaCEQ 5.0 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q25",
    "before": null,
    "after": "“The addition of the portfolio almost doubles the equity portfolio Sharpe ratio…” [ … ] Table 10 Panel B: global equity portfolios, “Sharpe 0.37” for “Full hedge” and “0.70” for “DCF time series”. Location: p. 801 Table 10B. Same portfolio/weighting and Jan 1997-Jul 2017 path."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q26",
    "before": null,
    "after": "“Equivalent results are found for the global bond portfolio: the inclusion of the DCFTS portfolio increases the Sharpe ratio by 80%...” [ … ] Table 10 Panel B: global bond portfolios, “Sharpe 0.54” for “Full hedge” and “0.97” for “DCF time series”. Location: p. 801 Table 10B. Same portfolio/weighting and Jan 1997-Jul 2017 path."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1368",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1370",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1372",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1373",
    "before": null,
    "after": "Style-equity 0.46 versus 0.37 does not support the printed over-40% claim; source inconsistency flagged, not repaired."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1374",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1375",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1377",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1379",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1381",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1383",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1384",
    "before": null,
    "after": "Some printed DeltaCEQ values disagree with displayed levels beyond rounding. Preserve literal table values; do not substitute newly calculated differences."
  },
  {
    "sheet": "Outcomes",
    "cell": "H158",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H159",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H160",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H161",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H162",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H163",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H164",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H165",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I158",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I159",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I160",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I161",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I162",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I163",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I164",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I165",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J158",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J159",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J160",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J161",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J162",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J163",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J164",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J165",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K159",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Annualized standard deviation, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K160",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Sharpe ratio of the combined portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K161",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Skewness of combined portfolio returns. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K162",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Information ratio relative to the fully hedged portfolio. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K163",
    "before": null,
    "after": "Reported portfolio-performance functional (dispersion, risk-adjusted ratio, drawdown or utility-based statistic), not a log or raw return. Certainty-equivalent return of the combined portfolio, percent. Zero probability mass is not established by rounded point estimates."
  },
  {
    "sheet": "Outcomes",
    "cell": "K164",
    "before": null,
    "after": "Table 10B: annualized performance fee to switch FROM the combined portfolio TO the fully hedged portfolio, relative risk aversion 2. Reported DCF fees negative: -5.63% equity/-5.61% bond. Prose states positive willingness to switch in the opposite direction; do not reverse printed table signs."
  },
  {
    "sheet": "Outcomes",
    "cell": "K165",
    "before": null,
    "after": "Table 10B: annualized performance fee to switch FROM the combined portfolio TO the fully hedged portfolio, relative risk aversion 6. Reported DCF fees negative: -5.59% equity/-5.56% bond. Prose states positive willingness to switch in the opposite direction; do not reverse printed table signs."
  },
  {
    "sheet": "Settings",
    "cell": "I67",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J67",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K67",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L67",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M67",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "O67",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Table 10B p. 801: adding currency portfolios to fixed fully hedged equity/bond holdings. Correct fee direction: table reports fees to switch BACK to the fully hedged portfolio; DCF values are negative (-5.63/-5.59 equity and -5.61/-5.56 bond). Prose describes positive willingness to adopt the combined portfolio. Preserve printed delta values rather than silently repairing several mismatches with displayed levels. The style-equity over-40% prose claim conflicts with displayed Sharpe levels 0.46/0.37. Fee versus fee wording (over three times) is an effect-versus-effect comparison, not a separate outcome-level benchmark."
  }
]
```

## 2026-10-11T01:40:48.254212+00:00 — Review 2RLBINN9 h1: causal scope, outcomes and benchmark evidence

139 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1385",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1386",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1387",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1388",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1389",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1390",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1391",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1392",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1385",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1386",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1387",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1388",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1389",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1390",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1391",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1392",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1385",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1386",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1387",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1388",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1389",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1390",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1391",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1392",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1385",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1386",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1387",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1388",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1389",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1390",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1391",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1392",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1385",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1386",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1387",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1388",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1389",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1390",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1391",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1392",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1385",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1386",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1387",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1388",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1389",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1390",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1391",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1392",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1385",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1386",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1387",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1388",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1389",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1390",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1391",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1392",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1385",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1386",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1387",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1388",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1389",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1390",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1391",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1392",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1385",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1386",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1387",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1388",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1389",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1390",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1391",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1392",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1385",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Actual future returns: Sharpe 1.25 versus baseline 0.52; printed DeltaSharpe 0.73."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1386",
    "before": null,
    "after": "Table 5 p. 795 Panel A equity, Actual future returns: CEQ 15.52% versus baseline 4.4%; printed DeltaCEQ 11.12 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1387",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Actual future returns: Sharpe 2.52 versus baseline 0.77; printed DeltaSharpe 1.75."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1388",
    "before": null,
    "after": "Table 5 p. 795 Panel A bond, Actual future returns: CEQ 15.84% versus baseline 4.52%; printed DeltaCEQ 11.32 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1389",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Actual future returns: Sharpe 1.14 versus baseline 0.4; printed DeltaSharpe 0.74."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1390",
    "before": null,
    "after": "Table 5 p. 795 Panel B equity, Actual future returns: CEQ 13.76% versus baseline 2.66%; printed DeltaCEQ 11.1 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1391",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Actual future returns: Sharpe 2.56 versus baseline 0.75; printed DeltaSharpe 1.81."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1392",
    "before": null,
    "after": "Table 5 p. 795 Panel B bond, Actual future returns: CEQ 14.9% versus baseline 3.7%; printed DeltaCEQ 11.2 percentage points."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1385",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1386",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1387",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1388",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1389",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1390",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1391",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1392",
    "before": null,
    "after": "Same portfolio, weights and Jan 1997-Jul 2017 price path. Deliberately paired contrast and reference level; no author division."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4268",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4269",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4270",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4271",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4272",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4273",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4268",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4269",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4270",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4271",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4272",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4273",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4268",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4269",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4270",
    "before": null,
    "after": "hy3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4271",
    "before": null,
    "after": "hy4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4272",
    "before": null,
    "after": "hy5"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4273",
    "before": null,
    "after": "hy6"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4268",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4269",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4270",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4271",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4272",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4273",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4268",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4269",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4270",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4271",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4272",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4273",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4268",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4269",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4270",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4271",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4272",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4273",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4268",
    "before": null,
    "after": "Annualized portfolio mean return, percent."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4269",
    "before": null,
    "after": "Annualized portfolio return SD, percent."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4270",
    "before": null,
    "after": "Portfolio Sharpe ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4271",
    "before": null,
    "after": "CEQ return at gamma=3, percent."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4272",
    "before": null,
    "after": "Fee to switch to historical baseline DCF, relative risk aversion 2, percent per year."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4273",
    "before": null,
    "after": "Fee to switch to historical baseline DCF, relative risk aversion 6, percent per year."
  },
  {
    "sheet": "Settings",
    "cell": "A1776",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1776",
    "before": null,
    "after": "h1"
  },
  {
    "sheet": "Settings",
    "cell": "I1776",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1776",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1776",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1776",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1776",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1776",
    "before": null,
    "after": "Table 5 Actual rets columns, p. 795, Section 6.1 p. 796: replace expected currency returns with actual next-month returns, keeping the baseline covariance framework. Compare with historical baseline DCF for equity/bond and equal/GDP weights. Infeasible perfect-information counterfactual isolates potential gains from better return forecasts; not achievable OOS performance."
  },
  {
    "sheet": "Settings",
    "cell": "O1776",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. "
  }
]
```

## 2026-10-11T01:41:04.937845+00:00 — Review 2RLBINN9 h2: causal scope, outcomes and benchmark evidence

23 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4274",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4275",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4274",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4275",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4274",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4275",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4274",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4275",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4274",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4275",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4274",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4275",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4274",
    "before": null,
    "after": "Portfolio Sharpe ratio under alternative evaluation periods."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4275",
    "before": null,
    "after": "Portfolio CEQ return under alternative evaluation periods."
  },
  {
    "sheet": "Settings",
    "cell": "A1777",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1777",
    "before": null,
    "after": "h2"
  },
  {
    "sheet": "Settings",
    "cell": "I1777",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1777",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1777",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1777",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1777",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1777",
    "before": null,
    "after": "Section 8.1 p. 802 (references Table A.2): DCF adoption under alternative OOS starts Jan 1992 and Jan 2002; same Jul 2017 endpoint. Results qualitatively unchanged; Sharpe/CEQ often slightly higher. Group date variants."
  },
  {
    "sheet": "Settings",
    "cell": "O1777",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Retain substantive result explicitly reported in MAIN TEXT. Separate online appendix table not inspected; no unavailable coefficients, exact comparison levels or detailed table outcomes invented. No qualifying numerical same-outcome benchmark beyond the narrated contrast identified in main text."
  }
]
```

## 2026-10-11T01:41:21.338384+00:00 — Review 2RLBINN9 h3: causal scope, outcomes and benchmark evidence

23 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4276",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4277",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4276",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4277",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4276",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4277",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4276",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4277",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4276",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4277",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4276",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4277",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4276",
    "before": null,
    "after": "Portfolio Sharpe ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4277",
    "before": null,
    "after": "Portfolio CEQ return."
  },
  {
    "sheet": "Settings",
    "cell": "A1778",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1778",
    "before": null,
    "after": "h3"
  },
  {
    "sheet": "Settings",
    "cell": "I1778",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1778",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1778",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1778",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1778",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1778",
    "before": null,
    "after": "Section 8.2 p. 802 (Table A.3): change initial factor-return training start from 1987 to 1989 or 1992. Baseline has highest Sharpe/CEQ but differences insignificant; routine window variants grouped."
  },
  {
    "sheet": "Settings",
    "cell": "O1778",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Retain substantive result explicitly reported in MAIN TEXT. Separate online appendix table not inspected; no unavailable coefficients, exact comparison levels or detailed table outcomes invented. No qualifying numerical same-outcome benchmark beyond the narrated contrast identified in main text."
  }
]
```

## 2026-10-11T01:41:37.872656+00:00 — Review 2RLBINN9 h4: causal scope, outcomes and benchmark evidence

23 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4278",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4279",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4278",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4279",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4278",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4279",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4278",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4279",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4278",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4279",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4278",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4279",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4278",
    "before": null,
    "after": "Portfolio Sharpe ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4279",
    "before": null,
    "after": "Portfolio CEQ return."
  },
  {
    "sheet": "Settings",
    "cell": "A1779",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1779",
    "before": null,
    "after": "h4"
  },
  {
    "sheet": "Settings",
    "cell": "I1779",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1779",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1779",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1779",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1779",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1779",
    "before": null,
    "after": "Section 8.3 p. 802 (Table A.4): replace 60-month factor-beta rolling window with 84 or 120 months; Sharpe ratios within 0.02 of baseline. Group windows and portfolio variants."
  },
  {
    "sheet": "Settings",
    "cell": "O1779",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Retain substantive result explicitly reported in MAIN TEXT. Separate online appendix table not inspected; no unavailable coefficients, exact comparison levels or detailed table outcomes invented. No qualifying numerical same-outcome benchmark beyond the narrated contrast identified in main text."
  }
]
```

## 2026-10-11T01:41:54.585826+00:00 — Review 2RLBINN9 h5: causal scope, outcomes and benchmark evidence

23 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4280",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4281",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4280",
    "before": null,
    "after": "h5"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4281",
    "before": null,
    "after": "h5"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4280",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4281",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4280",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4281",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4280",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4281",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4280",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4281",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4280",
    "before": null,
    "after": "Portfolio Sharpe ratio."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4281",
    "before": null,
    "after": "Portfolio CEQ return."
  },
  {
    "sheet": "Settings",
    "cell": "A1780",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1780",
    "before": null,
    "after": "h5"
  },
  {
    "sheet": "Settings",
    "cell": "I1780",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1780",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1780",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1780",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1780",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1780",
    "before": null,
    "after": "Section 8.4 p. 802 (Table A.5): replace expanding factor-return estimation with 60/120-month rolling windows; small deterioration, generally statistically indistinguishable except 120-month equal-weight equity case."
  },
  {
    "sheet": "Settings",
    "cell": "O1780",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Retain substantive result explicitly reported in MAIN TEXT. Separate online appendix table not inspected; no unavailable coefficients, exact comparison levels or detailed table outcomes invented. No qualifying numerical same-outcome benchmark beyond the narrated contrast identified in main text."
  }
]
```

## 2026-10-11T01:42:11.573567+00:00 — Review 2RLBINN9 h6: causal scope, outcomes and benchmark evidence

23 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4282",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4283",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4282",
    "before": null,
    "after": "h6"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4283",
    "before": null,
    "after": "h6"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4282",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4283",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4282",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4283",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4282",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4283",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4282",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4283",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4282",
    "before": null,
    "after": "Portfolio Sharpe ratio; reported contrasts relative to alternative rules."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4283",
    "before": null,
    "after": "Portfolio CEQ return; reported contrasts relative to alternative rules."
  },
  {
    "sheet": "Settings",
    "cell": "A1781",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1781",
    "before": null,
    "after": "h6"
  },
  {
    "sheet": "Settings",
    "cell": "I1781",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1781",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1781",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1781",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1781",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1781",
    "before": null,
    "after": "Section 8.5 pp. 802-803 (Table A.6): DCF-versus-alternative hedging-rule performance after excluding all crises or separately Asian crisis Jul 1997-Dec 1998, GFC Jul 2007-Mar 2009, European debt crisis May 2010-Dec 2012. Group sample exclusions; NOT a causal effect of crises."
  },
  {
    "sheet": "Settings",
    "cell": "O1781",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Retain substantive result explicitly reported in MAIN TEXT. Separate online appendix table not inspected; no unavailable coefficients, exact comparison levels or detailed table outcomes invented. No qualifying numerical same-outcome benchmark beyond the narrated contrast identified in main text."
  }
]
```

## 2026-10-11T01:42:28.284191+00:00 — Review 2RLBINN9 h7: causal scope, outcomes and benchmark evidence

16 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Outcomes",
    "cell": "A4284",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4284",
    "before": null,
    "after": "h7"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4284",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4284",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4284",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4284",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4284",
    "before": null,
    "after": "Incremental annual hedging return, percent per annum; change about -20 basis points under doubled spreads."
  },
  {
    "sheet": "Settings",
    "cell": "A1782",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1782",
    "before": null,
    "after": "h7"
  },
  {
    "sheet": "Settings",
    "cell": "I1782",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1782",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1782",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1782",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1782",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1782",
    "before": null,
    "after": "Section 8.6 p. 803 (Table A.7): double bid-ask spreads in the backtest versus baseline costs. DCF incremental annual returns decline about 20 basis points for equity and bond portfolios; relative performance remains similar. This is a transaction-cost parameter counterfactual, not a forecast of endogenous market impact."
  },
  {
    "sheet": "Settings",
    "cell": "O1782",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Retain substantive result explicitly reported in MAIN TEXT. Separate online appendix table not inspected; no unavailable coefficients, exact comparison levels or detailed table outcomes invented. No qualifying numerical same-outcome benchmark beyond the narrated contrast identified in main text."
  }
]
```

## 2026-10-11T01:42:45.020606+00:00 — Review 2RLBINN9 h8: causal scope, outcomes and benchmark evidence

43 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1393",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1394",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1393",
    "before": null,
    "after": "h8"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1394",
    "before": null,
    "after": "h8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1393",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1394",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1393",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1394",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1393",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1394",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1393",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1394",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1393",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1394",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1393",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1394",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1393",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1394",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1393",
    "before": null,
    "after": "p. 782 Figure 2 discussion: equity terminal wealth over $5 under DCF versus $2 unhedged, from $1 invested Jan 1997 through Jul 2017."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1394",
    "before": null,
    "after": "p. 782 Figure 2 discussion: bond terminal wealth almost $4 under DCF versus $1.5 unhedged, same starting investment and horizon."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4285",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "A4286",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4285",
    "before": null,
    "after": "h8"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4286",
    "before": null,
    "after": "h8"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4285",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4286",
    "before": null,
    "after": "hy2"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4285",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4286",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4285",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4286",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4285",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4286",
    "before": null,
    "after": "other"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4285",
    "before": null,
    "after": "Cumulative wealth from $1 in equity portfolio, USD; compounded returns."
  },
  {
    "sheet": "Outcomes",
    "cell": "K4286",
    "before": null,
    "after": "Cumulative wealth from $1 in bond portfolio, USD; compounded returns."
  },
  {
    "sheet": "Settings",
    "cell": "A1783",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1783",
    "before": null,
    "after": "h8"
  },
  {
    "sheet": "Settings",
    "cell": "I1783",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1783",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1783",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1783",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M1783",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1783",
    "before": null,
    "after": "Figure 2 and introduction p. 782: cumulative-wealth effect of adopting DCF hedging instead of no hedge, separately for equal-weighted global equities and bonds on identical historical paths. $1 in Jan 1997 grows by Jul 2017 to over $5 versus $2 in equities and almost $4 versus $1.5 in bonds."
  },
  {
    "sheet": "Settings",
    "cell": "O1783",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. "
  }
]
```

## 2026-10-11T01:43:01.221473+00:00 — Review 2RLBINN9 h9: causal scope, outcomes and benchmark evidence

38 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1395",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1396",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1395",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1396",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1395",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1396",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1395",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1396",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1395",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1396",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1395",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1396",
    "before": null,
    "after": "other_level"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1395",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1396",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1395",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1396",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1395",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1396",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1395",
    "before": null,
    "after": "Section 8.6 p. 803: DCF median turnover about 20%-25% versus momentum over 25%; turnover is the same outcome under two rules."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1396",
    "before": null,
    "after": "Section 8.6 p. 803: DCF median turnover about 20%-25% versus stated range 0%-10% for other strategies. Individual median values not given; retain reported range, not invented separate numerical medians."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1396",
    "before": null,
    "after": "Grouped benchmark is the explicitly stated range, not a pooled mean or exact strategy-specific median."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4287",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4287",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4287",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4287",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4287",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4287",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4287",
    "before": null,
    "after": "Monthly currency-hedge turnover distribution/median, fraction of hedge position changed; percent."
  },
  {
    "sheet": "Papers",
    "cell": "E11",
    "before": null,
    "after": "DONE — Main-article review: predictive Table 2 s1 excluded; s2-s12 retained as explicit portfolio-rule counterfactuals (Other), not macroeconomic causal estimates. Corrected fee direction and outcome transformations; checked all original and omitted comparisons, including table contrast/level pairings. Added expected-return oracle split, main-text Sections 8.1-8.6 robustness, Figure 2 terminal wealth and turnover channel. Source numerical/sign inconsistencies preserved and flagged. Original fields unchanged. Main article Tables 1-10/Figures 1-3 and footnotes reviewed; separate Internet Appendix not inspected, and no unreported table coefficients invented."
  },
  {
    "sheet": "Settings",
    "cell": "A1784",
    "before": null,
    "after": "2RLBINN9"
  },
  {
    "sheet": "Settings",
    "cell": "B1784",
    "before": null,
    "after": "h9"
  },
  {
    "sheet": "Settings",
    "cell": "I1784",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J1784",
    "before": null,
    "after": "Other"
  },
  {
    "sheet": "Settings",
    "cell": "K1784",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L1784",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M1784",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N1784",
    "before": null,
    "after": "Section 8.6 p. 803 (Figure A.2): effects of hedging rule on currency hedge turnover, a substantive implementation-cost channel. DCF monthly median turnover about 20%-25%, momentum over 25%, other rules 0%-10%; full hedge and no hedge both zero turnover by construction. Group strategy contrasts; no external price-impact inference."
  },
  {
    "sheet": "Settings",
    "cell": "O1784",
    "before": null,
    "after": "Implemented pairwise strategy-rule contrasts on common historical price paths, not a causal effect of macro predictors on market prices. Other = forecast-driven constrained mean-variance portfolio recomputation/backtest. Binary refers to adoption of one specified rule versus its comparator, not to the continuously varying monthly hedge ratio. OOS Jan 1997-Jul 2017 unless noted; transaction-cost and price-taking assumptions limit external interpretation. Qualifies as rule-induced implementation outcome, not merely input balance. Main-text summary only; exact appendix quantiles not invented."
  }
]
```

## 2026-10-11T02:00:04.027499+00:00 — Review 3DI8S52Q s1: causal scope, outcomes and benchmark evidence

2 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I77",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "O77",
    "before": null,
    "after": "Table II p.388 characterizes correlations/trading styles. Authors explicitly say the strong correlation does not indicate who initiates trades, and then introduce Table III to infer liquidity direction. Table II alone is descriptive, not an implemented effect of returns on trading. Exclude under causal-interpretation gate; do not promote an input description into a separate causal setting."
  }
]
```

## 2026-10-11T02:00:22.205884+00:00 — Review 3DI8S52Q s2: causal scope, outcomes and benchmark evidence

7 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I78",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J78",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K78",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L78",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M78",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N78",
    "before": null,
    "after": "Table III A-B pp.389-390, equation (5): Fama-MacBeth OLS return impact of continuous weekly net position change Q; weeks t+1 and t+2. Group trader-category estimates and routine control variants of the same net-trading treatment."
  },
  {
    "sheet": "Settings",
    "cell": "O78",
    "before": null,
    "after": "Retained for the authors explicit price-pressure/liquidity causal interpretation, not as design-based proof. Observational position/return covariation can reflect omitted fundamentals and simultaneous trading. Authors infer temporary price pressure and compensation for supplying liquidity, explicitly pp.389,394. No identifying FE, matching or instrument. The sign reverses across sides of the same market. No qualifying outcome benchmark found."
  }
]
```

## 2026-10-11T02:00:39.903236+00:00 — Review 3DI8S52Q s3: causal scope, outcomes and benchmark evidence

7 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I79",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J79",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K79",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L79",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M79",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N79",
    "before": null,
    "after": "Table IV A-B pp.391-392: Fama-MacBeth OLS impact of continuous net position change Q using finer DCOT categories, June 2007-December 2017. Group trader-category estimates and two horizons."
  },
  {
    "sheet": "Settings",
    "cell": "O79",
    "before": null,
    "after": "Retained for the authors explicit price-pressure/liquidity causal interpretation, not as design-based proof. Observational position/return covariation can reflect omitted fundamentals and simultaneous trading. DCOT publication starts June 2006, but TABLE estimation sample starts June 2007. Producer 8.14/4.93 and money-manager -6.19/-4.89 slopes are multiplied by 100. Finer disaggregation supports a central identity-of-liquidity-provider conclusion."
  }
]
```

## 2026-10-11T02:00:58.196304+00:00 — Review 3DI8S52Q s4: causal scope, outcomes and benchmark evidence

150 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1397",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1398",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1399",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1400",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1401",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1402",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1403",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1404",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1405",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1406",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1397",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1398",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1399",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1400",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1401",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1402",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1403",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1404",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1405",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1406",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1397",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1398",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1399",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1400",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1401",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1402",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1403",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1404",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1405",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1406",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1397",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1398",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1399",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1400",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1401",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1402",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1403",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1404",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1405",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1406",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K30",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1397",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1398",
    "before": null,
    "after": "y2"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1399",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1400",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1401",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1402",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1403",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1404",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1405",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1406",
    "before": null,
    "after": "y6"
  },
  {
    "sheet": "Comparisons",
    "cell": "L30",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1397",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1398",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1399",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1400",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1401",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1402",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1403",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1404",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1405",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1406",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M30",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1397",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1398",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1399",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1400",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1401",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1402",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1403",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1404",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1405",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1406",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N30",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1397",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1398",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1399",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1400",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1401",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1402",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1403",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1404",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1405",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1406",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O30",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1397",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1398",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1399",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1400",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1401",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1402",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1403",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1404",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1405",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1406",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P30",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1397",
    "before": null,
    "after": "Table V A p.393 days 1-4: top-minus-bottom 0.24 percentage points; bottom-quintile mean -0.05%, same horizon."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1398",
    "before": null,
    "after": "Table V A p.393 days 5-10: top-minus-bottom 0.29 percentage points; bottom-quintile mean -0.09%, same horizon."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1399",
    "before": null,
    "after": "Table V A p.393 days 11-20: top-minus-bottom 0.19 percentage points; bottom-quintile mean 0.08%, same horizon."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1400",
    "before": null,
    "after": "Table V A p.393 days 21-40: top-minus-bottom -0.1 percentage points; bottom-quintile mean 0.44%, same horizon."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1401",
    "before": null,
    "after": "Table V A p.393 days 1-40: top-minus-bottom 0.64 percentage points; bottom-quintile mean 0.37%, same horizon."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1402",
    "before": null,
    "after": "Table V B p.393 week 1: top-minus-bottom position change 2.95 percentage points of ranking-day open interest; bottom group mean -1.55%."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1403",
    "before": null,
    "after": "Table V B p.393 week 2: top-minus-bottom position change 0.28 percentage points of ranking-day open interest; bottom group mean -0.22%."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1404",
    "before": null,
    "after": "Table V B p.393 weeks 3-4: top-minus-bottom position change -1.37 percentage points of ranking-day open interest; bottom group mean 0.51%."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1405",
    "before": null,
    "after": "Table V B p.393 weeks 5-8: top-minus-bottom position change -2.49 percentage points of ranking-day open interest; bottom group mean 0.82%."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1406",
    "before": null,
    "after": "Table V B p.393 weeks 1-8: top-minus-bottom position change -0.63 percentage points of ranking-day open interest; bottom group mean -0.44%."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q30",
    "before": null,
    "after": "p.394: stated 73 bps over days 1-20, about 9% annualized, exceeds premium on a passive long position in the broad commodity market. Benchmark is a passive-market expected/average excess return; exact value not given in comparison sentence. Do not substitute the treatment size or attribute a computed ratio."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1397",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1398",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1399",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1400",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1401",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1402",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1403",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1404",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1405",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1406",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R30",
    "before": null,
    "after": "Broad passive-market mean is a different portfolio/weighting from the extreme-Q sorted contrast. Annualization itself is not division by a benchmark. Source rounding discrepancy .72 versus printed .73 disclosed in outcome correction."
  },
  {
    "sheet": "Outcomes",
    "cell": "A4288",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Outcomes",
    "cell": "B4288",
    "before": null,
    "after": "s4"
  },
  {
    "sheet": "Outcomes",
    "cell": "C4288",
    "before": null,
    "after": "hy1"
  },
  {
    "sheet": "Outcomes",
    "cell": "H202",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H203",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H204",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H205",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H206",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H207",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H4288",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I202",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I203",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I204",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I205",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I206",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I207",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I4288",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J202",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J203",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J204",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J205",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J206",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J207",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J4288",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "K4288",
    "before": null,
    "after": "Days 1-20 post-ranking excess return; p.394 reports high-minus-low 73 bps, about 9% annualized. Distinct from y5 days 1-40. Rounded Table V subperiod spreads .24+.29+.19 percentage points sum .72; retain printed prose .73 rather than silently altering source."
  },
  {
    "sheet": "Settings",
    "cell": "I80",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J80",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K80",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L80",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M80",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N80",
    "before": null,
    "after": "Table V A-B pp.393-394: implemented top-versus-bottom commercial-Q quintile contrast, with intermediate quintile means as descriptive context. Compare subsequent excess returns and reversal of commercial positions. Binary labels refer to top versus bottom group membership, not raw continuous Q."
  },
  {
    "sheet": "Settings",
    "cell": "O80",
    "before": null,
    "after": "Retained for the authors explicit price-pressure/liquidity causal interpretation, not as design-based proof. Observational position/return covariation can reflect omitted fundamentals and simultaneous trading. OLS category = linear unadjusted sorted-group mean contrast (equivalent to a binary-regressor slope); no matching/weighting to balance treatment covariates. Author price-pressure interpretation retained. Pre-ranking outcomes are diagnostics, not additional effects. Added days 1-20 outcome for existing prose comparison; y5 is days 1-40 and was wrong link."
  }
]
```

## 2026-10-11T02:01:15.948123+00:00 — Review 3DI8S52Q s5: causal scope, outcomes and benchmark evidence

7 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I81",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J81",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K81",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L81",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M81",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N81",
    "before": null,
    "after": "Table VI pp.395-396: restrict to continuous SMOOTHED hedging pressure (52-week trailing average net short position, scaled by current open interest), Fama-MacBeth OLS effects on weeks t+1/t+2 excess returns; with/without Q control. Raw HP and focal short-term Q effects split into h1/h2."
  },
  {
    "sheet": "Settings",
    "cell": "O81",
    "before": null,
    "after": "Retained for the authors explicit price-pressure/liquidity causal interpretation, not as design-based proof. Observational position/return covariation can reflect omitted fundamentals and simultaneous trading. Smoothing is not an instrument. Smoothed coefficients .52/.47 and .53/.45 (times 100) interpreted as hedging-demand premium. No outcome-mean/SD benchmark."
  }
]
```

## 2026-10-11T02:01:34.004457+00:00 — Review 3DI8S52Q s6: causal scope, outcomes and benchmark evidence

7 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Settings",
    "cell": "I82",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J82",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K82",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L82",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M82",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N82",
    "before": null,
    "after": "Table VII A-B pp.396-397: continuous smoothed hedging-pressure effect on weeks t+1/t+2 returns; DCOT producers and comparable-period COT commercial measures, June 2007-December 2017, with/without controls. Short-term Q treatment separated into h3."
  },
  {
    "sheet": "Settings",
    "cell": "O82",
    "before": null,
    "after": "Retained for the authors explicit price-pressure/liquidity causal interpretation, not as design-based proof. Observational position/return covariation can reflect omitted fundamentals and simultaneous trading. Restore omitted COT columns as same-location alternative measurement/sample comparison, rather than treating them as absent. Fama-MacBeth OLS, no FE."
  }
]
```

## 2026-10-11T02:01:52.457691+00:00 — Review 3DI8S52Q s7: causal scope, outcomes and benchmark evidence

198 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "A1407",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1408",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1409",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1410",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1411",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1412",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1413",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1414",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1415",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1416",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1417",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1418",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1419",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1420",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1421",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "A1422",
    "before": null,
    "after": "3DI8S52Q"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1407",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1408",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1409",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1410",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1411",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1412",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1413",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1414",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1415",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1416",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1417",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1418",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1419",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1420",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1421",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "B1422",
    "before": null,
    "after": "s7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1407",
    "before": null,
    "after": "hc1"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1408",
    "before": null,
    "after": "hc2"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1409",
    "before": null,
    "after": "hc3"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1410",
    "before": null,
    "after": "hc4"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1411",
    "before": null,
    "after": "hc5"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1412",
    "before": null,
    "after": "hc6"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1413",
    "before": null,
    "after": "hc7"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1414",
    "before": null,
    "after": "hc8"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1415",
    "before": null,
    "after": "hc9"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1416",
    "before": null,
    "after": "hc10"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1417",
    "before": null,
    "after": "hc11"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1418",
    "before": null,
    "after": "hc12"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1419",
    "before": null,
    "after": "hc13"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1420",
    "before": null,
    "after": "hc14"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1421",
    "before": null,
    "after": "hc15"
  },
  {
    "sheet": "Comparisons",
    "cell": "C1422",
    "before": null,
    "after": "hc16"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1407",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1408",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1409",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1410",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1411",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1412",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1413",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1414",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1415",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1416",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1417",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1418",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1419",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1420",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1421",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "K1422",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1407",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1408",
    "before": null,
    "after": "y1"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1409",
    "before": null,
    "after": "y2"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1410",
    "before": null,
    "after": "y2"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1411",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1412",
    "before": null,
    "after": "y3"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1413",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1414",
    "before": null,
    "after": "y4"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1415",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1416",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1417",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1418",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1419",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1420",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1421",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "L1422",
    "before": null,
    "after": "y5"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1407",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1408",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1409",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1410",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1411",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1412",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1413",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1414",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1415",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1416",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1417",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1418",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1419",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1420",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1421",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "M1422",
    "before": null,
    "after": "outcome_mean"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1407",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1408",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1409",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1410",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1411",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1412",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1413",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1414",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1415",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1416",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1417",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1418",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1419",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1420",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1421",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "N1422",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1407",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1408",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1409",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1410",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1411",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1412",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1413",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1414",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1415",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1416",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1417",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1418",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1419",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1420",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1421",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "O1422",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1407",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1408",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1409",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1410",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1411",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1412",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1413",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1414",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1415",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1416",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1417",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1418",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1419",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1420",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1421",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "P1422",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1407",
    "before": null,
    "after": "Table VIII A pp.398-399 days1-4, low-HP stratum: high-minus-low Q difference 0.21 percentage points; low-Q mean -0.1%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1408",
    "before": null,
    "after": "Table VIII A pp.398-399 days1-4, high-HP stratum: high-minus-low Q difference 0.17 percentage points; low-Q mean 0.05%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1409",
    "before": null,
    "after": "Table VIII A pp.398-399 days5-20, low-HP stratum: high-minus-low Q difference 0.05 percentage points; low-Q mean -0.11%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1410",
    "before": null,
    "after": "Table VIII A pp.398-399 days5-20, high-HP stratum: high-minus-low Q difference 0.49 percentage points; low-Q mean 0.2%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1411",
    "before": null,
    "after": "Table VIII A pp.398-399 days21-40, low-HP stratum: high-minus-low Q difference -0.08 percentage points; low-Q mean -0.08%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1412",
    "before": null,
    "after": "Table VIII A pp.398-399 days21-40, high-HP stratum: high-minus-low Q difference -0.05 percentage points; low-Q mean 0.63%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1413",
    "before": null,
    "after": "Table VIII A pp.398-399 days1-40, low-HP stratum: high-minus-low Q difference 0.17 percentage points; low-Q mean -0.29%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1414",
    "before": null,
    "after": "Table VIII A pp.398-399 days1-40, high-HP stratum: high-minus-low Q difference 0.61 percentage points; low-Q mean 0.88%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1415",
    "before": null,
    "after": "Table VIII B pp.398-399 week1, low-HP stratum: high-minus-low Q difference 1.24 percentage points; low-Q mean -0.89%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1416",
    "before": null,
    "after": "Table VIII B pp.398-399 week1, high-HP stratum: high-minus-low Q difference 1.82 percentage points; low-Q mean -0.86%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1417",
    "before": null,
    "after": "Table VIII B pp.398-399 weeks2-4, low-HP stratum: high-minus-low Q difference -0.24 percentage points; low-Q mean -0.51%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1418",
    "before": null,
    "after": "Table VIII B pp.398-399 weeks2-4, high-HP stratum: high-minus-low Q difference -0.96 percentage points; low-Q mean 0.74%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1419",
    "before": null,
    "after": "Table VIII B pp.398-399 weeks5-8, low-HP stratum: high-minus-low Q difference -1.03 percentage points; low-Q mean -0.16%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1420",
    "before": null,
    "after": "Table VIII B pp.398-399 weeks5-8, high-HP stratum: high-minus-low Q difference -1.18 percentage points; low-Q mean 0.9%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1421",
    "before": null,
    "after": "Table VIII B pp.398-399 weeks1-8, low-HP stratum: high-minus-low Q difference -0.03 percentage points; low-Q mean -1.56%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "Q1422",
    "before": null,
    "after": "Table VIII B pp.398-399 weeks1-8, high-HP stratum: high-minus-low Q difference -0.32 percentage points; low-Q mean 0.78%. Rounded printed differences retained."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1407",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1408",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1409",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1410",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1411",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1412",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1413",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1414",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1415",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1416",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1417",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1418",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1419",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1420",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1421",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Comparisons",
    "cell": "R1422",
    "before": null,
    "after": "Observed comparison-group mean is not established as the treated/high-bin untreated counterfactual. Table pairs an explicit difference with group outcome means; no division by mean."
  },
  {
    "sheet": "Outcomes",
    "cell": "H212",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H213",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H214",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H215",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "H216",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Outcomes",
    "cell": "I212",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I213",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I214",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I215",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "I216",
    "before": null,
    "after": "unknown"
  },
  {
    "sheet": "Outcomes",
    "cell": "J212",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J213",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J214",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J215",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Outcomes",
    "cell": "J216",
    "before": null,
    "after": "none"
  },
  {
    "sheet": "Settings",
    "cell": "I83",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J83",
    "before": null,
    "after": "OLS"
  },
  {
    "sheet": "Settings",
    "cell": "K83",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "L83",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "M83",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N83",
    "before": null,
    "after": "Table VIII A-B pp.398-399: high-versus-low current commercial Q contrast within each smoothed-hedging-pressure half. Binary Q-bin treatment; separate high-versus-low smoothed-HP contrasts into h4. Outcomes: returns and later commercial position changes."
  },
  {
    "sheet": "Settings",
    "cell": "O83",
    "before": null,
    "after": "Retained for the authors explicit price-pressure/liquidity causal interpretation, not as design-based proof. Observational position/return covariation can reflect omitted fundamentals and simultaneous trading. OLS category = linear unadjusted two-way sorted-group contrasts (equivalent binary-regressor slopes), NOT covariate-balancing matching. Distinct focal HP and Q contrasts cannot be one unspecified four-valued treatment. Two HP strata are effect heterogeneity for the Q contrast."
  }
]
```

## 2026-10-11T02:02:10.385432+00:00 — Review 3DI8S52Q s8: causal scope, outcomes and benchmark evidence

9 populated-cell value changes. The XLSX also preserves formatting.

```json
[
  {
    "sheet": "Comparisons",
    "cell": "K31",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Comparisons",
    "cell": "R31",
    "before": null,
    "after": "Wrong benchmark and now wrong split: 3.39% of open interest is treatment magnitude, NOT return outcome baseline. The 8.2 versus 15.6 bps statement p.404 compares two conditional Q effects (large-loss modifier now h6), not an outcome-level benchmark; do not relabel an effect-versus-effect comparison as other_level."
  },
  {
    "sheet": "Settings",
    "cell": "I84",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "J84",
    "before": null,
    "after": "FE"
  },
  {
    "sheet": "Settings",
    "cell": "K84",
    "before": null,
    "after": "0"
  },
  {
    "sheet": "Settings",
    "cell": "L84",
    "before": null,
    "after": "1"
  },
  {
    "sheet": "Settings",
    "cell": "M84",
    "before": null,
    "after": "n/a"
  },
  {
    "sheet": "Settings",
    "cell": "N84",
    "before": null,
    "after": "Table IX A pp.400-402: continuous commercial Q return slope and its modification by high commodity-specific implied volatility. Commodity-FE linear panel regression, weeks t+1/t+2, with/without high-VIX interaction. Other risk modifiers split into h5-h7."
  },
  {
    "sheet": "Settings",
    "cell": "O84",
    "before": null,
    "after": "Retained for the authors explicit price-pressure/liquidity causal interpretation, not as design-based proof. Observational position/return covariation can reflect omitted fundamentals and simultaneous trading. Q remains continuous; a binary moderator does not by itself make the focal dose treatment binary. Commodity FE remove time-invariant commodity heterogeneity. Main conclusion explicitly emphasized in introduction/conclusion. The roughly twice wording compares conditional Q effects, not effect to an outcome mean/SD or untreated outcome level."
  }
]
```
