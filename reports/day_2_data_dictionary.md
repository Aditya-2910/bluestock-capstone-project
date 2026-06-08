# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | AMFI Scheme Code |
| scheme_name | TEXT | Mutual Fund Name |
| fund_house | TEXT | AMC Name |
| category | TEXT | Fund Category |
| plan | TEXT | Direct/Regular |
| expense_ratio_pct | REAL | Expense Ratio |
| risk_grade | TEXT | Risk Category |

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Fund Identifier |
| date | DATE | NAV Date |
| nav | REAL | Daily NAV |