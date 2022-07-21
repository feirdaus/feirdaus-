# Nama    : Moechammad Feirdaus Afriliyan
# Jurusan : Pengembangan Perangkat Lunak (PPL)
# Tugas   : Menghitung luas Bangun Datar

nama = input("Masukan Nama : ")
nim = input("Masukan NIM : ")

print()
print("====================================")
print("Welcome ",nama)
print("Your NIM ",nim)
print("====================================")
print()

# soal 1
print("\nQuestion No.1\nDiketahui sisi = 6, sebutkan Nama dan hitunglah luas Bangun Datar tersebut!")
banDar1 = input("Nama Bangun Datar = ") 
sisi1 = eval(input("Sisi : "))
sisi2 = eval(input("Sisi : "))
print("Bangun Datar tersebut adalah", banDar1, "dan Luas Bangun Datar Tersebut adalah",sisi1 * sisi2)

# soal 2
print("\nQuestion No.2\nDiketahui Alas = 7, Tinggi = 8, Sebutkan Nama dan luas Bangun Datar tersebut!")
banDar2 = input("Nama Bangun Datar = ") 
alas = eval(input("Alas : "))
tinggi = eval(input("Tinggi : "))
print("Bangun Datar tersebut adalah", banDar2, "dan Luas Bangun Datar Tersebut adalah",(alas * tinggi)/2)

# soal 3
print("\nQuestion No.3\nDiketahui Panjang = 4, Lebar = 9, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
banDar3 = input("Nama Bangun Datar = ") 
panjang = eval(input("Panjang : "))
lebar = eval(input("Lebar : "))
print("Bangun Datar tersebut adalah", banDar3, "dan Luas Bangun Datar Tersebut adalah",panjang * lebar)

# soal 4
print("\nQuestion No.4\nDiketahui Jari-jari 56, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
banDar4 = input("Nama Bangun Datar = ") 
phi = eval(input("π  : "))
jariJari = eval(input("r : "))
print("Bangun Datar tersebut adalah", banDar4, "dan Luas Bangun Datar Tersebut adalah",phi * jariJari * jariJari)

# soal 5
print("\nQuestion No.5\nDiketahui Diagonal I = 4, Diagonal II = 8, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
banDar5 = input("Nama Bangun Datar = ") 
d1 = eval(input("Diagonal I  : "))
d2 = eval(input("Diagonal II : "))
print("Bangun Datar tersebut adalah", banDar5, "dan Luas Bangun Datar Tersebut adalah",(d1*d2)/2)

# soal 6
print("\nQuestion No.6\nDiketahui Sisi AB dan CD sejajar, sisi AB = 6, sisi CD = 8, tinggi = 3, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
banDar6 = input("Nama Bangun Datar = ") 
sisiAB = eval(input("Sisi AB : "))
sisiCD = eval(input("Sisi CD : "))
tinggi = eval(input("Tinggi : "))
print("Bangun Datar tersebut adalah", banDar6, "dan Luas Bangun Datar Tersebut adalah",(sisiAB+sisiCD)*tinggi/2)

# soal 7
print("\nQuestion No.7\nDiketahui sebuah jajar genjang dengan alas = 9, tinggi = 7, hitunglah Luas Bangun Datar tersebut!") 
alasJG = eval(input("Alas  : "))
tinggiJG = eval(input("Tinggi : "))
print("Luas Jajar Genjang adalah",alasJG*tinggiJG)


print()
print("========================================")
print()
print(" Thank You Very Much For Your Attention ")
print()
print("========================================")