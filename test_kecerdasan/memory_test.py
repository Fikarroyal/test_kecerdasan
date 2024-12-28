import time

def tes_memori():
    print("Selamat datang di Tes Memori!")
    kata = "Kucing"
    print(f"Ingat kata ini: {kata}")
    time.sleep(5)
    print("\n" * 50)  # Clear screen
    jawaban = input("Apa kata yang tadi ditampilkan? ")
    if jawaban.lower() == kata.lower():
        print("Benar! Memori Anda baik.")
    else:
        print("Salah. Coba lagi lain kali!")
