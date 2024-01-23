#input data
nama=input("Masukkan Nama Mahasiswa              :")
nim=input("Masukkan NIM Mahasiswa               :")
kelas=input("Masukkan Kelas                       :")
program=input("Masukkan program yang di ambil(S1)   :")
gel=input("Gelombang                            :")
jekel=input("Jenis Kelamin(L/P)                   :")
prodi=input("Fakultas/Prodi;\n1. Rekayasa Perangkat Lunak : RPL\n2. Ilmu Komputer            : IK\n3. Teknologi Informasi      : TI\n4. Sistem Informasi         : SI\n5. Akutansi                 : A\n6. Manajement               : M\nYang Diambil                         :")
waktu=input("Masukkan Waktu(pagi/sore)            :")

#Untuk program
if program=="S1" or "s1":
    p="S1"
else:
    "Data tidak ditemukan "
if prodi=="RPL":
    x="Rekayasa Perangkat Lunak"
    if gel == "1":
        pembayaran = 3280000
        ssp = 1000000
    elif gel == "2":
        pembayaran = 3280000
        ssp = 1250000
    elif gel == "3":
        pembayaran = 3280000
        ssp = 1500000
    elif gel == "4":
        pembayaran = 3280000
        ssp = 1200000
    elif gel == "5":
        pembayaran = 3280000
        ssp = 1500000
    elif gel == "6":
        pembayaran = 3280000
        ssp = 1800000
    else:
        print("Data Tidak Ditemukan")
elif prodi=="IK":
    x="Ilmu Komputer"
    if gel == "1":
        pembayaran = 3280000
        ssp = 1000000
    elif gel == "2":
        pembayaran = 3280000
        ssp = 1250000
    elif gel == "3":
        pembayaran = 3280000
        ssp = 1500000
    elif gel == "4":
        pembayaran = 3280000
        ssp = 1200000
    elif gel == "5":
        pembayaran = 3280000
        ssp = 1500000
    elif gel == "6":
        pembayaran = 3280000
        ssp = 1800000
    else:
        print("Data Tidak Ditemukan")
elif prodi=="TI":
    x="Teknologi Informasi"
    if gel == "1":
        pembayaran = 3280000
        ssp = 1000000
    elif gel == "2":
        pembayaran = 3280000
        ssp = 1250000
    elif gel == "3":
        pembayaran = 3280000
        ssp = 1500000
    elif gel == "4":
        pembayaran = 3280000
        ssp = 1200000
    elif gel == "5":
        pembayaran = 3280000
        ssp = 1500000
    elif gel == "6":
        pembayaran = 3280000
        ssp = 1800000
    else:
        print("Data Tidak Ditemukan")
elif prodi=="SI" or "si":
    x="Sistem Informasi"
    if gel == "1":
        pembayaran = 3280000
        ssp        = 1000000
    elif gel == "2":
        pembayaran = 3280000
        ssp        = 1250000
    elif gel == "3":
        pembayaran = 3280000
        ssp        = 1500000
    elif gel == "4":
        pembayaran = 3280000
        ssp        = 1200000
    elif gel == "5":
        pembayaran = 3280000
        ssp        = 1500000
    elif gel == "6":
        pembayaran = 3280000
        ssp        = 1800000
    else:
        print("Data Tidak Ditemukan")
elif prodi=="A":
    x="Akutansi"
    if gel == "1":
        pembayaran = 2580000
        ssp = 1000000
    elif gel == "2":
        pembayaran = 2580000
        ssp = 1250000
    elif gel == "3":
        pembayaran = 2580000
        ssp = 1500000
    elif gel == "4":
        pembayaran = 2580000
        ssp = 1200000
    elif gel == "5":
        pembayaran = 2580000
        ssp = 1500000
    elif gel == "6":
        pembayaran = 2580000
        ssp = 1800000
    else:
        print("Data Tidak Ditemukan")
elif prodi=="M":
    x="Manajement"
    if gel == "1":
        pembayaran = 2580000
        ssp        = 1000000
    elif gel == "2":
        pembayaran = 2580000
        ssp        = 1250000
    elif gel == "3":
        pembayaran = 2580000
        ssp        = 1500000
    elif gel == "4":
        pembayaran = 2580000
        ssp        = 1200000
    elif gel == "5":
        pembayaran = 2580000
        ssp        = 1500000
    elif gel == "6":
        pembayaran = 2580000
        ssp        = 1800000
    else:
        print("Data Tidak Ditemukan")
else :
    print("Data Tidak Ditemukan")

if waktu== "pagi" or "PAGI":
    biaya=0
elif waktu== "sore" or "SORE":
    biaya=500000
else :
    print("Data Tidak Ditemukan")

#proses jenis kelamin
if jekel=="L" or "l":
    jenis= "Laki-laki"
elif jekel=="P" or "p":
    jenis= "Perempuan"
else :
    print("Data Tidak Ditemukan")

total=pembayaran+biaya+ssp

#untuk ssp



#output
print("----------------------------------------------------")
print("             Pembayaran Semester 2 UBSI Slipi")
print("----------------------------------------------------")
print("Nama Mahasiswa :",nama)
print("NIM            :",nim)
print("Kelas          :",kelas)
print("Gelombang      :",gel)
print("Jenis Kelamin  :",jenis)
print("Program        :",p)
print("Prodi          :",x)
print("Waktu Kuliah   :",waktu)
print("Rincian Biaya :")
print("                 Biaya Kuliah            : Rp.",pembayaran)
print("                 Biaya Kelas Malam       : Rp.",biaya)
print("                 SSP                     : Rp.",ssp)
print("                                          _________________+")
print("                 Total Pembayaran        : Rp.",total)
