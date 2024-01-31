import json

class REGISTRO():
    def __init__(self, data):
        self.time_period_start = data['time_period_start']
        self.time_period_end = data['time_period_end']
        self.time_open = data['time_open']
        self.time_close = data['time_close']
        self.price_open = data['price_open']
        self.price_high = data['price_high']
        self.price_low = data['price_low']
        self.price_close = data['price_close']
        self.volume_traded = data['volume_traded']
        self.trades_count = data['trades_count']

    def getItem(self, key='time_period_start'):
        return getattr(self, key, None)

    def to_dict(self):
        # Convierte los atributos en un diccionario
        return self.__dict__

    def __lt__(self, other):
        return self.time_period_start < other.time_period_start

    def __le__(self, other):
        return self.time_period_start <= other.time_period_start

    def __gt__(self, other):
        return self.time_period_start > other.time_period_start

    def __ge__(self, other):
        return self.time_period_start >= other.time_period_start

    def __eq__(self, other):
        if isinstance(other, REGISTRO):
            return self.time_period_start == other.time_period_start
        return False

    def __str__(self):
        # Personaliza la representación de REGISTRO
        if not self.time_period_start == None:
            return f"{self.time_period_start}"
        else:
            return (" Sin Datos ")

    def __hash__(self):
        return hash((self.time_period_start,))

    @classmethod
    def from_dict(cls, data_dict):
        # Crea una instancia de REGISTRO desde un diccionario
        return cls(data_dict)
