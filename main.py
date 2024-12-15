import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design2 import Ui_MainWindow  # Mengimpor kelas yang dihasilkan oleh pyuic5
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

        # self.function_handler.myFunc1()

    def update_text(self, text):
        """Slot untuk memperbarui teks pada QLabel"""
        self.label.setText(text)  # Mengubah teks QLabel dengan hasil dari signal
        
    def keyPressEvent(self, event):
        """Override keyPressEvent untuk menangani Enter key"""
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.send_input()  # Memanggil fungsi get_input() saat Enter ditekan

    def send_input(self):
        input_text = self.lineEdit.text()
        self.function_handler.print(input_text)  # Mengirim input ke FunctionHandler
        self.lineEdit.clear()  # Clear the QLineEdit after sending the input
        
if __name__ == "__main__":
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, False)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, False)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())