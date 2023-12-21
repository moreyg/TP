#Implementa el pedido simple de informacion

from .requests_class import APIRequestHandler

class COIN_API_SYMBOLS(APIRequestHandler):

    def __init__(self, api_key, base_url, global_endpoints):
        super().__init__(api_key, base_url, global_endpoints)
        # Puedes agregar inicializaciones específicas de CoinApi aquí

    def update_available_indices(self, endpoint):
        # Implementación específica para procesar datos de CoinApi
        # Por ejemplo, procesar y almacenar información de monedas
        url = f'{self.base_url}/{endpoint}/'
        headers = {                           
           'X-CoinAPI-Key': self.api_key,
           'Accept': 'application/json'
           }
        data = self.get_data(url,headers)
        for coin_data in data:
            ticker = Ticker(endpoint, coin_data['name'], coin_data['description'])
            self.available_indices.append(ticker)

    def fetch_coin_data(self, coin_id):
        # Método específico para obtener datos de una moneda específica
        # Aquí puedes construir la URL específica y realizar la solicitud
        pass

    # Otros métodos específicos de CoinApi

