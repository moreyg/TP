#!/home/gmorey/Downloads/Repositorios_GitHub/TP/tpfinal/bin/python

from my_data.my_manager_objects.list_manager_symbols    import SymbolManager

class Handler:
    def __init__(self):
        # Crear un Manejador de Symbolos
        self.Smanager = SymbolManager()

    def start(self):
        return self.Smanager.start()

    def getInfoS(self, filtro):
        """
    Esta es una función que solicita el pedido de los SYMBOLS que coinciden con el filtro.
    Si no hay filtro, "" , un str vacio, se traen todos los SIMBOLS.
    Si el str no es vacio: "HALGO", se traen los SYMBOLS que tienen este str en el nombre 

    Se agrego esta funcion ya que traer los mas de 500000 SYMBOLS tarda mas de tres horas el proceso completo
    que necesita el sistema ya que recibe todo en una sola pagina y luego recorre cada registro recibido y lo 
    impacta en la base de datos.

    Al agregar un filtro podemos acotar el tamaño de la respuesta de la API y trabajar sobre esos simbolos.

    """
        return self.Smanager.getInfoS(filtro)
        

    def fetch_symbol(self, symbol_pos):
        return self.Smanager.fetch_symbol(symbol_pos)

    def fetch_data(self, symbol_pos, start, end, interval, limit='24'):
        return self.Smanager.simbol_data(symbol_pos, start, end, interval, limit)
        '''
            self.Smanager.fetch_data(symbol_pos, start, end, interval, limit)
            return #fin, sino sigo
        if not (self.Smanager.simbol_has_data_from_start(symbol_pos, start, end, interval, limit)):
            self.Smanager.fetch_data(symbol_pos, start, end, interval, limit)
        if not (self.Smanager.simbol_has_data_until_end(symbol_pos, start, end, interval, limit)):
            self.Smanager.fetch_data(symbol_pos, start, end, interval, limit)
        '''
    def fetch_paginated_data_db(self, page, page_size, filter_text):
        return self.Smanager.fetch_paginated_data_db(page, page_size, filter_text)

    def config_getApiKey(self):
        return self.Smanager.config_getApiKey()

    def config_setApiKey(self, text):
        self.Smanager.config_setApiKey(text)

