# aux_gui.py

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressDialog, QMessageBox
from PyQt5.QtGui import QMovie

class DataThread(QThread):
    progress = pyqtSignal(int, int)  # Emite el número de ítems procesados y la velocidad
    finished = pyqtSignal()
    stopped = pyqtSignal()

    def __init__(self, function, args):
        QThread.__init__(self)
        self.function = function
        self.args = args
        self._is_running = True

    def run(self):
        start_time = time.time()
        for i, item in enumerate(self.args[0]):
            if not self._is_running:
                self.stopped.emit()
                return
            # ... Código para procesar el ítem ...
            if i % 100 == 0:  # Actualizar cada 100 ítems, ajustar según sea necesario
                elapsed_time = time.time() - start_time
                speed = i / elapsed_time if elapsed_time > 0 else 0
                self.progress.emit(i, speed)
        self.finished.emit()

    def stop(self):
        self._is_running = False


class LoadingDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setModal(True)
        self.setWindowTitle("Cargando...")
        self.setFixedSize(200, 200)

        layout = QVBoxLayout()
        
        # Configurar QLabel para mostrar el GIF
        self.loading_label = QLabel("Cargando...")
        self.loading_movie = QMovie("path/to/loading.gif")  # Asegúrate de tener un GIF adecuado
        self.loading_label.setMovie(self.loading_movie)
        self.loading_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.loading_label)
        self.setLayout(layout)

    def start_loading(self):
        self.loading_movie.start()
        self.show()

    def stop_loading(self):
        self.loading_movie.stop()
        self.close()


def create_progress_dialog(parent):
    progress_dialog = QProgressDialog("Procesando...", "Detener", 0, 100, parent)
    progress_dialog.setWindowModality(Qt.WindowModal)
    return progress_dialog

# Puedes agregar más clases y funciones de UI aquí

