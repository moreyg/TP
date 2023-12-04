import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Replace 'your_actual_api_key' with your actual CoinGecko API key
api_key = '4B82844F-2761-494A-A92F-DC0C8EB93910'

def get_crypto_historical_data(crypto_symbol, days_back=(365)):
    base_url = "https://api.coingecko.com/api/v3"
    endpoint = f"/coins/{crypto_symbol}/market_chart"
    #endpoint = f"/coins/{crypto_symbol}"
    
    # Calculate the start date (days_back days ago from today)
    start_date = (datetime.now() - timedelta(days=days_back)).strftime('%s')  # Convert to Unix timestamp
    
    params = {
        'vs_currency': 'usd',
        'days': days_back,
        'interval': 'daily',
        'api_key': api_key
    }

    response = requests.get(base_url + endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        #formated = json.dumps(data, indent=4)
        #print(formated)
        prices = data['prices']
        #formated = json.dumps(prices, indent=4)
        #print(formated)
        
        timestamps, prices = zip(*prices)
        dates = [datetime.utcfromtimestamp(timestamp / 1000) for timestamp in timestamps]
        print(timestamps)
        print(prices)
        print(dates)
        
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, prices, label=f'{crypto_symbol} Prices')
        plt.title(f'{crypto_symbol} Historical Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.savefig('bitcoin.png')
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Replace 'bitcoin' with the cryptocurrency symbol you want to get data for
get_crypto_historical_data('bluelight',30)
