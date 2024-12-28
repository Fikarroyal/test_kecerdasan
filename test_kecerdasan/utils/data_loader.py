def muat_pertanyaan(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return []
