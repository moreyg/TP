import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMessageBox, QInputDialog, QComboBox, QDialog, QLabel, QVBoxLayout, QDateEdit, QTabWidget, QLineEdit
from PyQt5.QtCore import Qt, QDateTime, QDate, QSettings
from plot_shower_class import PlotShower
from tp_Handler   import Handler
from collections.abc import Iterable

class CoinApiGUI(QMainWindow):
    def __init__(self, handler):
        super(CoinApiGUI, self).__init__()
        
        # Variables to store timeStart and timeEnd

        #Este dict es {"symbol_id":poss_en_lista_de_objetos_O_Symbols}
        self.index_to_symbol_map = {}

        self.handler  = handler
        self.page = 0
        self.page_size = 20
        self.current_filter_text = ''
        self.selected_symbol = None  # Atributo para almacenar el símbolo seleccionado
        self.boolean_symbol_start_date_selected = False
        self.boolean_symbol_end_date_selected   = False
        self.boolean_symbol_interval_selected   = False
        self.boolean_symbol_id_selected         = False


        # Create actions
        start_action = QAction('Start', self)
        start_action.triggered.connect(self.start)

        ask_for_key_action = QAction('Set_API_Key', self)
        ask_for_key_action.triggered.connect(self.ask_for_key)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.confirm_exit)

        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about_dialog)

        # Create QSettings instance
        self.settings = QSettings("GMSoluciones", "gmorey")#PREGUNTAR EN INICIALIZACION
        self.setGeometry(300,300,300,200)
        #self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "YourOrganization", "YourAppName")
        #self.settings.setPath(QSettings.IniFormat, QSettings.UserScope, "/path/to/custom/location")

        # Restore saved dates or set defaults
        time_start_str = self.settings.value("time_start")
        time_end_str = self.settings.value("time_end")

        if time_start_str is not None:
            self.time_start = QDate.fromString(time_start_str, Qt.ISODate)
        else:
            self.time_start = QDate.currentDate()

        if time_end_str is not None:
            self.time_end = QDate.fromString(time_end_str, Qt.ISODate)
        else:
            self.time_end = QDate.currentDate()

        # Create toolbar
        toolbar = QToolBar('Main Toolbar', self)
        toolbar.addAction(start_action)
        toolbar.addAction(exit_action)
        toolbar.addAction(about_action)
        self.addToolBar(toolbar)
        toolbar.setVisible(False)

        # Create central widget
        #central_widget = QWidget(self)
        #label = QLabel('Main Window Content', central_widget)
        #label.setAlignment(Qt.AlignCenter)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        label = QLabel('Main Window Content')
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Crear el QTabWidget
        tab_widget    = QTabWidget()
        # Crear las pestañas
        tab_symbols   = QWidget()
        tab_exchanges = QWidget()
        tab_assets    = QWidget()
        # Agregar las pestañas al QTabWidget
        tab_widget.addTab(tab_symbols, "Symbols")
        tab_widget.addTab(tab_exchanges, "Exchanges")
        tab_widget.addTab(tab_assets, "Assets")
        # Establecer el QTabWidget como el widget central
        self.setCentralWidget(tab_widget)

        # Configurar cada pestaña
        self.configurarTabSymbols(tab_symbols)
        self.configurarTabExchanges(tab_exchanges)
        self.configurarTabAssets(tab_assets)

        # Set window properties
        self.setWindowTitle('Main Window Example')
        self.setGeometry(100, 100, 800, 600)

        # Log the start times and end times
        self.log_message(f'Start Time: {self.time_start.toString(Qt.ISODate)}')
        self.log_message(f'End Time: {self.time_end.toString(Qt.ISODate)}')

        # Create menu bar
        menu_bar = self.menuBar()

        # Crear un menú de archivo
        file_menu = menu_bar.addMenu('File')

        # Agregar acciones al menú de archivo
        file_menu.addAction(start_action)
        file_menu.addAction(ask_for_key_action)
        file_menu.addAction(exit_action)

        # Crear un menú de ayuda
        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction(about_action)

    def configurarTabSymbols(self, tab):
        layout = QVBoxLayout()
        # Campo de texto para filtrado
        self.filter_line_edit = QLineEdit('Escribir symbol para filtrado')
        self.filter_line_edit.textChanged.connect(self.apply_filter)
        layout.addWidget(self.filter_line_edit)
        # Botones para getAllSymbols
        self.update_symbols_button = QPushButton("Get Symbols Info")
        self.update_symbols_button.clicked.connect(self.ask_for_filter)
        layout.addWidget(self.update_symbols_button)
        # Botones para paginación
        self.prev_page_button = QPushButton("Página Anterior")
        self.prev_page_button.clicked.connect(self.load_prev_page)
        layout.addWidget(self.prev_page_button)

        self.next_page_button = QPushButton("Siguiente Página")
        self.next_page_button.clicked.connect(self.load_next_page)
        layout.addWidget(self.next_page_button)

        # Botón para solicitar información (inicialmente deshabilitado)
        self.request_info_button = QPushButton("Solicitar Data de Symbol Elegido", self)
        self.request_info_button.setEnabled(False)  # Inicialmente deshabilitado
        self.request_info_button.clicked.connect(self.on_request_data)
        layout.addWidget(self.request_info_button)

        # QDateEdit para la fecha de inicio
        self.start_date_edit = QDateEdit(self)
        self.start_date_edit.setDisplayFormat("yyyy-MM-dd")  # Formato ISO
        self.start_date_edit.setDate(QDate(2023, 1, 1))  # Establece la fecha inicial
        self.start_date_edit.setCalendarPopup(True)  # Activa el calendario desplegable
        self.start_date_edit.dateChanged.connect(self.on_fecha_inicio_changed)
        layout.addWidget(QLabel("Fecha de Inicio:"))
        layout.addWidget(self.start_date_edit)

        # QDateEdit para la fecha de fin
        self.end_date_edit = QDateEdit(self)
        self.end_date_edit.setDisplayFormat("yyyy-MM-dd")  # Formato ISO
        self.end_date_edit.setDate(QDate.currentDate())  # Establece la fecha a la actual
        self.end_date_edit.setCalendarPopup(True)  # Activa el calendario desplegable
        self.end_date_edit.dateChanged.connect(self.on_fecha_fin_changed)
        layout.addWidget(QLabel("Fecha de Fin:"))
        layout.addWidget(self.end_date_edit)

        # QComboBox para el intervalo de tiempo
        self.interval_combobox = QComboBox()
        self.interval_combobox.currentIndexChanged.connect(self.on_interval_selected)
        self.interval_combobox.addItem("Seleccione un intervalo de tiempo")  # Elemento inicial como título
        layout.addWidget(QLabel("Intervalo de Tiempo:"))
        layout.addWidget(self.interval_combobox)
        # QComboBox para mostrar los símbolos
        self.symbol_combobox = QComboBox()
        self.symbol_combobox.currentIndexChanged.connect(self.on_symbol_selected)
        layout.addWidget(self.symbol_combobox)
        # QLabel para mostrar la cantidad de símbolos
        self.symbol_count_label = QLabel(f'Cantidad de símbolos: {len(self.index_to_symbol_map)}')
        layout.addWidget(self.symbol_count_label)
        # QLabel para mostrar el NOMBRE(KEY) seleccionado
        self.selected_symbol_label = QLabel("ID seleccionado: Ninguno")
        layout.addWidget(self.selected_symbol_label)
        tab.setLayout(layout)
        # QLabel para mostrar el POS(VALUE) seleccionado
        self.selected_symbol_pos =  QLabel("Pos seleccionado: Ninguno")
        layout.addWidget(self.selected_symbol_pos)
        tab.setLayout(layout)

    def configurarTabExchanges(self, tab):
        layout = QVBoxLayout()
        # Crear QTextEdit para logs en la pestaña 'Exchanges'
        #self.log_edit_exchanges = QTextEdit()
        #self.log_edit_exchanges.setReadOnly(True)
        #layout.addWidget(self.log_edit_exchanges)
        tab.setLayout(layout)

    def configurarTabAssets(self, tab):
        layout = QVBoxLayout()
        # Crear QTextEdit para logs en la pestaña 'Assets'
        #self.log_edit_assets = QTextEdit()
        #self.log_edit_assets.setReadOnly(True)
        #layout.addWidget(self.log_edit_assets)
        tab.setLayout(layout)

    def ask_for_filter(self):
        reply = QMessageBox.question(self, "Confirmación", "¿Deseas aplicar un filtro?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.filter_for_GetInfo()
        else:
            reply2 = QMessageBox.question(self, "Confirmación!!", "Este proceso tarda tres horas...", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply2 == QMessageBox.Yes:
                self.index_to_symbol_map = self.handler.getInfoS("")
                self.symbol_count_label.setText(f'Cantidad de símbolos actualizado : {len(self.index_to_symbol_map)}')
                self.update_symbol_combobox()

    def filter_for_GetInfo(self):
        default_filter = "BINANCE_SPOT_B"  # Filtro predeterminado
        text, ok = QInputDialog.getText(self, "Filtro", "Ingresa el filtro:", text=default_filter)
        if ok and text:
            self.index_to_symbol_map = self.handler.getInfoS(text)
            self.symbol_count_label.setText(f'Cantidad de símbolos actualizado : {len(self.index_to_symbol_map)}')
            self.update_symbol_combobox()
    
    def start(self):
        pass

    def ask_for_key(self):
        #segunda clave valida !! AAA49AEB-B190-4F8B-AA2B-EA1D7A7E9148
        default_text = self.handler.config_getApiKey() # Texto predeterminado
        text, ok = QInputDialog.getText(self, "Input Dialog", "Ingresa tu coin API key:", text=default_text)
        if ok and text:
            # Haz algo con el texto ingresado
            if default_text == text :
                return
            else:
                self.log_message(f'API Key ingresada: {text}')
                self.handler.config_setApiKey(text)

    def confirm_exit(self):
         # Save the selected dates
        self.settings.setValue("date_start", self.time_start.toString(Qt.ISODate))
        self.settings.setValue("date_end", self.time_end.toString(Qt.ISODate))

        reply = QMessageBox.question(self, 'Confirm Exit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.instance().quit()  # Cierra la aplicación

    def log_message(self, message):
        ''' Append the message to the log window
        '''
        #self.log_edit.append(message)

    def open_date_input_dialog(self):
        # Create an instance of the DateInputDialog class
        date_input_dialog = DateInputDialog(self)
        # Execute the dialog using the exec_() method
        result = date_input_dialog.exec_()
        # At this point, the dialog has been executed, and the result is available
        # The result typically indicates whether the user accepted or rejected the dialog
        # Further logic can be added here based on the result, e.g., processing user input

        if result == QDialog.Accepted:
           # User accepted the dialog
           # Retrieve selected dates from the DateInputDialog
           time_start, time_end = date_input_dialog.get_dates()
           # Log the selected dates
           self.log_message(f'Date Start for Option 1: {time_start.toString(Qt.ISODate)}')
           self.log_message(f'Date End for Option 1: {time_end.toString(Qt.ISODate)}')
        else:
            self.log_message('Date input dialog was canceled or closed.')


    def show_about_dialog(self):
        about_text = 'This is a simple gmorey application.'
        QMessageBox.about(self, 'About', about_text)

    def apply_filter(self, text):
        if text.lower() == "quit":
            QApplication.instance().quit()
            return
        self.current_filter_text = text
        self.page = 0  # Reinicia a la primera página
        self.update_symbol_combobox()

    def load_next_page(self):
        self.page += 1
        self.update_symbol_combobox()

    def load_prev_page(self):
        if self.page > 0:
            self.page -= 1
        self.update_symbol_combobox()

    def update_symbol_combobox(self):
        self.symbol_combobox.clear()


        # Filtrar y paginar sobre self.index_to_symbol_map
        filtered_symbols = [symbol_id for symbol_id in self.index_to_symbol_map.keys() if self.current_filter_text.lower() in symbol_id.lower()]

        # Aplicar la paginación
        start_index = self.page * self.page_size
        end_index = start_index + self.page_size
        paginated_symbols = filtered_symbols[start_index:end_index]

        # Agregar los símbolos filtrados y paginados al QComboBox
        for symbol_id in paginated_symbols:
            self.symbol_combobox.addItem(symbol_id)

    def filter_symbols(self, text):
        self.symbol_combobox.clear()
        filtered_list = [symbol for symbol in full_symbol_list if text.lower() in symbol.lower()]
        self.symbol_combobox.addItems(filtered_list)

    def closeEvent(self, event):
        # Crear un mensaje de advertencia cuando se intente cerrar la ventana
        reply = QMessageBox.warning(self, "Salir del sistema", "Por favor, cierre el sistema a través de su menú de salida: Exit", QMessageBox.Ok, QMessageBox.Ok)

        # Ignorar el evento de cierre para mantener la ventana abierta
        event.ignore()

    def on_symbol_selected(self, index):
        # Obtén el símbolo seleccionado del QComboBox
        self.selected_symbol = self.symbol_combobox.itemText(index)
        # Actualiza el QLabel con el símbolo seleccionado
        self.selected_symbol_label.setText(f"Symbol     : {self.selected_symbol}")
        pos = self.index_to_symbol_map.get(self.selected_symbol, "No encontrado")
        self.selected_symbol_pos.setText(f"Symbol pos : {pos}")
        self.boolean_symbol_id_selected = True
        self.enableButton_RequestData()

    def sugerir_intervalo(self, fecha_inicio, fecha_fin):
        # Calcula la diferencia en días y en segundos
        diferencia = fecha_fin.toPyDate() - fecha_inicio.toPyDate()
        diferencia_dias = diferencia.days
        diferencia_segundos = diferencia.total_seconds()

        # Sugerencias basadas en la duración del período
        if diferencia_dias == 0:
            if diferencia_segundos <= 3600:  # Menos de 1 hora
                return ["1SEC", "2SEC", "3SEC", "5SEC", "10SEC", "15SEC", "20SEC", "30SEC","1MIN", "2MIN", "3MIN", "5MIN"]
            else:
                return ["10SEC","30SEC","1MIN", "2MIN", "3MIN", "5MIN", "10MIN", "15MIN", "20MIN", "30MIN"]
        elif 1 <= diferencia_dias < 7:
            return ["1MIN", "2MIN", "3MIN", "5MIN", "10MIN", "15MIN", "20MIN", "30MIN","1HRS", "2HRS", "3HRS", "4HRS", "6HRS"]
        else:
            return ["4HRS", "6HRS","1DAY", "2DAY", "3DAY", "5DAY", "7DAY", "10DAY"]

    def enableButton_RequestData(self):
        if (self.boolean_symbol_end_date_selected and self.boolean_symbol_start_date_selected and self.boolean_symbol_id_selected and self.boolean_symbol_interval_selected):
            self.request_info_button.setEnabled(True)  # Inicialmente deshabilitado

    def on_fecha_inicio_changed(self):
        opciones = self.sugerir_intervalo(self.start_date_edit.date(), self.end_date_edit.date())
        self.interval_combobox.clear()
        self.interval_combobox.addItems(opciones)
        self.boolean_symbol_start_date_selected = True
        self.enableButton_RequestData()
        

    def on_fecha_fin_changed(self):
        opciones = self.sugerir_intervalo(self.start_date_edit.date(), self.end_date_edit.date())
        self.interval_combobox.clear()
        self.interval_combobox.addItems(opciones)
        self.boolean_symbol_end_date_selected = True
        self.enableButton_RequestData()

    def on_request_data(self):
        # Obtener los valores seleccionados
        selected_id = self.symbol_combobox.currentText()
        start_date = self.start_date_edit.date().toString("yyyy-MM-dd")
        end_date = self.end_date_edit.date().toString("yyyy-MM-dd")
        # Realizar la acción de solicitud de información
        # Por ejemplo, una consulta a una base de datos o a una API
        self.handler.fetch_data(self.index_to_symbol_map[selected_id], start_date, end_date)

    def thread_on_request_data(self):
        self.data_thread = DataThread(self.on_request_data())
        self.data_thread.finished.connect(self.fin_on_request_data)
        self.data_thread.start()

    def fin_on_request_data(self, data):
        # Aquí procesas los datos y actualizas el gráfico
        self.update_graph(data)

    def on_interval_selected(self, index):
        # Obtén el símbolo seleccionado del QComboBox
        self.selected_interval = self.interval_combobox.itemText(index)
        # Actualiza el QLabel con el símbolo seleccionado
        # self.selected_interval_label.setText(f"ID seleccionado: {self.selected_interval}")
        self.boolean_symbol_interval_selected = True
        self.enableButton_RequestData()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CoinApiGUI()
    main_window.show()
    sys.exit(app.exec_())

