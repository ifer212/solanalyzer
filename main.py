import asyncio
from fetch_transactions import get_wallet_transactions, get_transaction_details
from price_fetcher import get_token_price_at_time, get_max_price
from analytics import calculate_pnl, create_dataframe
from dashboard import display_dashboard

# Wallet address to track
wallet_address = '9xN3GQxipaW1hmM6224ozFCK3EfLuhKd1caC7gJiRBTF'

async def main():
    # Fetch transactions
    transactions = await get_wallet_transactions(wallet_address)
    
    data = {
        "tx_signature": [],
        "token_in": [],
        "token_out": [],
        "entry_price": [],
        "exit_price": [],
        "amount": [],
        "pnl": [],
        "max_price": [],
    }
    
    for tx in transactions:
        tx_details = await get_transaction_details(tx.signature)
        swap_details = extract_swap_details(tx_details)  # Implement this function
        
        for swap in swap_details:
            entry_price = get_token_price_at_time(swap["token_in"], swap["timestamp"])
            exit_price = get_token_price_at_time(swap["token_out"], swap["timestamp"])
            max_price = get_max_price(swap["token_out"])
            pnl = calculate_pnl(entry_price, exit_price, swap["amount"])
            
            data["tx_signature"].append(tx.signature)
            data["token_in"].append(swap["token_in"])
            data["token_out"].append(swap["token_out"])
            data["entry_price"].append(entry_price)
            data["exit_price"].append(exit_price)
            data["amount"].append(swap["amount"])
            data["pnl"].append(pnl)
            data["max_price"].append(max_price[1])
    
    df = create_dataframe(data)
    display_dashboard(df)

# Run the main function
asyncio.run(main())
