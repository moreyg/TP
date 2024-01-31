class DosTable():

    def __init__(self):
        self.symbolos = []
        self.encabezado = ["Eje X"]
        self.eje_x = []
        self.valores_y = []
        self.data = {}

    def addSymbol(self, o):
        if o not in self.symbolos:
            self.symbolos.append(o)

    def remSymbol(self, o):
        if o not in self.symbolos:
            return
        else:
            if o.id in self.encabezado:
                self.encabezado.remove(o.id)
            self.symbolos.remove(o)

    def _encabezado(self):
        for o in self.symbolos:
            if o.id not in self.encabezado:
                self.encabezado.append(o.id)
        # Imprimir encabezados de la tabla
        encabezados_str = (" | ".join(self.encabezado))
        print(encabezados_str)
        # Imprimir separador
        print("-" * len(encabezados_str))

    def _eje_x(self):
        for o in self.symbolos:
           for registro in o.data.data:
                if registro.time_period_start not in self.eje_x:
                    self.eje_x.append(registro.time_period_start)
        self.eje_x.sort()

    def _data_y(self):
        self.valores_y.clear()
        for o in self.symbolos:
            v = o.getValores(self.eje_x)
            self.valores_y.append(v)

    def printTabla(self):
        self._encabezado()
        self._eje_x()
        self._data_y()
        # Aplicar la transformación utilizando zip() para tener en cada lista los valores que corresponden al eje de tiempo de todos los symbolos
        resultado = [list(x) for x in zip(*self.valores_y)]
        #Hago un diccionario donde k es el valor del tiempo eje x y le corresponde cada lista generada en la transformacion anterior
        diccionario_resultante = dict(zip(self.eje_x, resultado))
        for k,v in diccionario_resultante.items():
            valores_formateados = [str(x) for x in v]  # Convierte todos los valores a strings
            valores_juntos = "\t|  ".join(valores_formateados)
            print(f'{k} | {valores_juntos}')

