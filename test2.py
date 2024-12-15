from PyQt5.QtCore import pyqtSignal, QObject

class FunctionHandler(QObject):
    # Signal untuk mengirim string ke slot
    textUpdated = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def print(self, msg):
        """Fungsi yang melakukan perhitungan dan mengirimkan hasil ke UI"""
        #Konversi message ke string
        if type(msg) != str:
            msg = str(msg)
          
        self.textUpdated.emit(msg)  # Emit signal dengan string
        

    def myFunc1(self):
        App(self)
        
def App(self):
    self.print("Hello World")
