from iq_test import tes_iq
from logic_test import tes_logika
from memory_test import tes_memori
from pattern_recognition import tes_pola

def main():
    print("Selamat datang di Program Tes Kecerdasan!")
    print("Pilih tes yang ingin Anda coba:")
    print("1. Tes IQ")
    print("2. Tes Logika")
    print("3. Tes Memori")
    print("4. Tes Pengenalan Pola")
    pilihan = input("Masukkan nomor pilihan Anda: ")
    
    if pilihan == "1":
        tes_iq()
    elif pilihan == "2":
        tes_logika()
    elif pilihan == "3":
        tes_memori()
    elif pilihan == "4":
        tes_pola()
    else:
        print("Pilihan tidak valid. Program keluar.")

if __name__ == "__main__":
    main()
