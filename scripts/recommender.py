import pandas as pd

perf = pd.read_csv(
    "./data/processed/clean_scheme_performance.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

recommend = (

perf[
    perf["risk_grade"]
    .str.contains(
        risk,
        case=False
    )
]

.sort_values(
    "sharpe_ratio",
    ascending=False
)

.head(3)

)

print(
recommend[
[
"scheme_name",
"fund_house",
"sharpe_ratio",
"return_3yr_pct"
]
]
)