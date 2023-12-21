#Implementa el pedido simple de informacion

from .coinApi import COIN_API

class COIN_API_SYMBOLS(COIN_API):

    
    def __init__(self ):
        super().__init__(api_key, base_url)
        self.endpoint = 'symbols'



    def getAllDataFilter(self, fs="BINANCE_SPOT_B"):
        # url = "https://rest.coinapi.io/v1/symbols?filter_symbol_id=BINANCE_SPOT_B"
        url = f"{self.url}?filter_symbol_id={fs}"
        payload={}
        headers = self.headers
        response = requests.request("GET", url, headers=headers, data=payload)
        r = response.json()  # Return the JSON response En funcion de quien lo pida como trabajo la respuesta.
        print(f'CoinApi_get_Data() {type(r)}')
        print(f'CoinApi_get_Data() {len(r)}')
        return r

    def getAllData(self):
        '''
        # url = "https://rest.coinapi.io/v1/symbols"
        url = f"{self.url}"
        payload={}
        headers = self.headers
        response = requests.request("GET", url, headers=headers, data=payload)
        r = response.json()  # Return the JSON response En funcion de quien lo pida como trabajo la respuesta.
        print(f'CoinApi_get_Data() {type(r)}')
        print(f'CoinApi_get_Data() {len(r)}')
        '''
        respuesta = [ {"symbol_id": "BINANCE_SPOT_ETH_USDT2", "exchange_id": "BINANCE", "symbol_type": "SPOT", "asset_id_base": "ETH", "asset_id_quote": "USDT", "data_start": "2017-08-17", "data_end": "2023-12-14", "data_quote_start": "2017-12-18T00:00:00.0000000Z", "data_quote_end": "2023-12-14T00:00:00.0000000Z", "data_orderbook_start": "2017-12-18T21:56:06.7316673Z", "data_orderbook_end": "2023-07-07T00:00:00.0000000Z", "data_trade_start": "2017-08-17T00:00:00.0000000Z", "data_trade_end": "2023-12-14T00:00:00.0000000Z", "volume_1hrs": 10028.2969, "volume_1hrs_usd": 21360802.05, "volume_1day": 323954.0698, "volume_1day_usd": 690039278.62, "volume_1mth": 10598438.4238, "volume_1mth_usd": 22575233609.29, "price": 2132.485, "symbol_id_exchange": "ETHUSDT", "asset_id_base_exchange": "ETH", "asset_id_quote_exchange": "USDT", "price_precision": 0.01, "size_precision": 0.0001 }, { "symbol_id": "BINANCE_SPOT_BTC_USDC", "exchange_id": "BINANCE", "symbol_type": "SPOT", "asset_id_base": "BTC", "asset_id_quote": "USDC", "data_start": "2018-12-15", "data_end": "2023-12-14", "data_quote_start": "2018-12-15T00:00:00.0000000Z", "data_quote_end": "2023-12-14T00:00:00.0000000Z", "data_orderbook_start": "2018-12-15T03:00:00.6860000Z", "data_orderbook_end": "2023-07-07T00:00:00.0000000Z", "data_trade_start": "2018-12-15T00:00:00.0000000Z", "data_trade_end": "2023-12-14T00:00:00.0000000Z", "volume_1hrs": 38.03605, "volume_1hrs_usd": 1556915.69, "volume_1day": 1467.95954, "volume_1day_usd": 60087449.63, "volume_1mth": 29827.51329, "volume_1mth_usd": 1220918665.34, "price": 40928.035, "symbol_id_exchange": "BTCUSDC", "asset_id_base_exchange": "BTC", "asset_id_quote_exchange": "USDC", "price_precision": 0.01, "size_precision": 1e-05 }, { "symbol_id": "BINANCE_SPOT_ETH_USDT", "exchange_id": "BINANCE", "symbol_type": "SPOT", "asset_id_base": "ETH", "asset_id_quote": "USDT", "data_start": "2017-08-17", "data_end": "2023-12-14", "data_quote_start": "2017-12-18T00:00:00.0000000Z", "data_quote_end": "2023-12-14T00:00:00.0000000Z", "data_orderbook_start": "2017-12-18T21:56:06.7316673Z", "data_orderbook_end": "2023-07-07T00:00:00.0000000Z", "data_trade_start": "2017-08-17T00:00:00.0000000Z", "data_trade_end": "2023-12-14T00:00:00.0000000Z", "volume_1hrs": 10028.2969, "volume_1hrs_usd": 21360802.05, "volume_1day": 323954.0698, "volume_1day_usd": 690039278.62, "volume_1mth": 10598438.4238, "volume_1mth_usd": 22575233609.29, "price": 2132.485, "symbol_id_exchange": "ETHUSDT", "asset_id_base_exchange": "ETH", "asset_id_quote_exchange": "USDT", "price_precision": 0.01, "size_precision": 0.0001 }]
        return respuesta

