#!/home/gmorey/Downloads/Repositorios_GitHub/TP/tpfinal/bin/python

from tp_utils import *
from my_data.my_manager_objects.list_manager_symbols    import SymbolManager

class Handler:
    def __init__(self):
        # Crear un Manejador de Symbolos
        self.Smanager = SymbolManager()


    def getInfoS(self, filtro):
    #def getAllSymbols(self, filtro):
        return self.Smanager.getInfoS(filtro)
        

    def fetch_data(self, symbol_pos, start, end):
        self.Smanager.fetch_data(symbol_pos, start, end)

    def fetch_paginated_data_db(self, page, page_size, filter_text):
        return self.Smanager.fetch_paginated_data_db(page, page_size, filter_text)

    def config_getApiKey(self):
        return self.Smanager.config_getApiKey()

    def config_setApiKey(self, text):
        self.Smanager.config_setApiKey(text)

