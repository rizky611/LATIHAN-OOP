class InputForm:
    @staticmethod
    def input_data():
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
        tugas = float(input("Masukkan nilai Tugas: "))
        return {"nama": nama, "nim": nim, "uts": uts, "uas": uas, "tugas": tugas}