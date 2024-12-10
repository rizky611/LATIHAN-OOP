# view/mahasiswa.py
class ViewMahasiswa:
    @staticmethod
    def tampilkan_data(mahasiswa_list):
        if not mahasiswa_list:
            print("Tidak ada data mahasiswa.")
            return

        print("Daftar Mahasiswa:")
        print("No  Nama            NIM        UTS   UAS   Tugas  Rata-rata")
        print("----------------------------------------------------------")
        for i, mhs in enumerate(mahasiswa_list, start=1):
            print(f"{i:<3} {mhs.nama:<15} {mhs.nim:<10} {mhs.uts:<5} {mhs.uas:<5} {mhs.tugas:<6} {mhs.rata_rata:.2f}")
