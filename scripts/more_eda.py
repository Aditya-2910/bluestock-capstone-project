import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#-------- this is for the performance analytics section in report---------#

#------------- for nav vs nifty50---------------------#


fund_code = 119551

nav = pd.read_csv("./data/processed/clean_nav_history.csv")
bench = pd.read_csv("./data/raw/10_benchmark_indices.csv")

nav["date"] = pd.to_datetime(nav["date"])
bench["date"] = pd.to_datetime(bench["date"])

fund = nav[nav["amfi_code"] == fund_code].copy()

nifty50 = bench[
    bench["index_name"] == "NIFTY50"
].copy()

nifty100 = bench[
    bench["index_name"]=="NIFTY100"
]

fund["normalized"] = (
    fund["nav"] /
    fund["nav"].iloc[0]
) * 100

nifty50["normalized"] = (
    nifty50["close_value"] /
    nifty50["close_value"].iloc[0]
) * 100

plt.figure(figsize=(12,6))

plt.plot(
    fund["date"],
    fund["normalized"],
    label="SBI Bluechip"
)

plt.plot(
    nifty50["date"],
    nifty50["normalized"],
    label="NIFTY50"
)

plt.legend()
plt.title("Growth of ₹100 Invested")
plt.ylabel("Normalized Value")

plt.savefig(
    "./reports/nav_vs_nifty50.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


#----------------------- for nav vs nifty100-------------------#
fund_code = 119551

nav = pd.read_csv("./data/processed/clean_nav_history.csv")
bench = pd.read_csv("./data/raw/10_benchmark_indices.csv")

nav["date"] = pd.to_datetime(nav["date"])
bench["date"] = pd.to_datetime(bench["date"])

fund = nav[nav["amfi_code"] == fund_code].copy()


nifty100 = bench[
    bench["index_name"]=="NIFTY100"
]

fund["normalized"] = (
    fund["nav"] /
    fund["nav"].iloc[0]
) * 100

nifty100["normalized"] = (
    nifty100["close_value"] /
    nifty100["close_value"].iloc[0]
) * 100

plt.figure(figsize=(12,6))

plt.plot(
    fund["date"],
    fund["normalized"],
    label="SBI Bluechip"
)

plt.plot(
    nifty100["date"],
    nifty100["normalized"],
    label="NIFTY100"
)

plt.legend()
plt.title("Growth of ₹100 Invested")
plt.ylabel("Normalized Value")

plt.savefig(
    "./reports/nav_vs_nifty100.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



#---------------------cohort analystics for Advanced analystics ==================#

import seaborn as sns
tx = pd.read_csv(
    "./data/processed/clean_investor_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

first_tx = (
    tx.groupby("investor_id")
      ["transaction_date"]
      .min()
      .reset_index()
)

first_tx["cohort_year"] = (
    pd.to_datetime(
        first_tx["transaction_date"]
    ).dt.year
)

cohort = (
    first_tx["cohort_year"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=cohort.index,
    y=cohort.values
)

plt.title(
    "Investor Cohort Analysis"
)

plt.xlabel(
    "First Investment Year"
)

plt.ylabel(
    "Number of Investors"
)

plt.savefig(
    "./reports/cohort_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#-----------------------------for sip continuity chart-------------#
sip = tx[
    tx["transaction_type"]
    == "SIP"
].copy()

sip = sip.sort_values(
    ["investor_id",
     "transaction_date"]
)

sip["gap_days"] = (

sip.groupby("investor_id")
   ["transaction_date"]
   .diff()
   .dt.days

)

eligible = (
    sip.groupby("investor_id")
       .size()
)

eligible = eligible[
    eligible >= 6
].index

gap_analysis = (

sip[
    sip["investor_id"]
    .isin(eligible)
]

.groupby("investor_id")
["gap_days"]

.mean()

.reset_index()

)
gap_analysis["status"] = np.where(

gap_analysis["gap_days"] > 35,

"At Risk",

"Healthy"

)
status_counts = (
    gap_analysis["status"]
    .value_counts()
)

plt.figure(figsize=(8,8))

plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%"
)

plt.title(
    "SIP Continuity Analysis"
)

plt.savefig(
    "./reports/sip_continuity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


holdings = pd.read_csv(
    "./data/raw/09_portfolio_holdings.csv"
)

sector_alloc = (

holdings.groupby("sector")
["weight_pct"]

.sum()

.sort_values(
    ascending=False
)

.head(10)

)

plt.figure(figsize=(10,10))

plt.pie(
    sector_alloc.values,
    labels=sector_alloc.index,
    autopct="%1.1f%%"
)

plt.title(
    "Sector Allocation Across Equity Funds"
)

plt.savefig(
    "./reports/sector_allocation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

hhi = (

holdings.groupby(
    "amfi_code"
)

["weight_pct"]

.apply(
    lambda x:
    np.sum(
        (x/100)**2
    )
)

.reset_index(
    name="HHI"
)

)

top_hhi = (

hhi.sort_values(
    "HHI",
    ascending=False
)

.head(15)

)

import seaborn as sns

plt.figure(figsize=(12,6))

sns.barplot(
    data=top_hhi,
    x="amfi_code",
    y="HHI"
)

plt.xticks(
    rotation=45
)

plt.title(
    "Portfolio Concentration (HHI)"
)

plt.savefig(
    "./reports/hhi_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()