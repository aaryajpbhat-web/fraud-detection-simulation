
# data_generator.py
import numpy as np
import pandas as pd
from config import TRANSACTIONS, FRAUD_RATE, START_DATE

def generate_raw_transactions():
    np.random.seed(42)
    num_fraud = int(FRAUD_RATE * TRANSACTIONS)
    
    tx_ids = np.arange(1, TRANSACTIONS + 1)
    user_ids = np.random.randint(1000, 50000, size=TRANSACTIONS)
    merchant_ids = np.random.randint(1, 2000, size=TRANSACTIONS)
    amounts = np.random.lognormal(mean=3.0, sigma=1.0, size=TRANSACTIONS)
    distances = np.random.exponential(scale=10.0, size=TRANSACTIONS)
    
    fraud_indices = np.random.choice(TRANSACTIONS, size=num_fraud, replace=False)
    amounts[fraud_indices] = np.random.uniform(5000, 25000, size=num_fraud)
    distances[fraud_indices] = np.random.uniform(500, 3000, size=num_fraud)
    
    df = pd.DataFrame({
        'tx_id': tx_ids,
        'user_id': user_ids,
        'merchant_id': merchant_ids,
        'amount': np.round(amounts, 2),
        'distance_km': np.round(distances, 2)
    })
    
    # Add timestamps
    start_timestamp = pd.to_datetime(START_DATE)
    random_seconds = np.random.randint(0, 30 * 24 * 3600, size=TRANSACTIONS)
    df['timestamp'] = start_timestamp + pd.to_timedelta(random_seconds, unit='s')
    
    return df.sort_values('timestamp').reset_index(drop=True)
