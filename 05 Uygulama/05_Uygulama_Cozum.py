toplam = 0
agirlik = 0
sayim = -1
baslangic = 1
while True:
    agirlik = int(input("{0}. Malzemenin ağırlığını girin: ".format(baslangic)))
    baslangic += 1
    toplam = toplam + agirlik
    sayim += 1
    if agirlik == -1:
        toplam += 1
        break
print("Kamyona {0} Malzeme Yüklendi".format(sayim))
print("Malzemelerin Toplam Ağırlığı: {0}".format(toplam))
