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
        """Fungsi untuk menangani input dari QLineEdit"""
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
    cnt = 0
    suhu = float("inf")
    waktu = float("inf")
    while(suhu > suhu_max):
        print(f"Masukkan suhu di bawah {suhu_max}°C")
        suhu = int(input("Masukkan Suhu (°C) : "))
    while(waktu > waktu_max):
        print(f"Masukkan waktu di bawah {waktu_max} detik")
        waktu = int(input("Masukkan Waktu (detik) : "))
    return suhu, waktu

def sesuai(suhu, waktu):
    global temp
    verify = False
    temp = False
    while(verify == False):
        print(f"Suhu : {suhu}°C\nWaktu : {waktu} detik")
        tmp = str(input("Apakah suhu dan waktu sudah sesuai?\n1. Ya\n2. Tidak\n"))
        #format input
        if(int(tmp) == 1):
            verify = True
        elif(int(tmp) == 2):
            temp = bool(True)
            suhu, waktu = suhuwaktu()
    return suhu, waktu

def proses(suhu, waktu):
    print(f"Memulai proses\nSuhu : {suhu}°C\nWaktu : {waktu} detik")
    for i in range(waktu, -1, -1):
        print(f"\rMemproses... Sisa Waktu : {i//60:02d} menit {i%60:02d} detik", end="")
        time.sleep(1)
    print("\ntimer selesai, masuk hemat daya\n")
    tmp = str(input("Apakah anda ingin kembali menyalakan microwave? \n1. Ya\n2. Tidak\n"))
    #format input
    if(int(tmp) == 1):
        #lanjut
        return
    elif(int(tmp) == 2):
        global status
        status = False
        print("""             . . .                         
              \|/                          
            `--+--'                        
              /|\                          
             ' | '                         
               |                           
               |                           
           ,--'#`--.                       
           |#######|                       
        _.-'#######`-._                    
     ,-'###############`-.                 
   ,'#####################`,               
  /#########################\              
 |###########################|             
|#############################|            
|#############################|            
|#############################|            
|#############################|            
 |###########################|             
  \#########################/              
   `.#####################,'               
     `._###############_,'                 
        `--..#####..--'""")
        time.sleep(2)
        print("""
                   _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
              """)

def auto_defrost(tmp):
    suhu = int(tmp)
    waktu = int(tmp)
    return suhu, waktu

def auto_cook(cnt, rekom_waktu, rekom_suhu, rekomendasi):
    for i in rekomendasi.keys():
        print(f"{rekomendasi[i]+1}. {i}")
    print(f"{cnt+1}. simpan makanan baru")
    x = int(input("pilih "))
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
            x = int(input("pilih yg valid mas "))


def Defrost():
    print(f"Mode :\n1. Auto\n2. Manual")
    ModeDefrost = str(input("Pilih mode yang tersedia : "))

    mode_valid = False

    #Cek masukan
    while(mode_valid == False):
        #Format input
        ModeDefrost.lower()
        if(ModeDefrost.find("auto") != -1):
            ModeDefrost = 1
        elif(ModeDefrost.find("manual") != -1):
            ModeDefrost = 2

        #Cek masukan
        if(int(ModeDefrost) == 1):
            #Auto Defrost
            mode_valid = True
            Berat = int(input("Berat Makanan (g): "))
            suhu, waktu = auto_defrost(Berat)
            suhu, waktu = sesuai(suhu, waktu)
            proses(suhu, waktu)
        elif(int(ModeDefrost) == 2):
            #Manual
            mode_valid = True
            suhu, waktu = suhuwaktu()
            suhu, waktu = sesuai(suhu, waktu)
            proses(suhu, waktu)
        else:
            #Minta input lagi
            ModeDefrost = str(input("Mode Defrost apa? "))

#Masuk ke Cook
def Cook(cnt):
    #List mode
    print(f"Mode :\n1. Auto\n2. Manual")
    ModeCook = str(input("Pilih mode yang tersedia : "))

    mode_valid = False

    #Cek masukan
    while(mode_valid == False):
        #Format input
        ModeCook.lower()
        if(ModeCook.find("auto") != -1):
            ModeCook = 1
        elif(ModeCook.find("manual") != -1):
            ModeCook = 2

        #Cek masukan
        if(int(ModeCook) == 1):
            mode_valid = True
            #Jadi auto
            #Print list
            suhu, waktu, cnt = auto_cook(cnt, rekom_waktu, rekom_suhu, rekomendasi)
            #Pilih
            proses(suhu, waktu)
        elif(int(ModeCook) == 2):
            mode_valid = True
            #Jadi manual
            suhu, waktu = suhuwaktu()
            sesuai(suhu, waktu)
            proses(suhu, waktu)
        else:
            #Minta input lagi
            ModeCook = str(input("Mode Cook apa? "))
        return cnt

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
    self.print(""" 
                                                                                                    
                                                                                                    
    .--.--.            ____                         ___                                            
    /  /    '.        ,'  , `.                     ,--.'|_                                          
    |  :  /`. /     ,-+-,.' _ |            __  ,-.  |  | :,'                                         
    ;  |  |--`   ,-+-. ;   , ||          ,' ,'/ /|  :  : ' :                                         
    |  :  ;_    ,--.'|'   |  || ,--.--.  '  | |' |.;__,'  /                                          
    \  \    `.|   |  ,', |  |,/       \ |  |   ,'|  |   |                                           
    `----.   \   | /  | |--'.--.  .-. |'  :  /  :__,'| :                                           
    __ \  \  |   : |  | ,    \__\/: . .|  | '     '  : |__                                         
    /  /`--'  /   : |  |/     ," .--.; |;  : |     |  | '.'|                                        
    '--'.     /|   | |`-'     /  /  ,.  ||  , ;     ;  :    ;                                        
    `--'---' |   ;/        ;  :   .'   \---'      |  ,   /                                         
            '---'         |  ,     .-./           ---`-'                                          
            ____            `--`---'                                                               
            ,'  , `.                                                                                 
        ,-+-,.' _ |  ,--,                                                                           
    ,-+-. ;   , ||,--.'|              __  ,-.   ,---.           .---.                              
    ,--.'|'   |  ;||  |,             ,' ,'/ /|  '   ,'\         /. ./|               .---.          
    |   |  ,', |  ':`--'_       ,---. '  | |' | /   /   |     .-'-. ' |  ,--.--.    /.  ./|  ,---.   
    |   | /  | |  ||,' ,'|     /     \|  |   ,'.   ; ,. :    /___/ \: | /       \ .-' . ' | /     \  
    '   | :  | :  |,'  | |    /    / ''  :  /  '   | |: : .-'.. '   ' ..--.  .-. /___/ \: |/    /  | 
    ;   . |  ; |--' |  | :   .    ' / |  | '   '   | .; :/___/ \:     ' \__\/: . .   \  ' .    ' / | 
    |   : |  | ,    '  : |__ '   ; :__;  : |   |   :    |.   \  ' .\    ," .--.; |\   \   '   ;   /| 
    |   : '  |/     |  | '.'|'   | '.'|  , ;    \   \  /  \   \   ' \ |/  /  ,.  | \   \  '   |  / | 
    ;   | |`-'      ;  :    ;|   :    :---'      `----'    \   \  |--";  :   .'   \ \   \ |   :    | 
    |   ;/          |  ,   /  \   \  /                      \   \ |   |  ,     .-./  '---" \   \  /  
    '---'            ---`-'    `----'                        '---"     `--`---'             `----'   
                                                                                                    
    """)
    while(status != False):
        self.getInput("Press Enter to Continue")
        #List mode
        mode_awal = self.getInput("Mode :\n1. Defrost\n2. Cook\nPilih mode yang tersedia : ")
        mode_valid = bool(False)

        #Cek masukan
        while(mode_valid == False):
            #Format input menjadi angka
            mode_awal.lower()
            if(mode_awal.find("defrost") != -1):
                mode_awal = 1
            elif(mode_awal.find("cook") != -1):
                mode_awal = 2

            #Cek masukan
            if(int(mode_awal) == 1):
                mode_valid = True
                Defrost() #Masuk ke Defrost
            elif(int(mode_awal) == 2):
                mode_valid = True
                cnt = Cook(cnt) #Masuk Cook
            else: #Eror Prevention
                mode_awal = str(input("Mohon pilih mode yang tersedia "))