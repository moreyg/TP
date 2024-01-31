from abc import ABC, abstractmethod
from .data import DATA
import json

class O_Generic(ABC):
    def __init__(self, _info, _id=None):
        '''
    def __init__(self, _info, _id=None):
        self.data =Data() 
        self.info = _info
        if (_id!=None):
            self.id = _id
        else:
        '''
        self.data = DATA()
        self.info = _info
        self.id = _id

    def addData(self, data):
        pass

    def getID(self):
        return self.id

    def getValores(self, eje_x):
        _return = []
        for x in eje_x:
            _return.append(self.getPriceEnd(x))
        return _return

    def getPriceEnd(self,x):
        _return ="0"
        for r in self.data.data:
            t = r.time_period_start
            if t == x :
                _return=r.price_close 
        return _return

    def getData(self):
        return self.data

    def setData(self, x):
        self.data=x

    def getInfo(self):
        return self.info

    def getLen(self):
        return self.data.getLen()

    def getFirstData(self):
        return self.data.getFirstData()

    def getLastData(self):
        return self.data.getLastData()

    def has_data(self):
        return self.data.has_data()
    '''
    def __str__(self):
        valid_items = [(k, v) for k, v in self.info.items() if isinstance(v, str)]
        return "\n".join(f"{k}: {v}" for k, v in valid_items)
    '''

    def __eq__(self, otro):
        if isinstance(otro, O_Generic):
            return self.id == otro.id
        return False
