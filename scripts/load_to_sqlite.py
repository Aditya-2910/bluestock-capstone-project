import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

DB_PATH = (
    "./data/db/bluestock_mf.db"
)

engine = create_engine(
    f"sqlite:///{DB_PATH}"
)

fund = pd.read_csv(
    "./data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "./data/processed/clean_nav_history.csv"
)

tx = pd.read_csv(
    "./data/processed/clean_investor_transactions.csv"
)

perf = pd.read_csv(
    "./data/processed/clean_scheme_performance.csv"
)

aum = pd.read_csv(
    "./data/raw/03_aum_by_fund_house.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

tx.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded.")