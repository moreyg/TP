import json
from .registro import REGISTRO
from sortedcontainers import SortedSet


class DATA():
    def __init__(self):
        self.data = SortedSet()  # Usamos OrderedSet en lugar de set para mantener el orden

    def to_dict(self):
        data_list = [registro.to_dict() for registro in self.data]
        return {'data': data_list}

    @classmethod
    def from_dict(cls, data_dict):
        data = DATA()
        for registro_data in data_dict['data']:
            registro = REGISTRO.from_dict(registro_data)
            data.addData(registro)
        return data

    def clearData(self):
        self.data = SortedSet()

    def addData(self, registro):
        if registro in self.data:
            #print(f"-- NO AGREGO {registro.getItem()}")
            return
        else:
            #print(f"++ SI  AGREGO {registro.getItem()}")
            self.data.add(registro)  # Agregamos el registro al OrderedSet

    def getLen(self):
        return (len(self.data))  # Devolvemos lista del conjunto ordenado

    def getFirstData(self):
        return self.data[0]  # Devolvemos lista del conjunto ordenado

    def getLastData(self):
        return self.data[-1]  # Devolvemos lista del conjunto ordenado

    def __str__(self):
        # Crear una cadena con representaciones de los registros
        registros_str = "\n".join(str(registro) for registro in self.data)
        return f"DATA:\n{registros_str}"

    def has_data(self):
        if self.getLen() != 0:
            return True
        else:
            return False

    def check_startdate(self,start):
        r = self.data[0]
        if (start  < r.getItem()):
            pass
           #print(f"API FROM {start} to {r.getItem()}")
        else:
            pass
            #print("+DB+")


    def check_enddate(self, end):
        r = self.data[-1]
        if (r.getItem() < end):
            pass
            #print(f"API FROM {r.getItem()} to {end}")
        else:
            pass
            #print("+DB+")
