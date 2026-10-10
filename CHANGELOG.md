
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
