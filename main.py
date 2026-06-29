# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:15:15 2026

@author: VICTUS
"""

# main.py
import time
from data_generator import generate_raw_transactions
from fraud_engine import apply_fraud_heuristics, get_riskiest_merchants

def main():
    print("Phase 1: Generating Data")
    start = time.time()
    df = generate_raw_transactions()
    print(f"-> Completed in {time.time()-start:.2f} seconds\n")
    
    print("Phase 2: Applying Fraud Heuristics")
    start = time.time()
    df_flagged = apply_fraud_heuristics(df)
    print(f"-> Completed in {time.time()-start:.2f} seconds\n")
    
    print("Phase 3: Calculating Merchant Risk")
    start = time.time()
    risky_merchants = get_riskiest_merchants(df_flagged)
    print(f"-> Completed in {time.time()-start:.2f} seconds\n")
    
    print("========================================")
    print("        TOP 5 RISKIEST MERCHANTS        ")
    print("========================================")
    print(risky_merchants)

if __name__ == "__main__":
    main()