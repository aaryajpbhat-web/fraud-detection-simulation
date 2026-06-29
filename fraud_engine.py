# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:14:49 2026

@author: VICTUS
"""

# fraud_engine.py
import numpy as np
import pandas as pd
import sqlite3

def apply_fraud_heuristics(df):
    df['payment_status'] = 'SUCCESS'
    timeout_indices = df.sample(frac=0.02).index
    df.loc[timeout_indices, 'payment_status'] = np.nan
    df['payment_status'] = df['payment_status'].fillna('NETWORK_TIMEOUT')
    
    df['1h_velocity'] = (
        df.groupby('user_id')
        .rolling('1h', on='timestamp')['tx_id']
        .count()
        .reset_index(level=0, drop=True)
        .sort_index()
        .to_numpy() 
    )
    
    df['is_flagged'] = (
        (df['1h_velocity'] > 5) | 
        (df['distance_km'] > 400) | 
        (df['amount'] > 4000)
    ).astype(int)
    
    return df

def get_riskiest_merchants(df):
    with sqlite3.connect(':memory:') as conn:
        df.to_sql('transactions', conn, index=False, if_exists='replace') 
        
        query = """
        WITH MerchantStats AS (
            SELECT merchant_id,
                   COUNT(tx_id) as total_tx_volume,
                   SUM(CASE WHEN is_flagged = 1 THEN 1 ELSE 0 END) as fraud_tx_count
            FROM transactions
            GROUP BY merchant_id
        )
        SELECT merchant_id,
               total_tx_volume,
               fraud_tx_count,
               ROUND((CAST(fraud_tx_count AS FLOAT) / total_tx_volume) * 100, 2) as fraud_percentage
        FROM MerchantStats
        WHERE total_tx_volume > 100
        ORDER BY fraud_percentage DESC, total_tx_volume DESC
        LIMIT 5;
        """
        return pd.read_sql_query(query, conn)