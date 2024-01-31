from abc import ABC, abstractmethod
from ..my_database.my_sqlite.sqlite_handler import SQLiteHandler
from ..my_requests.coinApi import COIN_API

class GenericManager(ABC):
    def __init__(self):
        self.items = []
        self.has_old_data = False
        self.db_path = ""
        self.db = ""
        self.tabla = ""
        self.api_instance = COIN_API()
        self.items_db =''
        self.items_db_dir =''
        self.items_db_table =''
        self.db_handler = None 
        self.columns_to_create= None
        self.columns= None

    def config_getApiKey(self):
        return self.api_instance.config_getApiKey()

    def config_setApiKey(self, text):
        return self.api_instance.config_setApiKey(text)

    @abstractmethod
    def load_items(self, items_data):
        """
        Método abstracto para cargar datos en la lista interna.
        Este método debe ser implementado por cada subclase.
        """
        pass

    def is_empty(self):
        """
        Verifica si la lista interna está vacía.
        """
        return len(self.items) == 0

    def clear_items(self):
        """
        Borra la lista interna.
        """
        self.items = []

    def fetch_data(self):
        self.db_handler.fetch_data
    def getIDs(self):
        """
        Retorna los IDs de la lista como lista
        """
        return [(o.getID()) for o in self.items]


    def cantidad(self):
        """
        Retorna la cantidad de Items de la lista
        """
        return len(self.items)

    def __repr__(self):
        return f"GenericManager(api_key={self.api_instance} vacio ={self.is_empty})"

    def __str__(self):
        return f"GebericManager(api_key={self.api_instance} vacio ={self.is_empty})"

#    FUNCIONDES DE SQL

    @abstractmethod
    def cantidad_db(self):
        """
        Retorna la cantidad de Items de la db
        """
        pass

    @abstractmethod
    def fetch_paginated_data_db(self, generics, generic, page, page_size, filter_text):
        '''
        Obtener indices paginados desde la DB
        '''
        pass
