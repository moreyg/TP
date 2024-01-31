from .list_manager_object import GenericManager
from ..my_objects.o_symbol import O_Symbol
from ..my_objects.data import DATA
from ..my_database.my_sqlite.sqlite_handler import SQLiteHandler
import os
import json
import datetime

class SymbolManager(GenericManager):

    def __init__(self):
        super().__init__()
        self.has_old_data = False
        self.db_path = "./db"
        self.db = "./db/db_symbols"
        self.tabla="symbols"
        self.columns_to_create='id TEXT PRIMARY KEY, info TEXT, data TEXT'
        self.columns='id, info'
        self.db_handler = SQLiteHandler(self.db, self.tabla, self.columns_to_create, self.columns)
        count = self.db_handler.count_records('symbols')
        if count >=1 :
            self.has_old_data = True

    def check_infraesurcuta_DB_Symbols(self):
        try:
             if not os.path.exists(self.db_path):
                 os.makedirs(directory_path)
                 return True
             if os.path.exists(self.db_path) and not os.path.isdir(self.db_path):
                 print ("error en infraestructura, ./db debe ser un directorio")
                 return False
             if not os.path.exists(self.db):
                 return True
             if os.path.exists(self.db) and os.path.isdir(self.db):
                 print ("error en infraestructura, ./db_symbols debe no ser un directorio")
                 return False
             file_stats = os.stat(self.db)
             if file_stats.st_size == 0:
               return True
             return True
        except Exception as e:
            print(f"Error al verificar la infraestructura necesaria: {e}")
            return False

    def load_items(self, items_data):
        """
        Método abstracto para cargar datos en la lista interna.
        Este método debe ser implementado por cada subclase.
        """
        pass

    def fetch_symbol(self, symbol_pos):
        return self.items[int(symbol_pos)]

    def fetch_data(self, symbol_pos , start, end, interval, limit='12'):
        """
        Método abstracto para obtener datos desde una fuente externa.
        Este método debe ser implementado por cada subclase.
        """
        s= self.items[int(symbol_pos)]
        x = self.api_instance.getDataS(s.getID(), start, end,interval,limit)
        s.addData(x) #ACA TENGO Q IMPEDIR DUPLICADOS, INTENTO NO PEDIR DATA QUE YA TENGO
        d = s.getData()
        data_to_save = d.to_dict()  # Obtener el contenido
        new_data = json.dumps(data_to_save)  # Convertir a JSON
        self.db_handler.insertSymbolData(s.id,new_data)


    def simbol_data(self, symbol_pos, start, end, interval, limit):
        r = None
        symbol_obj = self.items[int(symbol_pos)]
        #print(symbol_obj.getLen())
        if not symbol_obj.has_data():
            #print("1 DATA VACIO")
            r = self.db_handler.symbol_get_data(symbol_obj.getID())
            if r is not None:
                x = DATA.from_dict(json.loads(r))
                symbol_obj.setData(x)
                #print(f"2 {symbol_obj.getLen()}")
                #print("2 SE PUSO LA MISMA DATA DE TABLA AL OBJETO")
                #print("FALTA COMPARAR DATA PEDIDA CON EXSITENTE PARA PEDIR LO QUE NO ESTA EN TABLA")
                #print(f"Datos en memoria : {symbol_obj.getLen()}")
                #symbol_obj.getData().check_startdate(start)
                #symbol_obj.getData().check_enddate(end)
                #OPTIMIZAR EL PEDIDO A LO FALTANTE SEGUN RESULTADOS
                #DE LOS CHEQUEOS ANTERIORES DE FECHA START Y FECHA END
                #ACA !! self.fetch_data(symbol_pos , start, end, interval, limit)
                return symbol_obj
            else:
                self.fetch_data(symbol_pos , start, end, interval, limit)
                #print("3 SE PIDIO A LA API lo pedido")
                #print(f"3 {symbol_obj.getLen()}")
                return symbol_obj
        else:
            #print("4 O_Symbol con DATA")
            symbol_obj.getData().check_startdate(start)
            symbol_obj.getData().check_enddate(end)
            #OPTIMIZAR EL PEDIDO A LO FALTANTE SEGUN RESULTADOS
            #DE LOS CHEQUEOS ANTERIORES DE FECHA START Y FECHA END
            self.fetch_data(symbol_pos , start, end, interval, limit)
        #print("NO SE AGREGAN REGISTROS DUPLICADOS SEGUN FUNCIONALIDAD EN DATA Y EN REGISTRO")
        return symbol_obj


    def load_initial_data(self):
        '''
    def load_initial_data(self):
        data = self.db_handler.fetch_data(self.tabla, self.columns)
        for x in data:
            print(data)
            break
        '''
        data = self.db_handler.fetch_data(self.tabla, self.columns)
        self.items = [O_Symbol(_valor, _id) for _id, _valor in data]
        d = {symbol.getID(): index for index, symbol in enumerate(self.items)}
        return d

    def getInfoS(self, filtro):
        """
        Solicita a la API todos los símbolos, segun el filtro, y carga la lista interna.
        Que pasa a la db SQL para descargar memoria y lograr persistencia
        """
        fha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #PREGUNTA Y RESPUESTA
        #print(f'{fha}        #PREGUNTA Y RESPUESTA')
        symbols_info = self.api_instance.getInfoS(filtro)
        #ARMO LISTA DESDE RESPUESTA
        fha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(f'{fha}       #ARMO LISTA DESDE RESPUESTA')
        objetos_via_api = [O_Symbol(json.dumps(info),info['symbol_id']) for info in symbols_info]
        #print(f'{fha}       #ARMADA! LISTA DESDE RESPUESTA')
        #AGREGAR A LA DB LOS NUEVOS DATOS QUE VIENEN DE LA  CONSULTA VIA API, NO LOS ACTUALIZA OJO !!!
        fha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(f'{fha}        #AGREGAR A LA DB LOS NUEVOS OBJETOS QUE VIENEN DE LA  CONSULTA VIA API, NO LOS ACTUALIZA OJO !!!')
        self.db_handler.add_items_to_db(objetos_via_api)
        #print(f'{fha}        #AGREGADO!! A LA DB LOS NUEVOS OBJETOS QUE VIENEN DE LA  CONSULTA VIA API, NO LOS ACTUALIZA OJO !!!')
        #AGREGAR A SELF.ITEMS LOS NUEVOS
        fha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(f'{fha}        #AGREGAR A SELF.ITEMS LOS NUEVOS OBJETOS DE LA RESPUESTA DE LA API')
        if not isinstance(self.items, set):
           self.items = set(self.items)
        # Agrega objetos al conjunto self.items
        for x in objetos_via_api:
            self.items.add(x)
        fha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(f'{fha}        #FIN !! AGREGAR A SELF.ITEMS LOS NUEVOS OBJETOS DE LA RESPUESTA DE LA API')
        if isinstance(self.items, set):
            self.items = list(self.items)

        #PREPARO EL NUEVO DICCIONARIO PARA  LA GUI
        #print(f'{fha} largo de self.items = {len(self.items)}')
        fha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(f'{fha}        #PREPARO EL NUEVO DICCIONARIO PARA  LA GUI')
        d = {symbol.getID(): index for index, symbol in enumerate(self.items)}
        fha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(f'{fha}        #FIN!!!')
        return d

    def __repr__(self):
        return f"SymbolManager(api_key={self.api_instance} vacio ={self.is_empty()})"

    def __str__(self):
        return f"SymbolManager(api_key={self.api_instance} vacio ={self.is_empty()})"


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



