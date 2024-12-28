def tes_logika():
    print("Selamat datang di Tes Logika!")
    pertanyaan = [
        {"soal": "Semua A adalah B. Semua B adalah C. Apakah semua A adalah C? (ya/tidak)", "jawaban": "ya"},
        {"soal": "Jika hari ini hujan, maka tanah basah. Hari ini tidak hujan. Apakah tanah basah? (ya/tidak)", "jawaban": "tidak"}
    ]
    skor = 0
    for p in pertanyaan:
        jawaban = input(p["soal"] + " ")
        if jawaban.lower() == p["jawaban"]:
            print("Benar!")
            skor += 1
        else:
            print("Salah!")
    print(f"Skor Anda: {skor}/{len(pertanyaan)}")
