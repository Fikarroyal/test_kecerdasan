def tes_iq():
    print("Selamat datang di Tes IQ!")
    pertanyaan = [
        {"soal": "Jika 2, 4, 6, 8, ..., maka angka selanjutnya adalah?", "jawaban": "10"},
        {"soal": "Berapa hasil dari 5 x 6?", "jawaban": "30"}
    ]
    skor = 0
    for p in pertanyaan:
        jawaban = input(p["soal"] + " ")
        if jawaban == p["jawaban"]:
            print("Benar!")
            skor += 1
        else:
            print("Salah!")
    print(f"Skor Anda: {skor}/{len(pertanyaan)}")
