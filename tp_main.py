#!/home/gmorey/Downloads/Repositorios_GitHub/TP/tpfinal/bin/python
# main.py

from PyQt5.QtWidgets import QApplication
from tp_gui import CoinApiGUI
from tp_Handler   import Handler    # Importa tu clase CoinApi
import sys

def main():
    app = QApplication(sys.argv)
    handler  = Handler()    # Crea una instancia de tu backend CoinApi
    #Verifica la infraestructura
    if not handler.Smanager.check_infraesurcuta_DB_Symbols():
        sys.exit(1)

    #Iniciamos el systema
    gui = CoinApiGUI(handler)            # Pasa el backend a la GUI
    if (handler.Smanager.has_old_data):
        #print(' + CON DATA EXIXTENTE')
        d=handler.Smanager.load_initial_data()
        gui.start(d)
    else:
        pass
        #print(' - NO HAY DATA EXISTENTE')
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
