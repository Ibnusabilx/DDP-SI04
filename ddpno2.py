print()
print("===== NO 2 =====")
print()

#list luas bangun datar
pilih = int(input("""selamat datang diaplikasi menghitung
1.untuk menghitung luas persegi
2.untuk menghitung luas lingkaran
3.untuk menghitung luas segitiga 

masukan pilihan anda : \n"""))

match pilih:
    case 1 :
        print("kamu memilihi 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi persegi: "))
        luaspsg = sisi*sisi
        print("luas persegi yang sisinya ", sisi, "adalah", luaspsg )
    case 2 : 
        print("kamu memilihi 2 untuk menghitung lingkaran")
        jari2 = int(input("masukan jari-jari: "))
        luaslkr = 3.14 * jari2 * jari2
        print("luas lingkaran yang jari-jarinya ", jari2, "adalah", luaslkr )
    case 3 : 
        print("kamu memilihi 3 untuk menghitung segitiga")
        alas = int(input("masukan alas segitiga: "))
        tinggi = int(input("masukan tinggi segitiga: "))
        luassegitiga = 0.5 *alas * tinggi
        print("luas segitiga dengan alas ", alas, "dan tinggi", tinggi, "adalah", luassegitiga )
    case _:
        print("anda salah pilih")

