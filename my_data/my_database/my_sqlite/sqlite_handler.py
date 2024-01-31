# sqlite_handler.py

import sqlite3
import json
import datetime

class SQLiteHandler:
    def __init__(self, db, table,columns_to_create, columns):
        self.db               = db
        self.table            = table
        self.columns          = columns
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        #SE CREA LA TABLA SI NO EXISTE!!, SI EXISTE EL NOMBRE NO LA CREA. SETEA VALORES PARA OTRAS FUNCIONES!
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table} ({columns_to_create})")
        '''
        ver si existe la tabla con otros columnas
        '''
        conn.commit()
        conn.close()

    def add_items_to_db(self, items):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        for item in items:
           # Verificar si un registro con la misma clave primaria ya existe
           cursor.execute(f"SELECT COUNT(*) FROM {self.table} WHERE id=?", (item.id,))
           exists = cursor.fetchone()[0] > 0
           if not exists:
               cursor.execute(f"INSERT INTO {self.table} ({self.columns}) VALUES ('{item.id}','{item.info}')")
        conn.commit()
        conn.close()

    def insertSymbolData(self, _id, _data):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("UPDATE symbols SET data = ? WHERE id = ?", (_data, _id))
        conn.commit()
        conn.close()

    def symbol_has_data(self,_id):
        _return = ''
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT data FROM symbols WHERE id = ?", (_id,))
        resultado = cursor.fetchone()
        if resultado is not None:
            _return = resultado[0]
        conn.commit()
        conn.close()
        return _return

    def symbol_get_data(self, _id):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT data FROM symbols WHERE id = ?", (_id,))
        resultado = cursor.fetchone()
        conn.commit()
        conn.close()
        return resultado[0]

    def delete_data(self, table):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table}")
        conn.commit()
        conn.close()

    def fetch_data(self, table, columns):
        '''
           def fetch_data(self, table, columns):
                conn = sqlite3.connect(self.db)
                cursor = conn.cursor()
                cursor.execute(f"SELECT {columns} FROM {table}")
                rows = cursor.fetchall()
                conn.close()
                return rows
        '''
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(f"SELECT {columns} FROM {table}")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def count_records(self, table):
        """
        Cuenta el número de registros en una tabla dada.
        """
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM {table}"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def fetch_paginated_data_db(self, table, column, page, page_size, filter_text=''):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        offset = page * page_size
        query = f"""
            SELECT {column} FROM {table}
            WHERE {column} LIKE ?
            LIMIT ? OFFSET ?
        """
        cursor.execute(query, (f'%{filter_text}%', page_size, offset))
        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]
