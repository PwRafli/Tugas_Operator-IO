#deklarasi variabel
bil1 = 0
bil2 = 0
jumlah = 0
kurang = 0
kali = 0
bagi = 0.0
hsl_bagi = 0
sisa_bagi = 0
pangkat = 0

#input
bil1 = int(input("Masukkan Bilangan 1: "))
bil2 = int(input("Masukkan Bilangan 2: "))

#proses
jumlah += bil2
kurang -+bil2
kali *= bil2
bagi /=bil2
hsl_bagi //=bil2
sisa_bagi %=bil2
pangkat **=bil2

#output
print()
print(f"Hasil penjumlahan : {jumlah}")
print(f"Hasil pengurangan : {kurang}")
print(f"Hasil perkalian   : {kali}")
print(f"Hasil pembagian   : {bagi:.2f}")
print(f"Hasil pembagian genap: {hsl_bagi}")
print(f"Sisa hasil bagi   : {sisa_bagi}")
print(f"Hasil perpangkatan : {pangkat}")