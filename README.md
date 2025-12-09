# BNPL_Customer_Project
BNPL Customer Insights &amp; Risk Analysis

Objective
Analyze Buy Now, Pay Later (BNPL) customer data to uncover trends, assess repayment behavior, and identify high-risk patterns.
Dataset Includes 20,000 rows
________________________________________
Python Data Pipeline (ETL Setup)
Purpose:
Build a modular data pipeline to manage the entire data flow: from raw generation or ingestion to transformation and cleaning.
Pipeline Components:

1.	extract_data() – Loads or generates raw data.
2.	clean_data(df) – Handles nulls, duplicates, and fixes data types.
3.	transform_data(df) – Creates new features, e.g., total repayment.
4.	validate_data(df) – Ensures data quality (valid credit scores, no negatives).
5.	save_data(df, filename) – Exports the clean file for later use.
________________________________________
SQL Analysis

1.	Total purchases by customer
2.	Missed payments by the merchant
3.	Avg income vs. credit score
4.	Most common product categories per location
5.	Risk classification based on late payments
________________________________________
Power BI Visualization

1. KPIs: Total Users, Active Users, Default Rate 
2. Bar Chart: Product Categories by Revenue
3. Heatmap: Risk by Region
4. Line Chart: Monthly Sales Volume
5. Pie Chart: Gender Distribution
