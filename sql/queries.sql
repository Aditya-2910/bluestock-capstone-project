-- 1
SELECT *
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2
SELECT
strftime('%Y-%m', nav_date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- 3
SELECT
state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY 2 DESC;

-- 4
SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- 5
SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 6
SELECT
risk_grade,
AVG(sharpe_ratio)
FROM fact_performance
GROUP BY risk_grade;

-- 7
SELECT
fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- 8
SELECT
city_tier,
AVG(amount_inr)
FROM fact_transactions
GROUP BY city_tier;

-- 9
SELECT
gender,
SUM(amount_inr)
FROM fact_transactions
GROUP BY gender;

-- 10
SELECT
age_group,
AVG(amount_inr)
FROM fact_transactions
GROUP BY age_group;