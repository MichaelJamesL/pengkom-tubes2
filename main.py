import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow  # Mengimpor kelas yang dihasilkan oleh pyuic5
from PyQt5.QtCore import Qt
#from test2 import FunctionHandler
from app import FunctionHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Menyiapkan UI dari file design.py
        
        self.function_handler = FunctionHandler()
        # Menghubungkan signal dari FunctionHandler ke slot untuk mengupdate QLabel
        self.function_handler.textUpdated.connect(self.update_text)

        self.function_handler.myFunc1()

    def update_text(self, text):
        """Slot untuk memperbarui teks pada QLabel"""
        self.label.setText(text)  # Mengubah teks QLabel dengan hasil dari signal
        
if __name__ == "__main__":
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, False)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, False)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
