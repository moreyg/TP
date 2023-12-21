#!/home/gmorey/Downloads/Repositorios_GitHub/TP/tpfinal/bin/python
# main.py

from PyQt5.QtWidgets import QApplication
from tp_gui import CoinApiGUI
from tp_Handler   import Handler    # Importa tu clase CoinApi
import sys

def main():
    app = QApplication(sys.argv)

    handler  = Handler()    # Crea una instancia de tu backend CoinApi

    gui = CoinApiGUI(handler)            # Pasa el backend a la GUI
    gui.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
