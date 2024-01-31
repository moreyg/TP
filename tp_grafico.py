from datetime import datetime
import matplotlib.pyplot as plt

class DynamicPlotApp():

    def __init__(self):
        super().__init__()
        self.symbolos = []
        self.eje_x = []
        self.valores_y = []
        self.data = {}
        self.lines = {}  
        self.buttons = {}

    def addSymbol(self, o):
        if o not in self.symbolos:
            self.symbolos.append(o)

    def remSymbol(self, o):
        if o not in self.symbolos:
            return
        else:
            self.symbolos.remove(o)
            
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

    def showGrafico(self):
        self._eje_x()
        self._data_y()
        i= 0
        for y in self.valores_y:
            self.addLine(self.eje_x, y, self.symbolos[i].id)
            i=i+1

    def addLine(self, x_data, y_data, _id):
        x1 = [datetime.fromisoformat(fecha[:10]) for fecha in x_data]
        y  = [float(valor) for valor in y_data]
        x_data_iso = [fecha.strftime("%Y-%m-%d") for fecha in x1]
        self.graficar(x_data_iso,y,_id)

    def graficar(self, x, y,_id):
        plt.figure(figsize=(10, 6))  # Tamaño de la figura
        plt.plot(x, y, marker='o', linestyle='-', color='b', label=_id)  # Crear el gráfico de líneas
        plt.xlabel('Fechas')  # Etiqueta del eje x
        plt.ylabel('Valores')  # Etiqueta del eje y
        plt.title('Gráfico de Datos')  # Título del gráfico
        plt.grid(True)  # Habilitar la cuadrícula en el gráfico
        plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mayor legibilidad
        plt.tight_layout()  # Ajustar el diseño de la figura
        plt.legend()  # Mostrar la leyenda
        # Mostrar el gráfico en pantalla
        plt.show()
