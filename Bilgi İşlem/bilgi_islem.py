from tkinter import *
from tkinter.ttk import Combobox
import sqlite3

con = sqlite3.connect("bilgi_islem.db")
cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS bilgiislemtablo (tcno TEXT,ad_soyad TEXT,yas TEXT,cinsiyet TEXT,adres TEXT,yapilanhizmet TEXT,tarih TEXT,kullanilanmalzeme TEXT,malzemeadet INT,malzemefiyat INT,alinanucret INT,malzememaliyet INT,kasa INT,hemsireadi TEXT)')

class bilgi_islem(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI(parent)
    def initUI(self, parent):

        self.frame1 = LabelFrame(self, text="HASTA BİLGİLERİ", fg="black", font="serif 15 bold")
        self.frame1.grid(row=0, column=0, padx=20, pady=20)

        self.bir = StringVar()
        self.tcno = Label(self.frame1, text="T.C. Kimlik No", fg="black", font="serif 10 bold")
        self.tcno.grid(row=0, column=0, padx=20, pady=20, sticky="W")
        self.tcnoo = Entry(self.frame1, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.bir)
        self.tcnoo.grid(row=0, column=1, padx=20)
        self.tcnooo = Button(self.frame1, text="BUL", bg="green", fg="black", font="serif 10 bold", command=self.hastabilgi)
        self.tcnooo.grid(row=0, column=2, padx=(0,20), pady=20, sticky="W")

        self.iki = StringVar()
        self.hastaad = Label(self.frame1, text="Ad - Soyad", fg="black", font="serif 10 bold")
        self.hastaad.grid(row=1, column=0, padx=20, sticky="W")
        self.hastaadd = Entry(self.frame1, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.iki)
        self.hastaadd.grid(row=1, column=1)

        self.uc = StringVar()
        self.hastayas = Label(self.frame1, text="Yaş", fg="black", font="serif 10 bold")
        self.hastayas.grid(row=2, column=0, pady=20, padx=20, sticky="W")
        self.hastayass = Entry(self.frame1, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.uc)
        self.hastayass.grid(row=2, column=1)

        self.cinsiyet = IntVar()
        self.cinsiyet.set(1)
        self.hastacinsiyet = Label(self.frame1, text="Cinsiyet", fg="black", font="serif 10 bold")
        self.hastacinsiyet.grid(row=3, column=0, padx=20, sticky="W")
        self.hastacinsiyeterkek = Radiobutton(self.frame1, text="Erkek", font="serif 10 bold", variable=self.cinsiyet, value=1)
        self.hastacinsiyeterkek.place(x=200, y=150)
        self.hastacinsiyetkadın = Radiobutton(self.frame1, text="Kadın", font="serif 10 bold", variable=self.cinsiyet, value=2)
        self.hastacinsiyetkadın.place(x=300, y=150)
        
        self.dort = StringVar()
        self.hastaadres = Label(self.frame1, text="Adres", fg="black", font="serif 10 bold")
        self.hastaadres.grid(row=4, column=0, pady=20, padx=20, sticky="W")
        self.hastaadress = Entry(self.frame1, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.dort)
        self.hastaadress.grid(row=4, column=1)

        self.hizmet = StringVar()
        self.yapilanhizmet = Label(self.frame1, text="Yapılan Hizmet", fg="black", font="serif 10 bold")
        self.yapilanhizmet.grid(row=5, column=0, padx=20, sticky="W")
        self.yapilanhizmett = Combobox(self.frame1, width=27, textvariable=self.hizmet, font="serif 10 bold", justify="center")
        self.yapilanhizmett['values'] = (
                                        "Acil Yardım Uygulamaları",
                                        "Ambulans Hizmeti",
                                        "Apse Boşaltma",
                                        "Diğer",
                                        "Dikiş (Sütur) Atma",
                                        "Enjeksiyon",
                                        "Evde Hasta Bakım Hizmetleri",
                                        "Hemoglobin Ölçümü",
                                        "Kulak Yıkama",
                                        "Nasır Alma",
                                        "Pansuman ve Küçük Cerrahi Müdahale",
                                        "Serum Takma ve Takibi",
                                        "Sonda Takma",
                                        "Tırnak Çekme"
                                        "Tansiyon Takibi",
                                        "Yanık Bakımı",
                                        "Yatak Yarası Bakımı",
                                        )
        self.yapilanhizmett.grid(row=5, column=1)

        self.bes = StringVar()
        self.tarih = Label(self.frame1, text="Tarih (gg.aa.yyyy)", fg="black", font="serif 10 bold")
        self.tarih.grid(row=6, column=0, pady=20, padx=20, sticky="W")
        self.tarihh = Entry(self.frame1, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.bes)
        self.tarihh.grid(row=6, column=1)

        self.frame2 = LabelFrame(self, text="FİYATLANDIRMA", fg="black", font="serif 15 bold")
        self.frame2.grid(row=0, column=1)

        self.alti = StringVar()
        self.kullanilanmalzeme = Label(self.frame2, text="Kullanılan Malzeme", fg="black", font="serif 10 bold")
        self.kullanilanmalzeme.grid(row=0, column=0, padx=20, pady=20, sticky="W")
        self.kullanilanmalzemee = Entry(self.frame2, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.alti)
        self.kullanilanmalzemee.grid(row=0, column=1, padx=20)

        self.yedi = StringVar()
        self.yedi.set(0)
        self.malzemeadet = Label(self.frame2, text="Kullanılan Malzeme Adeti", fg="black", font="serif 10 bold")
        self.malzemeadet.grid(row=1, column=0, padx=20, sticky="W")
        self.malzemeadett = Entry(self.frame2, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.yedi)
        self.malzemeadett.grid(row=1, column=1)

        self.sekiz = StringVar()
        self.sekiz.set(0)
        self.malzemefiyat = Label(self.frame2, text="Kullanılan Malzeme Birim Fiyatı", fg="black", font="serif 10 bold")
        self.malzemefiyat.grid(row=2, column=0, pady=20, padx=20, sticky="W")
        self.malzemefiyatt = Entry(self.frame2, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.sekiz)
        self.malzemefiyatt.grid(row=2, column=1)

        self.dokuz = StringVar()
        self.dokuz.set(0)
        self.alinanucret = Label(self.frame2, text="Hastadan Alınan Ücret", fg="black", font="serif 10 bold")
        self.alinanucret.grid(row=3, column=0, padx=20, sticky="W")
        self.alinanucrett = Entry(self.frame2, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.dokuz)
        self.alinanucrett.grid(row=3, column=1)

        self.maliyetmalzeme = IntVar()
        self.maliyetmalzeme.set(0)
        self.malzememaliyet = Label(self.frame2, text="Kullanılan Malzeme Maliyeti", fg="black", font="serif 10 bold")
        self.malzememaliyet.grid(row=4, column=0, pady=20, padx=20, sticky="W")
        self.malzememaliyett = Entry(self.frame2, text="", width=30, font="serif 10 bold", state="disabled", textvariable=self.maliyetmalzeme, justify="center")
        self.malzememaliyett.grid(row=4, column=1)

        self.frame3 = LabelFrame(self, text="ÖZET", fg="black", font="serif 15 bold")
        self.frame3.grid(row=0, column=3, padx=20)

        self.on = StringVar()
        self.hemsireadi = Label(self.frame3, text="Hemşire Adı", fg="black", font="serif 10 bold")
        self.hemsireadi.grid(row=0, column=0, padx=20, pady=20, sticky="W")
        self.hemsireadi = Entry(self.frame3, text="", width=30, font="serif 10 bold", justify="center", textvariable=self.on)
        self.hemsireadi.grid(row=0, column=1, padx=20)

        self.kaydetbuton = Button(self.frame3, text="KAYDET", bg="green", fg="black", width=25, font="serif 10 bold", command=self.kaydet)
        self.kaydetbuton.grid(row=2, column=0, padx=20)

        self.temizlebuton = Button(self.frame3, text="TEMİZLE", bg="red", fg="black", width=25, font="serif 10 bold", command=self.temizle)
        self.temizlebuton.grid(row=2, column=1)

        self.mesajkutusu1 = StringVar()
        self.mesaj1 = Entry(self.frame3, text="", width=60, font="serif 10 bold", state="disabled", textvariable=self.mesajkutusu1, justify="center")
        self.mesaj1.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        self.mesaj2 = Label(self.frame3, text="")
        self.mesaj2.grid(row=4, column=0, columnspan=2, padx=20, pady=(0,20))

        self.grid()
        pass

    def hastabilgi(self):
        cursor.execute("SELECT * FROM bilgiislemtablo WHERE tcno=?",(self.tcnoo.get(),))
        data = cursor.fetchall()
        if data:
            for i in data:
                self.iki.set(i[1])
                self.uc.set(i[2])
                if(i[3] == "Kadın"):
                    self.cinsiyet.set(2)
                else:
                    self.cinsiyet.set(1)
                self.dort.set(i[4])
                self.hizmet.set(i[5])
                self.bes.set(i[6])
                self.alti.set(i[7])
                self.yedi.set(i[8])
                self.sekiz.set(i[9])
                self.dokuz.set(i[10])
                self.maliyetmalzeme.set(i[11])
                self.on.set(i[13])
        else:
            self.after(2000, self.after_method)
            self.mesaj2.config(text="Hasta Bilgisi Yok", bg="red", fg="black", font="serif 10 bold", width=25, height=2)
        pass

    def kaydet(self):
        tc = self.tcnoo.get()
        adsoyad = self.hastaadd.get()
        yas = self.hastayass.get()
        hastacinsiyet = self.cinsiyet.get()
        adres = self.hastaadress.get()
        hizmet = self.yapilanhizmett.get()
        tarih = self.tarihh.get()
        malzeme = self.kullanilanmalzemee.get()
        adet = self.malzemeadett.get()
        fiyat = self.malzemefiyatt.get()
        ucret = self.alinanucrett.get()
        hemsiread = self.hemsireadi.get()
        maliyet = int(adet) * int(fiyat)
        kasa = int(ucret) - int(maliyet)
        if(hastacinsiyet == 1):
            hastacinsiyet = "Erkek"
        if(hastacinsiyet == 2):
            hastacinsiyet = "Kadın"
        if((not tc) or (not adsoyad) or (not yas) or (not hastacinsiyet) or (not adres) or (not hizmet) or (not tarih) or (not malzeme) or (not hemsiread)):
            self.after(2000, self.after_method)
            self.mesaj2.config(text="Bazı Bilgiler Eksik", bg="red", fg="black", font="serif 10 bold", width=25, height=2)
        else:
            cursor.execute("Insert Into bilgiislemtablo (tcno,ad_soyad,yas,cinsiyet,adres,yapilanhizmet,tarih,kullanilanmalzeme,malzemeadet,malzemefiyat,alinanucret,malzememaliyet,kasa,hemsireadi) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(tc,adsoyad,yas,hastacinsiyet,adres,hizmet,tarih,malzeme,adet,fiyat,ucret,maliyet,kasa,hemsiread))
            con.commit()
            self.maliyetmalzeme.set(maliyet)
            self.mesajkutusu1.set("Malzeme Maliyeti: {0}, Kasa: {1}".format(maliyet,kasa))
            self.after(2000, self.after_method)
            self.mesaj2.config(text="İşlem Kayıt Edildi", bg="green", fg="black", font="serif 10 bold", width=25, height=2)
        pass

    def after_method(self):
        self.mesaj2.config(text="",bg="#f0f0f0")
    pass
    
    def temizle(self):
        self.bir.set("")
        self.iki.set("")
        self.uc.set("")
        self.dort.set("")
        self.bes.set("")
        self.alti.set("")
        self.yedi.set(0)
        self.sekiz.set(0)
        self.dokuz.set(0)
        self.on.set("")
        self.cinsiyet.set(value=1)
        self.hizmet.set("")
        self.maliyetmalzeme.set(0)
        self.mesajkutusu1.set("")
        pass

def main():
    pencere = Tk()
    cerceve = bilgi_islem(pencere)
    pencere.geometry('1570x390')
    pencere.iconbitmap('favicon.ico')
    pencere.title('Özel Çamlıca Sağlık Kabini')
    pencere.mainloop()
main()
con.close()
