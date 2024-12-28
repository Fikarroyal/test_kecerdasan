def tes_pola():
    print("Selamat datang di Tes Pengenalan Pola!")
    pertanyaan = [
        {"soal": "1, 3, 5, 7, ... (apa angka berikutnya?)", "jawaban": "9"},
        {"soal": "A, C, E, G, ... (apa huruf berikutnya?)", "jawaban": "I"}
    ]
    skor = 0
    for p in pertanyaan:
        jawaban = input(p["soal"] + " ")
        if jawaban.lower() == p["jawaban"].lower():
            print("Benar!")
            skor += 1
        else:
            print("Salah!")
    print(f"Skor Anda: {skor}/{len(pertanyaan)}")
