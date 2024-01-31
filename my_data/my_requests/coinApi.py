import logging
import sys
import requests

# Get the logger
logger = logging.getLogger('my_tp_app')

# Use the logger
logger.info('Mensaje de request_class.py')

class COIN_API():

    def __init__(self):
        self.url_symbols = "https://rest.coinapi.io/v1/symbols"
        try:
            with open('apikey', 'r') as file:
                dato = file.read()
                self.api_key=dato
                self.headers = {                           
                    'Accept': 'text/json',
                    'X-CoinAPI-Key': self.api_key
                }
        except FileNotFoundError:
            self.api_key  = 'PEGUE AQUI LA CLAVE RECIBIDA EN SU CORREO'
            self.headers = None

    def config_getApiKey(self):
        return self.api_key

    def config_setApiKey(self, newKey):
        with open('apikey', 'w') as file:
            file.write(newKey)
        self.api_key=newKey
        self.headers = {                           
           'Accept': 'text/json',
           'X-CoinAPI-Key': self.api_key
           }

    def getInfoS(self, filtro="BINANCE_SPOT_B"): 
        self.checkApiKey()
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
             

    def getDataS(self, symbol, stime, etime, interval, limit): 
        self.checkApiKey()
        resultado= None
        url = f'https://rest.coinapi.io/v1/ohlcv/{symbol}/history?period_id={interval}&time_start={stime}&time_end={etime}&limit={limit}'
        payload={}
        headers = self.headers
        resultado = self.my_request(url, headers, payload)
        return resultado    

    def my_request(self, url, headers, payload):
        self.checkApiKey()
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            #print(response.headers)
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
        self.checkApiKey()
        self.testing_quotes()




    def testing_quotes(self):
        self.checkApiKey()
        url = "https://rest.coinapi.io/v1/quotes/BINANCE_SPOT_BTC_USDT/history?time_start=2023-01-02&time_end=2023-07-16"
        payload={}
        headers = {
            'Accept': 'text/plain',
            'X-CoinAPI-Key': '4B82844F-2761-494A-A92F-DC0C8EB93910'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        #print(response.text)
        #print(f'Headers: {response.headers}')
        return response

    def getAllDataFilter(self, fs="BINANCE_SPOT_B"):
        self.checkApiKey()
        # url = "https://rest.coinapi.io/v1/symbols?filter_symbol_id=BINANCE_SPOT_B"
        url = f"{self.url}?filter_symbol_id={fs}"
        payload={}
        headers = self.headers
        response = requests.request("GET", url, headers=headers, data=payload)
        r = response.json()  # Return the JSON response En funcion de quien lo pida como trabajo la respuesta.
        #print(f'CoinApi_get_Data() {type(r)}')
        #print(f'CoinApi_get_Data() {len(r)}')
        return r

    def getAllData(self):
        self.checkApiKey()
        pass

    def fetch_global_data(self):
        self.checkApiKey()
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
        self.checkApiKey()
        """
        Update the list of available indices based on the provided data.
        :param data: Data from which to extract the indices.
        """
        # Aquí se debe agregar la lógica para extraer los índices de los datos
        # y agregarlos a self.available_indices. La implementación exacta
        # dependerá de cómo estén estructurados los datos.
        pass

    def get_available_indices(self):
        self.checkApiKey()
        """
        Get the list of available indices.
        :return: List of available indices.
        """
        return self.available_indices
    def get_list_data(self,endponit):
        self.checkApiKey()
        """
        get the all data from endponin, will be a list ok keys, or tikers, so we will be able to ask for that specific key or tiker
        """

    def get_tiker_data(self, endpoint, tiker, startTime, endtime):
        self.checkApiKey()
        pass
    
    def checkApiKey(self):
        if self.headers == None:
            print("No configuro la API-KEY en menu File")
            print("Solicitela gratis a https://docs.coinapi.io/market-data/rest-api/")
            print("Una vez que la reciba en el correo, inicie el sistema y via menu File configurela")
            print("Una vez configurada el sistema la recordara")
            sys.exit(1)
