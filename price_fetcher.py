import requests

def get_token_price_at_time(token_address, timestamp):
    url = f"https://api.coingecko.com/api/v3/coins/{token_address}/history"
    params = {"date": timestamp, "localization": "false"}
    response = requests.get(url, params=params)
    return response.json().get("market_data", {}).get("current_price", {}).get("usd", None)

def get_max_price(token_address):
    url = f"https://api.coingecko.com/api/v3/coins/{token_address}/market_chart"
    params = {"vs_currency": "usd", "days": "max"}
    response = requests.get(url, params=params)
    prices = response.json().get("prices", [])
    return max(prices, key=lambda x: x[1])
