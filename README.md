# Modular Fraud Detection Simulation

This project simulates a transactional dataset and applies basic rules-based heuristics to identify potentially fraudulent behavior. The code is modularized for professional readability and separation of concerns.

## Overview

The simulation runs in three distinct phases:

* **Phase 1 (Data Generation):** Generates 5 million mock transactions using normal and exponential distributions via `numpy`, injecting a 1% true fraud rate. Handled by `data_generator.py`.
* **Phase 2 (Heuristics):** Uses `pandas` to apply fraud detection rules, flagging transactions based on 1-hour velocity, distances over 400km, and amounts over $4,000. Handled by `fraud_engine.py`.
* **Phase 3 (SQL Risk Analysis):** Uses in-memory `sqlite3` to query the flagged data and output the top 5 riskiest merchants based on their percentage of fraudulent transactions. Handled by `fraud_engine.py`.

## Project Structure

* `config.py`: Stores global variables and simulation parameters.
* `data_generator.py`: Handles raw data creation.
* `fraud_engine.py`: Contains the logic for flagging fraud and running SQL analytics.
* `main.py`: The execution script that runs all phases in order.

## Requirements

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

To execute the simulation, run the main file in your terminal:

```bash
python main.py
```
