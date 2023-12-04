import requests

api_key = '4B82844F-2761-494A-A92F-DC0C8EB93910'
url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'

headers = {
    'X-CoinAPI-Key': api_key,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    rate = data['rate']
    print(f'Current Bitcoin to USD exchange rate: {rate}')
else:
    print(f'Error: {response.status_code}, {response.text}')
