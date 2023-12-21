# sqlite_handler.py

import sqlite3

class SQLiteHandler:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_table(self, table_name, columns):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        conn.commit()
        conn.close()

    def insert_data(self, table_name, columns, objects):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Asume que 'columns' es una cadena con un único nombre de columna para simplificar.
        # Si necesitas insertar en múltiples columnas, deberás ajustar esto.
        placeholders = '?'

        # Convertir la lista de objetos en una lista de tuplas conteniendo los IDs
        data_tuples = [(obj.id,) for obj in objects]

        for row in data_tuples:
            cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", row)

        conn.commit()
        conn.close()

    def delete_data(self, table_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
        conn.close()

    def fetch_data(self, table_name, columns):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT {columns} FROM {table_name}")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def count_records(self, table_name):
        """
        Cuenta el número de registros en una tabla dada.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM {table_name}"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def fetch_paginated_data_db(self, table_name, column, page, page_size, filter_text=''):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        offset = page * page_size
        query = f"""
            SELECT {column} FROM {table_name}
            WHERE {column} LIKE ?
            LIMIT ? OFFSET ?
        """
        cursor.execute(query, (f'%{filter_text}%', page_size, offset))
        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]
