import logging
import requests

# Get the logger
logger = logging.getLogger('my_tp_app')

# Use the logger
logger.info('Mensaje de request_class.py')

class COIN_API():

    def __init__(self):
        """'
        Initialize the APIRequestHandler with specific apiKey, baseUrl, and global endpoints.
        :param api_key: API key for authentication.
        :param base_url: Base URL of the API.
        :param global_endpoints: List of global endpoints.
        """
        self.url_symbols = "https://rest.coinapi.io/v1/symbols"
        self.api_key  = '4B82844F-2761-494A-A92F-DC0C8EB93910'
        self.headers = {                           
           'Accept': 'text/json',
           'X-CoinAPI-Key': self.api_key
           }
        self.infoS = [ {"symbol_id": "BINANCE_SPOT_ETH_USDT2", "exchange_id": "BINANCE", "symbol_type": "SPOT", "asset_id_base": "ETH", "asset_id_quote": "USDT", "data_start": "2017-08-17", "data_end": "2023-12-14", "data_quote_start": "2017-12-18T00:00:00.0000000Z", "data_quote_end": "2023-12-14T00:00:00.0000000Z", "data_orderbook_start": "2017-12-18T21:56:06.7316673Z", "data_orderbook_end": "2023-07-07T00:00:00.0000000Z", "data_trade_start": "2017-08-17T00:00:00.0000000Z", "data_trade_end": "2023-12-14T00:00:00.0000000Z", "volume_1hrs": 10028.2969, "volume_1hrs_usd": 21360802.05, "volume_1day": 323954.0698, "volume_1day_usd": 690039278.62, "volume_1mth": 10598438.4238, "volume_1mth_usd": 22575233609.29, "price": 2132.485, "symbol_id_exchange": "ETHUSDT", "asset_id_base_exchange": "ETH", "asset_id_quote_exchange": "USDT", "price_precision": 0.01, "size_precision": 0.0001 }, { "symbol_id": "BINANCE_SPOT_BTC_USDC", "exchange_id": "BINANCE", "symbol_type": "SPOT", "asset_id_base": "BTC", "asset_id_quote": "USDC", "data_start": "2018-12-15", "data_end": "2023-12-14", "data_quote_start": "2018-12-15T00:00:00.0000000Z", "data_quote_end": "2023-12-14T00:00:00.0000000Z", "data_orderbook_start": "2018-12-15T03:00:00.6860000Z", "data_orderbook_end": "2023-07-07T00:00:00.0000000Z", "data_trade_start": "2018-12-15T00:00:00.0000000Z", "data_trade_end": "2023-12-14T00:00:00.0000000Z", "volume_1hrs": 38.03605, "volume_1hrs_usd": 1556915.69, "volume_1day": 1467.95954, "volume_1day_usd": 60087449.63, "volume_1mth": 29827.51329, "volume_1mth_usd": 1220918665.34, "price": 40928.035, "symbol_id_exchange": "BTCUSDC", "asset_id_base_exchange": "BTC", "asset_id_quote_exchange": "USDC", "price_precision": 0.01, "size_precision": 1e-05 }, { "symbol_id": "BINANCE_SPOT_ETH_USDT", "exchange_id": "BINANCE", "symbol_type": "SPOT", "asset_id_base": "ETH", "asset_id_quote": "USDT", "data_start": "2017-08-17", "data_end": "2023-12-14", "data_quote_start": "2017-12-18T00:00:00.0000000Z", "data_quote_end": "2023-12-14T00:00:00.0000000Z", "data_orderbook_start": "2017-12-18T21:56:06.7316673Z", "data_orderbook_end": "2023-07-07T00:00:00.0000000Z", "data_trade_start": "2017-08-17T00:00:00.0000000Z", "data_trade_end": "2023-12-14T00:00:00.0000000Z", "volume_1hrs": 10028.2969, "volume_1hrs_usd": 21360802.05, "volume_1day": 323954.0698, "volume_1day_usd": 690039278.62, "volume_1mth": 10598438.4238, "volume_1mth_usd": 22575233609.29, "price": 2132.485, "symbol_id_exchange": "ETHUSDT", "asset_id_base_exchange": "ETH", "asset_id_quote_exchange": "USDT", "price_precision": 0.01, "size_precision": 0.0001 }]

    def config_getApiKey(self):
        return self.api_key

    def config_setApiKey(self, newKey):
        self.api_key=newKey

    def getInfoS(self, filtro="BINANCE_SPOT_B"): 
        if filtro == 'test' :
            return self.infoS
        resultado=None
        if filtro is None or filtro == '':
            # TODOS LOS SIMBOLOS 
            url = "https://rest.coinapi.io/v1/symbols"
            payload={}
            headers = self.headers
            resultado = self.my_request(url, headers, payload)
        else:
            # El filtro tiene algún valor
            url =f'https://rest.coinapi.io/v1/symbols?filter_symbol_id={filtro}'
            payload={}
            headers = self.headers
            resultado = self.my_request(url, headers, payload)
        return resultado    
             

    def getDataS(self, symbol, stime, etime): 
        resultado= None
        url = f'https://rest.coinapi.io/v1/quotes/{symbol}/history?time_start={stime}&time_end={etime}'
        payload={}
        headers = self.headers
        resultado = self.my_request(url, headers, payload)
        return resultado    

    def my_request(self, url, headers, payload):
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.headers)
            #print(response.text)
            return response.json()
        except HTTPError as http_err:
            print(f"Error HTTP: {http_err}")  # Detalles del error HTTP
        except Timeout as timeout_err:
            print(f"Error de tiempo de espera: {timeout_err}")  # La solicitud excedió el tiempo límite
        except ConnectionError as conn_err:
            print(f"Error de conexión: {conn_err}")  # Error de conexión
        except Exception as err:
            print(f"Ocurrió un error: {err}")  # Otros errores
        return None  # O maneja la situación de error de otra manera

    def get_symbol_quotes(self, symbol, start, end, limit='100'):
        self.testing_quotes()




    def testing_quotes(self):
        url = "https://rest.coinapi.io/v1/quotes/BINANCE_SPOT_BTC_USDT/history?time_start=2023-01-02&time_end=2023-07-16"
        payload={}
        headers = {
            'Accept': 'text/plain',
            'X-CoinAPI-Key': '4B82844F-2761-494A-A92F-DC0C8EB93910'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        #print(response.text)
        print(f'Headers: {response.headers}')
        return response

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

    def fetch_global_data(self):
        """
        Fetch data from all global endpoints and store the results.
        Update the available indices based on the global data.
        """
        for endpoint in self.global_endpoints:
            data = self.get_data(endpoint)
            if data:
               self.global_results[endpoint] = data
               self.update_available_indices(data)
            else:
               logger.error(f'Failed to fetch data from {endpoint}')

    def update_available_indices(self, data):
        """
        Update the list of available indices based on the provided data.
        :param data: Data from which to extract the indices.
        """
        # Aquí se debe agregar la lógica para extraer los índices de los datos
        # y agregarlos a self.available_indices. La implementación exacta
        # dependerá de cómo estén estructurados los datos.
        pass

    def get_available_indices(self):
        """
        Get the list of available indices.
        :return: List of available indices.
        """
        return self.available_indices
    def get_list_data(self,endponit):
        """
        get the all data from endponin, will be a list ok keys, or tikers, so we will be able to ask for that specific key or tiker
        """

    def get_tiker_data(self, endpoint, tiker, startTime, endtime):
        pass
