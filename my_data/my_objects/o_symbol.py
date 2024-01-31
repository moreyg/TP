from .o_generic import O_Generic
from .registro import REGISTRO
from .data import DATA
import json

class O_Symbol(O_Generic):


    def addData(self, respuesta):
        for x in respuesta:
            try:
                r = REGISTRO(x)
                self.data.addData(r)#ESTA FUNCION DE DATA VERIFICA REGISTROS DUPLICADOS 
            except json.JSONDecodeError:
                print(f"Error al decodificar JSON: {x}")

    def some_abstract_method(self):
        # Implementación específica para O_Symbol
        pass

    def __eq__(self, otro):
        if isinstance(otro, O_Symbol):
            return self.id == otro.id and self.info == otro.info
        return False

    def __hash__(self):
        return hash((self.id, self.info))
