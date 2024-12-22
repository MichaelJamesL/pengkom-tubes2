#Import Library
import time
from PyQt5.QtCore import pyqtSignal, QObject, QThread

#Fungsi
global_input = ""
class FunctionHandler(QObject):
    # Signal untuk mengirim string ke slot
    textUpdated = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def print(self, msg):
        """Fungsi yang melakukan perhitungan dan mengirimkan hasil ke UI"""
        self.textUpdated.emit(msg)  # Emit signal dengan string hasil perhitungan

    def handleInput(self, input_text):
        """Fungsi untuk menangani self.getInput dari QLineEdit"""
        global global_input
        global_input = input_text
        
    def myFunc1(self):
        Start(self)

    def getInput(self, msg):
        prev_input = global_input
        self.print(msg)
        while(global_input == prev_input):
            time.sleep(1)
        return global_input
    
def suhuwaktu():
    #input suhu waktu manual
    suhu = float("inf")
    waktu = float("inf")
    while(suhu > suhu_max):
        suhu = float(self.getInput(f"Masukkan suhu di bawah {suhu_max}°C\nMasukkan Suhu (°C) : "))
    while(waktu > waktu_max):
        waktu = int(self.getInput(f"Masukkan waktu di bawah {waktu_max} detik\nMasukkan Waktu (detik) : "))
    return suhu, waktu

def sesuai(suhu, waktu):
    #cek apakah suhu waktu sesuai
    global temp
    verify = False
    temp = False
    while(verify == False):
        tmp = str(self.getInput(f"Suhu : {suhu}°C\nWaktu : {waktu} detik\nApakah suhu dan waktu sudah sesuai?\n1. Ya\n2. Tidak\n"))
        #format input
        if(int(tmp) == 1):
            verify = True
        elif(int(tmp) == 2):
            temp = bool(True)
            suhu, waktu = suhuwaktu()
    return suhu, waktu

def ulang(): 
    tmp = str(input("\nApakah anda ingin kembali menyalakan microwave? \n1. Ya\n2. Tidak\n"))
    #format input
    if(int(tmp) == 1):
        #lanjut
        return
    elif(int(tmp) == 2):
        global status
        status = False
        self.print(""". . .""")
        time.sleep(2)
        self.print("""D U A R R R""")
        
def proses(suhu, waktu, mode):
    self.print(f"Memulai proses\nSuhu : {suhu}°C\nWaktu : {waktu} detik")
    for i in range(waktu, -1, -1):
        self.print(f"\rMemproses... Sisa Waktu : {i//60:02d} menit {i%60:02d} detik", end="")
        time.sleep(1)
    if(mode == "cook"):
        #cek user input
        #masuk mode warm
        print("\nMenghangatkan...")
    ulang()

def auto_defrost(tmp):
    suhu = int(tmp)
    waktu = int(tmp)
    return suhu, waktu

def auto_cook(cnt, rekom_waktu, rekom_suhu, rekomendasi):
    recommendations = [f"{rekomendasi[i]+1}. {i}" for i in rekomendasi.keys()]
    #format Input 
    x = int(self.getInput("\n".join(recommendations), f"\n{cnt+1}. simpan makanan baru\nPiilih makanan yang tersedia"))
    x -= 1
    mode_valid = False
    while(mode_valid == False):
        if(x < cnt):
            mode_valid = True
            suhu = rekom_suhu[x]
            waktu = rekom_waktu[x]
            suhu, waktu = sesuai(suhu, waktu)
            if(temp == True):
                y = str(input("Apakah Anda mau menyimpannya?\n1.Ya\n2.Tidak\n"))
                if(int(y) == 1):
                    rekom_suhu[x] = suhu
                    rekom_waktu[x] = waktu
            return suhu, waktu, cnt
        elif(x == cnt):
            mode_valid = True
            #input baru
            Makanan = str(input("Nama Makanan : "))
            suhu, waktu = suhuwaktu()
            tmp = 3
            while tmp!=1:
                tmp = int(input("Simpan?\n1.Ya\n2.Tidak "))
                if tmp == 1:
                    rekomendasi.update({Makanan : cnt})
                    rekom_suhu.append(suhu)
                    rekom_waktu.append(waktu)
                    cnt += 1
                elif tmp == 2 :
                    tmp = 1
            return suhu, waktu, cnt
        else:
            x = int(self.getInput("Mohon pilih mode yang valid: "))


def Defrost(par):
    self.print("Memasuki mode defrost")
    time.sleep(0.7)
    #Cek dari multi atau manual
    ModeDefrost = 0
    if(par == 0): 
        ModeDefrost = str(self.getInput(f"Mode yang tersedia :\n1. Auto\n2. Manual\nPilih mode yang tersedia : "))
    elif(par == 1): 
        ModeDefrost = '1'
    
    mode_valid = False

    #Cek masukan
    while(mode_valid == False):
        #Format Input
        ModeDefrost.lower()
        if(ModeDefrost.find("auto") != -1):
            ModeDefrost = 1
        elif(ModeDefrost.find("manual") != -1):
            ModeDefrost = 2

        #Cek masukan
        if(int(ModeDefrost) == 1):
            #Auto Defrost
            mode_valid = True
            Berat = int(self.getInput("Berat Makanan (g): "))
            suhu, waktu = auto_defrost(Berat)
            suhu, waktu = sesuai(suhu, waktu)
        elif(int(ModeDefrost) == 2):
            #Manual
            mode_valid = True
            suhu, waktu = suhuwaktu()
            suhu, waktu = sesuai(suhu, waktu)
        else:
            #Minta Input lagi
            ModeDefrost = str(self.getInput("Mode Defrost apa? "))
     
    #Cek asal   
    if(par == 0): 
        proses(suhu, waktu, "defrost")
        ulang()
    elif(par == 1): 
        Cook(cnt, 1, suhu, waktu)

#Masuk ke Cook
def Cook(cnt, par, suhu_def, waktu_def):
    self.print("Memasuki mode cook")
    time.sleep(0.7)
    #Cek asal
    ModeCook = 0
    if(par == 0): 
        print(f"Mode yang tersedia :\n1. Auto\n2. Manual")
        ModeCook = str(self.getInput(f"Memasuki mode cook\nMode :\n1. Auto\n2. Manual\nPilih mode yang tersedia : "))
    elif(par == 1): 
        ModeCook = '1'
    
    mode_valid = False

    #Cek masukan
    while(mode_valid == False):
        #Format Input
        ModeCook.lower()
        if(ModeCook.find("auto") != -1):
            ModeCook = 1
        elif(ModeCook.find("manual") != -1):
            ModeCook = 2

        #Cek masukan
        if(int(ModeCook) == 1):
            mode_valid = True
            #Jadi auto
            #print list
            suhu, waktu, cnt = auto_cook(cnt, rekom_waktu, rekom_suhu, rekomendasi)
            #Pilih
        elif(int(ModeCook) == 2):
            mode_valid = True
            #Jadi manual
            suhu, waktu = suhuwaktu()
            sesuai(suhu, waktu)
        else:
            #Minta Input lagi
            ModeCook = str(self.getInput("Mode Cook apa? "))
    
    if(par == 0): 
        proses(suhu, waktu, "cook")
        ulang()
    elif(par == 1):
        proses(suhu_def, waktu_def, "defrost")
        proses(suhu, waktu, "cook")
        ulang()
        
    return cnt

def Multi():
    Defrost(1)

#List rekomendasi (pls update 33nya)
rekomendasi = {
    "ayam" : 0,
    "udang" : 1,
    "roti" : 2
}

rekom_suhu = [
    80,
    60,
    50,
]

rekom_waktu = [
    100,
    1,
    1
]

#Suhu sama waktu max bisa diubah
suhu_max = int(100)
waktu_max = int(1800)

cnt = len(rekomendasi)
status = bool(True)


#Mulai di sini...
def Start(self):
    self.print("""S M A R T  M I C R O W A V E""")
    while(status != False):
        self.getInput("Press Enter to Continue")
        #List mode
        mode_awal = self.getInput("Mode :\n1. Defrost\n2. Cook\nPilih mode yang tersedia : ")
        mode_valid = bool(False)
        cnt = int(len(rekomendasi))

        #Cek masukan
        while(mode_valid == False):
            #Format self.getInput menjadi angka
            mode_awal.lower()
            if(mode_awal.find("defrost") != -1 and mode_awal.find("cook") != -1):
                mode_awal = 3
            elif(mode_awal.find("cook") != -1):
                mode_awal = 1
            elif(mode_awal.find("defrost") != -1): 
                mode_awal = 2

            #Cek masukan
            if(int(mode_awal) == 1):
                mode_valid = True
                Defrost(0) #Masuk ke Defrost
            elif(int(mode_awal) == 2):
                mode_valid = True
                cnt = Cook(cnt, 0) #Masuk Cook da
            elif(int(mode_awal) == 3): 
                mode_valid = True
                Multi()
            else: #Eror Prevention
                mode_awal = str(self.getInput("Mohon pilih mode yang tersedia "))