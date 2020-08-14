#https://kite.com/python/docs/difflib.get_close_matches
#https://www.programiz.com/python-programming/datetime/strftime
import difflib
from datetime import datetime
import sys

zaman = datetime.now()
yıl = zaman.strftime("%Y")
ay = zaman.strftime("%m")
gün = zaman.strftime("%d")
saat = zaman.strftime("%H:%M")

kullanici_verileri = {'ahmet' : 'sehir123', 'meryem' : "4444"}

envanter={'kuşkonmaz':[10,5], 'brokoli':[15,6], 'havuç':[18,7], 'elma':[20,5], 'muz':[10,8], 'çilek':[30,3], 'yumurta':[50,2], 'karışık meyve suyu':[0,8], 'balık kroket':[25,12], 'dondurma':[32,6], 'elma suyu':[40,7], 'portakal suyu':[30,8], 'üzüm suyu':[10,9]}

kullanici_sepet = {}
giren_kullanici = []

def login():
    print("**** Şehir Online Markete Hoşgeldiniz ****\nLütfen kullanıcı bilgilerinizi girerek giriş yapın: ")
    while True:
        kullanici_adi = input("Kullanıcı Adı: ")
        kullanici_sifre = input("Şifre: ")
        if kullanici_adi in kullanici_verileri.keys() and kullanici_sifre in kullanici_verileri.values():       
            print("Başarıyla giriş yapıldı!")
            giren_kullanici.append(kullanici_adi)
            break
        else:
            print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")
    print("Hoş geldin {0}! Lütfen ilgili menü numarasını girerek aşağıdaki\nseçeneklerden birini seçin.".format(kullanici_adi))
login()

def menu_secimi():
    print("Lütfen aşağıdaki hizmetlerden birini seçin:\n1. Ürün arama\n2. Sepeti göster\n3. Ödeme\n4. Hesaptan çık\n5. Kapat")
    while True:
        secim = input("Seçiminiz: ")
        if secim == "1" or secim == "2" or secim == "3" or secim == "4" or secim == "5":
            if secim == "1":
                while True:
                    arama = input("Hangi ürünü arıyorsun? ")
                    sozluk_arama = difflib.get_close_matches(arama, envanter)
                    if arama == "*":
                        menu_secimi()
                        break
                    if sozluk_arama == []:
                        print("Aradığınız ürün? {0}\nAramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir kelime deneyin (Ana menü için * girin)".format(arama))
                    else:
                        print("{0} benzer ürün bulundu: ".format(len(sozluk_arama)))
                        for i in range(len(sozluk_arama)):
                            if envanter[sozluk_arama[i]][0] > 0:
                                print("{0}. {1} {2} ₺".format(i,sozluk_arama[i],envanter[sozluk_arama[i]][1]))
                        ekleme_anamenu = input("Lütfen sepete eklemek istediğiniz ürünü seçin(ana menü için * giriniz): ")
                        if ekleme_anamenu == "*":
                            menu_secimi()
                            break
                        for i in range(len(sozluk_arama)):
                            if int(ekleme_anamenu) == i:
                                while True:
                                    miktar = input("{0} eklenecek. Miktarı girin: ".format(sozluk_arama[i]))
                                    if int(miktar) <= envanter[sozluk_arama[i]][0]:
                                        kullanici_sepet.setdefault(giren_kullanici[-1], {})
                                        kullanici_sepet[giren_kullanici[-1]].setdefault(sozluk_arama[i],miktar)
                                        print("Sepetinize {0} {1} eklendi.".format(miktar, sozluk_arama[i]))
                                        menu_secimi()
                                        break
                                    else:
                                        print("Üzgünüz! Miktar, limiti aşıyor. Lütfen daha az bir miktarla tekrar deneyin")
                        else:
                            print("Sepete eklemek istediğiniz ürünün numarası hatalıdır.")
            elif secim == "2":
                if giren_kullanici[-1] not in kullanici_sepet or list(kullanici_sepet.values()) == [{}]:
                    print("Sepetiniz boş\nToplam : 0 TL")
                    menu_secimi()
                    break
                else:
                    print("Sepetinizdekiler:")
                    toplam_sepet = 0
                    urunadi = list((kullanici_sepet[giren_kullanici[-1]]).keys())
                    ürün_miktar = list(kullanici_sepet[giren_kullanici[-1]].values())
                    if giren_kullanici[-1] in list(kullanici_sepet.keys()):  
                        for i in range(len(urunadi)):
                            sepet_tutar = int(envanter[urunadi[i]][1]) * int(ürün_miktar[i])
                            toplam_sepet = toplam_sepet + sepet_tutar
                            print("{0}. {1} fiyat={2}₺ miktar={3} toplam={4}₺".format(i, (list(kullanici_sepet[giren_kullanici[-1]].keys()))[i], envanter[urunadi[i]][1], (list(kullanici_sepet[giren_kullanici[-1]].values()))[i], sepet_tutar))
                    print("Toplam: {0}₺".format(toplam_sepet))
                    while True:
                        print("Lütfen bir işlem seçiniz:\n1.Ürün miktarı güncelle\n2.Bir ürünü sil\n3.Ödemeye geç\n4.Ana menüye dön")
                        islem = input("Seçiminiz: ")
                        if islem == "1":
                            degisim_urun = input("Lütfen miktarını değiştirmek istediğiniz ürünü seçin: ")
                            for i in range(len(urunadi)):
                                while True:
                                    degisim_miktar = input("Lütfen yeni miktarı yazın: ")
                                    urunadi = list(kullanici_sepet[giren_kullanici[-1]].keys())
                                    kullanici_sepet[giren_kullanici[-1]].update({urunadi[int(degisim_urun)]:int(degisim_miktar)})
                                    yeni_tutar = 0
                                    if int(degisim_miktar) <= envanter[urunadi[i]][0]:
                                        tutar = int(degisim_miktar) * int(envanter[urunadi[i]][1])
                                        yeni_tutar = yeni_tutar + tutar
                                        print("{0}. {1} fiyat={2}₺ miktar={3} toplam={4}₺".format(i, (list(kullanici_sepet[giren_kullanici[-1]].keys()))[i], envanter[urunadi[i]][1], (list(kullanici_sepet[giren_kullanici[-1]].values()))[i], tutar))
                                        print("Toplam: {0}₺".format(yeni_tutar))
                                        break
                                    else:
                                        print("Üzgünüz! Miktar, limiti aşıyor. Lütfen daha az bir miktarla tekrar deneyin")
                        elif islem == "2":
                            silinecek_urun = int(input("Silinecek ürünü seçin: "))
                            if giren_kullanici[-1] in list(kullanici_sepet.keys()):                        
                                urunadi = list(kullanici_sepet[giren_kullanici[-1]].keys())
                                kullanici_sepet[giren_kullanici[-1]].pop(str(urunadi[silinecek_urun]))
                                urunadi = list((kullanici_sepet[giren_kullanici[-1]]).keys())
                                if urunadi == []:
                                    print("Sepetiniz boş.\nAna menüye dönülüyor...")
                                    menu_secimi()
                                    break
                                else:
                                    silindikten_sonra_tutar = 0
                                    for i in range(len(urunadi)):
                                        silindikten_sonra_tutar = envanter[urunadi[i]][1] * (list(kullanici_sepet[giren_kullanici[-1]].values()))[i]
                                        print("{0}. {1} fiyat={2}₺ miktar={3} toplam={4}₺".format(i, (list(kullanici_sepet[giren_kullanici[-1]].keys()))[i], envanter[urunadi[i]][1], (list(kullanici_sepet[giren_kullanici[-1]].values()))[i], silindikten_sonra_tutar))
                                    print("Toplam: {0}₺".format(silindikten_sonra_tutar))
                        elif islem == "3":
                            print("Makbuz İşleniyor...\n******* Sehir Online Market ********\n************************************\n    44 44 0 34\n    sehir.edu.tr\n------------------------------------")
                            toplam_odeme_yeni = 0
                            urunadi = list((kullanici_sepet[giren_kullanici[-1]]).keys())
                            ürün_miktar = list(kullanici_sepet[giren_kullanici[-1]].values())
                            if giren_kullanici[-1] in list(kullanici_sepet.keys()):  
                                for i in range(len(urunadi)):
                                    odeme_tutar = int(envanter[urunadi[i]][1]) * int(ürün_miktar[i])
                                    toplam_odeme_yeni = toplam_odeme_yeni + odeme_tutar
                                    print("{0}. {1} fiyat={2}₺ miktar={3} toplam={4}₺".format(i, (list(kullanici_sepet[giren_kullanici[-1]].keys()))[i], envanter[urunadi[i]][1], (list(kullanici_sepet[giren_kullanici[-1]].values()))[i], odeme_tutar))
                                envanter[urunadi[i]][0] = int(envanter[urunadi[i]][0]) - int(ürün_miktar[i])
                            print("------------------------------------\nToplam {0}₺\n------------------------------------\n{1}/{2}/{3}     {4}\nBizi tercih ettiğiniz için teşekkür ederiz!".format(toplam_odeme_yeni, yıl, ay, gün, saat))
                            menu_secimi()
                            break
                        elif islem == "4":
                            menu_secimi()
                            break
            elif secim == "3":
                if len(list(kullanici_sepet.keys())) == 0 or giren_kullanici[-1] not in kullanici_sepet:
                    print("Sepetiniz boş. Lütfen sepete ürün ekleyin.\nAna menüye dönülüyor...")
                    menu_secimi()
                    break
                else:
                    print("Makbuz İşleniyor...\n******* Sehir Online Market ********\n************************************\n    44 44 0 34\n    sehir.edu.tr\n------------------------------------")
                    toplam_odeme = 0
                    urunadi = list((kullanici_sepet[giren_kullanici[-1]]).keys())
                    ürün_miktar = list(kullanici_sepet[giren_kullanici[-1]].values())
                    if giren_kullanici[-1] in list(kullanici_sepet.keys()):  
                        for i in range(len(urunadi)):
                            odeme_tutar = int(envanter[urunadi[i]][1]) * int(ürün_miktar[i])
                            toplam_odeme = toplam_odeme + odeme_tutar
                            print("{0}. {1} fiyat={2}₺ miktar={3} toplam={4}₺".format(i, (list(kullanici_sepet[giren_kullanici[-1]].keys()))[i], envanter[urunadi[i]][1], (list(kullanici_sepet[giren_kullanici[-1]].values()))[i], odeme_tutar))
                            envanter[urunadi[i]][0] = int(envanter[urunadi[i]][0]) - int(ürün_miktar[i])
                    print("------------------------------------\nToplam {0}₺\n------------------------------------\n{1}/{2}/{3}     {4}\nBizi tercih ettiğiniz için teşekkür ederiz!".format(toplam_odeme, yıl, ay, gün, saat))
                    menu_secimi()
            elif secim == "4":
                login()
                menu_secimi()
                break
            elif secim == "5":
                sys.exit()
                break
            break                
        else:
            print("Lütfen aşağıdaki hizmetlerden birini seçin:\n1. Ürün arama\n2. Sepeti göster\n3. Ödeme\n4. Hesaptan çık\n5. Kapat")
menu_secimi()