from abc import ABC, abstractmethod
import json

class O_Generic(ABC):
    def __init__(self, info):
        self.data = []
        if isinstance(info, str):  # Verifica si info es una cadena JSON
            self.info = json.loads(info)
        else:
            self.info = info  # Asumiendo que info ya es un diccionario

        self.id = self.info.get('symbol_id', None) if self.info else None

    def addData(self, data):
        for x in data:
            try:
                self.data.append(json.loads(x) if isinstance(x, str) else x)
            except json.JSONDecodeError:
                print(f"Error al decodificar JSON: {x}")

    def getID(self):
        return self.id

    def getData(self):
        return self.data

    def getInfo(self):
        return self.info

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.info.items())
