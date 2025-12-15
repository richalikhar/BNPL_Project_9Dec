#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
from pathlib import Path

def extract_data(path="bnpl_dataset_20000.csv"):
    return pd.read_csv(path)

#df = extract_data("bnpl_dataset_20000.csv")


# In[8]:


df.info();


# In[ ]:





# In[33]:


def clean_data(df):
    df = df.copy()
    # drop exact duplicates
    df = df.drop_duplicates()
    # Standardize date type
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    # Rename Columns
    df.rename(columns={
     'customer_income' : 'income',
     'merchant_name'   : 'merchant',
     'late_payments'   : 'missed_payments'
        }, inplace=True)   
    # Fix types
    num_cols = ['purchase_amount','down_payment','installments','age','income','credit_score','late_payments','missed_payments','fraud_flag','amount_repaid','default_flag']
    for c in num_cols:
        if c in df.columns:
            df[c]=pd.to_numeric(df[c],errors='coerce')
    # Fill small missing demographics with medians/modes
    if 'age' in df.columns:
        df['age'] = df['age'].fillna(df['age'].median().round(0))
    if 'income' in df.columns:
        df['income'] = df['income'].fillna(df['income'].median().round(0))
    if 'credit_score' in df.columns:
        df['credit_score'] = df['credit_score'].fillna(df['credit_score'].median().round(0))
    if 'gender' in df.columns:
        df['gender'] = df['gender'].fillna('Unknown')
    # Ensure non-negative where required
    for c in ['amount','down_payment','installments','income','amount_repaid']:
        if c in df.columns:
             df.loc[df[c] < 0,c] = np.nan
        return df
        


# In[ ]:





# In[34]:


def transform_data(df):
    df = df.copy()
    
    
    
    
    # Total financed amount = purchase_amount - down_payment
    df['financed_amount'] = df['purchase_amount'] - df['down_payment']
    # total_repaid_amount = down_payment + (installment_amount * installments_paid)
    df['total_repaid_amount'] = (df['down_payment']  + (df['installment_amount']  * df['installments'])).fillna(0)
    # Flag high risk: low repayment rate or many missed payments
    df['high_risk'] = ((df['total_repaid_amount'] < 0.8) | (df['missed_payments'] >= 2) | (df['credit_score'] < 550)).astype(int)
   # Monthly installment estimate
    df['monthly_installment_est'] = df['financed_amount'] / df['installments']
    return df



# In[ ]:


df


# In[35]:


def validate_data(df):
    problems = []
    if df['credit_score'].between(300,850).all() == 'false':
        problems.append("some credit scores outside 300-850")
    #nonegativeamounts
    if(df['purchase_amount'] < 0).any():
        problems.append("negative amount found")
    return problems









# In[36]:


def save_data(df, filename="cleaned_bnpl_data_new.csv"):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filename, index=False)
    return filename



# In[31]:


if __name__ == "__main__":
    df = extract_data("bnpl_dataset_20000.csv")
    dfc = clean_data(df)
    dft = transform_data(dfc)
    problems = validate_data(dft)
    print("Validation problems:", problems)
    save_data(dft, "cleaned_bnpl_data.csv")
    print("Saved cleaned_bnpl_data.csv")
   
   
    


# In[26]:


df.info()


# In[ ]:




