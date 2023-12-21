from .list_manager_object import GenericManager
from ..my_objects.o_symbol import O_Symbol
from ..my_database.my_sqlite.sqlite_handler import SQLiteHandler

class SymbolManager(GenericManager):

    def __init__(self):
        super().__init__()
        self.db_handler = SQLiteHandler('./db_symbols')
        self.db_handler.create_table("symbols", "id INTEGER PRIMARY KEY, symbol TEXT, info TEXT, data TEXT")

    def load_items(self, items_data):
        """
        Método abstracto para cargar datos en la lista interna.
        Este método debe ser implementado por cada subclase.
        """
        pass

    def fetch_data(self, symbol_pos , start, end, limit='100'):
        """
        Método abstracto para obtener datos desde una fuente externa.
        Este método debe ser implementado por cada subclase.
        """
        s = self.items[int(symbol_pos)]
        x = self.api_instance.getDataS(s.getID(), start, end)
        s.addData(x) 

    def getInfoS(self, filtro):
        """
        Solicita a la API todos los símbolos y carga la lista interna.
        Que pasa a la db SQL para descargar memoria y lograr persistencia
        """
        symbols_info = self.api_instance.getInfoS(filtro)
        self.items = [O_Symbol(info) for info in symbols_info]
        self.add_ids_to_db(self.items)
        d = {symbol.getID(): index for index, symbol in enumerate(self.items)}
        return d

    def __repr__(self):
        return f"SymbolManager(api_key={self.api_instance} vacio ={self.is_empty()})"

    def __str__(self):
        return f"SymbolManager(api_key={self.api_instance} vacio ={self.is_empty()})"

    def add_ids_to_db(self, lista_id):
        for symbol in lista_id:
            self.db_handler.insert_data("symbols", "symbol", (symbol,))

    def cantidad_db(self):
        return self.db_handler.count_records("symbols")

    def fetch_paginated_data_db(self, page, page_size, filter_text):
        '''
        Obtener indices paginados desde la DB
        '''
        return self.db_handler.fetch_paginated_data_db("symbols", "symbol", page, page_size, filter_text)

    def save_to_db(self):
        for symbol in self.items:
            info_json = json.dumps(symbol.info)
            data_json = json.dumps(symbol.data)
            # Insertar o actualizar en la base de datos
            self.db_handler.insert_or_update(symbol.id, info_json, data_json)

    def load_from_db(self):
        self.items = []
        rows = self.db_handler.fetch_all()
        for row in rows:
            symbol = O_Symbol(json.loads(row['info']))
            symbol.set_data(json.loads(row['data']))
            self.items.append(symbol)



