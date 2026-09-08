Batas_Nilai = (65,100)
Nilai_Masuk = []
Lulus = []
Remedi = []

print("DATA NILAI UJIAN MAHASISWA")
print("Minimal menginput 5 nilai ujian")
print("Harus ada nilai lulus dan remedi")
print("Ketik 'selesai' untuk mengakhiri input nilai ujian")

while True:
        Nilai = input("Masukkan nilai ujian (0-100):")

        if Nilai.lower() == "selesai":
                if len(Nilai_Masuk) < 5:
                    print("Nilai yang dimasukan belum mencapai 5, mohon masukan nilai lagi.")
                elif len(Lulus) == 0:
                    print("Harus ada minimal 1 nilai lulus")
                elif len(Remedi) == 0:
                    print("Harus ada minimal 1 nilai remedi")
                else:
                    break
        else:
            Nilai = int(Nilai)

            if Nilai < 0 or Nilai > Batas_Nilai [1]:
                    print("Nilai yang dimasukan tidak sesuai, mohon masukan nilai ujian antara 0-100")
            elif Nilai >= Batas_Nilai[0]:
                Nilai_Masuk.append(Nilai)
                Lulus.append(Nilai)
            else:
                Nilai_Masuk.append(Nilai)
                Remedi.append(Nilai)

print("Nilai yang dimasukan:")
print(Nilai_Masuk) 

hapus = input("Apakah ada nilai yang ingin di hapus? (Ada/Tidak ada):")

if hapus.lower() == "Ada":
    Nilai_Hapus = int(input("Masukan nilai yang ingin dihapus:"))

    if Nilai_Hapus in Nilai_Masuk:
        Nilai_Masuk.remove(Nilai_Hapus)

        if Nilai_Hapus in Lulus:
            Lulus.remove(Nilai_Hapus)
        elif Nilai_Hapus in Remedi:
            Remedi.remove(Nilai_Hapus)

        print("Nilai Mahasiswa berhasil di hapus")
    else:
        print("Nilai Mahasiswatidak ditemukan")

print("HASIL AKHIR")
print("Nilai masuk:", Nilai_Masuk)
print("Nilai Lulus:", Lulus)
print("Nilai Remedi:", Remedi)
