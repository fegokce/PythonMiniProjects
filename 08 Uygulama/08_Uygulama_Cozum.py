sinif_notlar = []
elliden_yuksek = 0
elliden_dusuk = 0
for i in range(1,30):
    notlar = int(input("Notunuzu girin:"))
    sinif_notlar.append(notlar)
for nott in sinif_notlar:
    if nott < 50:
        elliden_dusuk += 1
    else:
        elliden_yuksek += 1
print("50'den düşük not alan öğrenci sayısı: {0}".format(elliden_dusuk))
print("50'den yüksek not alan öğrenci sayısı: {0}".format(elliden_yuksek))
