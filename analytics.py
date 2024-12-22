import pandas as pd

def calculate_pnl(entry_price, exit_price, amount):
    return (exit_price - entry_price) * amount

def create_dataframe(data):
    return pd.DataFrame(data)
