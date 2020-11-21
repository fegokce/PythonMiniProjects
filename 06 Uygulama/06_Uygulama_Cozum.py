sayilist = []
while True:
    sayi = int(input("Bir sayı giriniz: "))
    sayilist.append(sayi)
    if sayi == -1:
        sayilist.remove(-1)
        break
print("En büyük sayı: {0}".format(max(sayilist)))
print("En Küçük sayı: {0}".format(min(sayilist)))
