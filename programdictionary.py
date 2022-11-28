print("Program Daftar Nilai")
print("====================")
print()
data = {}
while True:
    print()
    a = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] :")
    print()

    if a == "T":
        print("Tambah Data")
        nama = input("Nama\t: ")
        nim = int(input("NIM\t: "))
        tugas = int(input("Nilai Tugas\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        akhir = (int(tugas)*30/100) + (int(uts)*35/100) + (int(uas)*35/100)
        data[nama] = nim, tugas, uts, uas, akhir
        print()

    elif a == "U":
        print("Ubah Data")
        nama = input("Masukkan Nama :")
        print()
        if data.keys():
            tugas = int(input("Nilai Tugas\t: "))
            uts = int(input("Nilai UTS\t: "))
            uas = int(input("Nilai UAS\t: "))
            akhir = (int(tugas)*30/100) + (int(uts)*35/100) + (int(uas)*35/100)

    elif a == "H":
        print("Hapus Data")
        nama = input("Masukkan Nama :")
        if nama in data.keys():
            del data[nama]

    elif a == "C":
        print("Cari Data")
        nama = input("Masukkan Nama  :")
        if data.keys():
            print(72*"=")
            print("| {0:^10} | {1:^10} | {2:^6} | {3:^6} | {4:^6} | {5:^12} |".format("Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"))
            print(72*"=")
            print("| {0:>10} | {1:>10} | {2:>6} | {3:>5} | {4:>6} | {5:>12} |".format(nama, nim, tugas, uts, uas, akhir))
            print(72*"=")
            print()

    elif a == "L":
        if data.items():
            print("Daftar Nilai")
            print(72*"=")
            print("| {0:^10} | {1:^10} | {2:^6} | {3:^6} | {4:^6} | {5:^12} |".format("Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"))
            print(72*"=")
            for item in data.items():
                print("| {0:>10} | {1:>10} | {2:>6} | {3:>6} | {4:>6} | {5:>12} |".format(nama, nim, tugas, uts, uas, akhir))
                print(72*"=")
            print()
        else:
            print("Daftar Nilai")
            print(72*"=")
            print("| {0:^10} | {1:^10} | {2:^6} | {3:^6} | {4:^6} | {5:^12} |".format("Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"))
            print(72*"=")
            print("|                            Tidak Ada Data                           |")
            print(72*"=")
            print()
    elif a == "K":
        break