import pandas as pd
from pathlib import Path

RAW_DIR = Path("./data/raw")
PROCESSED_DIR = Path("./data/processed")

PROCESSED_DIR.mkdir(exist_ok=True)

print("="*60)
print("DAY 2 DATA CLEANING")
print("="*60)

# --------------------------------------------------
# NAV HISTORY
# --------------------------------------------------

nav = pd.read_csv(
    RAW_DIR / "02_nav_history.csv"
)

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    PROCESSED_DIR / "clean_nav_history.csv",
    index=False
)

print(
    f"Clean NAV rows: {len(nav)}"
)

# --------------------------------------------------
# INVESTOR TRANSACTIONS
# --------------------------------------------------

tx = pd.read_csv(
    RAW_DIR / "08_investor_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

valid_types = {
    "SIP",
    "Lumpsum",
    "Redemption"
}

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    # .str.title()
)

# print(tx["transaction_type"])

tx = tx[
    tx["transaction_type"].isin(valid_types)
]

# print(tx["transaction_type"])

tx = tx[
    tx["amount_inr"] > 0
]

valid_kyc = {
    "Verified",
    "Pending"
}

tx = tx[
    tx["kyc_status"].isin(valid_kyc)
]

tx = tx.drop_duplicates()

tx.to_csv(
    PROCESSED_DIR /
    "clean_investor_transactions.csv",
    index=False
)

print(
    f"Clean Transactions rows: {len(tx)}"
)

# --------------------------------------------------
# SCHEME PERFORMANCE
# --------------------------------------------------

perf = pd.read_csv(
    RAW_DIR /
    "07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:

    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["expense_ratio_flag"] = (
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
)

perf["negative_sharpe_flag"] = (
    perf["sharpe_ratio"] < 0
)

perf.to_csv(
    PROCESSED_DIR /
    "clean_scheme_performance.csv",
    index=False
)

print(
    f"Clean Performance rows: {len(perf)}"
)

print("\nDone.")