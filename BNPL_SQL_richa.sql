#1.	Total purchases by customer
SELECT customer_id, COUNT(*) AS num_purchases, SUM(amount) AS total_spent
FROM cleaned_bnpl_data
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 50;

#2.	Missed payments by the merchant
SELECT merchant, SUM(missed_payments) AS total_missed_payments, COUNT(*) AS txn_count
FROM cleaned_bnpl_data
GROUP BY merchant
ORDER BY total_missed_payments DESC;

#) 3. Avg income vs credit score 
SELECT 
  AVG(income) AS avg_income, 
  AVG(credit_score) AS avg_credit_score
 FROM cleaned_bnpl_data;


# 4.	Most common product categories per location
SELECT region, product_category, COUNT(*) AS cnt
FROM cleaned_bnpl_data
GROUP BY region, product_category
ORDER BY region, cnt DESC;


#5.	Risk classification based on late payments
SELECT customer_id,
       SUM(missed_payments) AS total_missed,
       MAX(credit_score) AS max_credit_score,
       CASE WHEN SUM(missed_payments) >= 2 OR AVG(repayment_rate) < 0.8 OR MAX(credit_score) < 550 THEN 'HIGH' ELSE 'LOW' END AS risk_label
FROM cleaned_bnpl_data
GROUP BY customer_id
ORDER BY total_missed DESC;

