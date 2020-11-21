while True: 
    print("Ucgenin Alani (1)\nDaire Alani (2)\nDiktortgen Alani (3)\nYamuk (4)\nCikis (-1)")
    secim = input("Seçiminiz: ")
    print("*****************************************")
    if secim == "1":
        kenar_birinci = float(input("1. kenarı girin: "))
        kenar_ikinci = float(input("2. kenarı girin: "))
        ucgen_alan = (kenar_birinci * kenar_ikinci) / 2
        print("Üçgenin Alanı: {0}".format(ucgen_alan))
        print("*****************************************")
    elif secim == "2":
        pi = 3
        yaricap = float(input("Dairenin yarıçapını girin: "))
        daire_alan = pi * (yaricap ** 2)
        print("Dairenin Alanı: {0}".format(daire_alan))
        print("*****************************************")
    elif secim == "3":
        kisa_kenar = float(input("Kısa kenarı girin: "))
        uzun_kenar = float(input("Uzun kenarı girin: "))
        dikdortgen_alan = kisa_kenar * uzun_kenar
        print("Dikdörtgenin Alanı: {0}".format(dikdortgen_alan))
        print("*****************************************")
    elif secim == "4":
        alt_kenar = float(input("Alt kenarı girin: "))
        ust_kenar = float(input("Üst kenarı girin: "))
        yukseklik = float(input("Yukseklik girin: "))
        yamuk_alan = (alt_kenar + ust_kenar) * yukseklik / 2
        print("Yamuğun Alanı: {0}".format(yamuk_alan))
        print("*****************************************")
    elif secim == "-1":
        break
