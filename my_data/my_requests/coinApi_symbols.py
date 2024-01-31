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
        #print(f'CoinApi_get_Data() {type(r)}')
        #print(f'CoinApi_get_Data() {len(r)}')
        return r

