from tkinter import * #burada tkinter kütüphanesini projemizde kullanmak için importladık.
import sqlite3 #yapılan verileri bir yerde saklamak için sqlite3 veritabanı kullanarak verileri kalıcı olarak sakladım

con = sqlite3.connect("restoran.db") #veri tabanı adı oluşturdum
cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS rezervasyon (masano TEXT,ad TEXT,telno TEXT)')#oluşturduğum veritabanına tablo ekledim

#restoran isimli bir class oluşturdum ve yazağım kodlar classın içine yani oluşturduğum pencere içinde yer alacak.
class restoran(Frame):
    #burdaki 2 fonkisyonda tkintera ait label,buton gibi özellikleri kullanmak için fonksiyon oluşturdum ve self, parent değerlerini içe attım.
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI(parent)
    def initUI(self, parent):
        self.var = StringVar()
        self.ad = StringVar()
        self.telno = StringVar()

        #projenin görünümü için gerekli widgetleri buraya koydum ve görselleri kullanıcı ile buluşturdum.
        self.baslik = Label(self, text="Restoran Rezervasyon Sistemi", bg="blue", width=130, fg="white", font="serif 15")
        self.baslik.grid(pady=10, padx=10, row = 0, column = 0, columnspan = 20)

        self.label1 = Label(self, text="Masa :")
        self.label1.grid(row = 1, column = 0, sticky = EW)

        self.label2 = Label(self, padx=10, textvariable=self.var)
        self.label2.grid(row = 1, column = 1, sticky = W)
        self.var.set("[Seçilmedi]")

        self.label3 = Label(self, text="Müşterinin İsmi :")
        self.label3.grid(row = 1, column = 2, sticky = EW)

        self.entry1 = Entry(self, text="", width="15", textvariable=self.ad)
        self.entry1.grid(row = 1, column = 3, sticky = EW)

        self.label4 = Label(self, text="Müşterinin Telefon Numarası :")
        self.label4.grid(row = 1, column = 4, sticky = EW)

        self.entry2 = Entry(self, text="", width="15", textvariable=self.telno)
        self.entry2.grid(row = 1, column = 5, sticky = EW)

        self.guncelle_kaydet_buton = Button(self, text="Rezervasyon Kaydet/Güncelle", command = self.guncelle_kaydet)
        self.guncelle_kaydet_buton.grid(row = 1, column = 6, sticky = EW, padx=10)

        self.sil_buton = Button(self, text="Rezervasyon Sil", command = self.kayit_sil)
        self.sil_buton.grid(row = 1, column = 7, sticky = EW)

        self.label5 = Label(self, text="")
        self.label5.grid(row = 1, column = 8, sticky = EW, padx=10)

        #butonları kapsıcak bir çerceve oluşturdum
        frame = Frame(self, relief="solid", bd=5)
        frame.grid(row = 2, columns = 5, padx=20, pady=20)

        #tek tek 15 masa için buton koymak yerine for döngüsü ile 1'den 15 sayısına kadar buton koyup nerede yer alacaklarını belirttim.
        x = 1
        for row_index in range (2,5):
            for column_index in range(0,5):
                self.buton = Button(frame, text = str(x+column_index), bg="green", width=10, height=3)
                self.buton.grid(row = row_index, column=column_index, padx=30, pady=25)
                self.buton.bind("<Button -1>", self.masano)
            x += 5

        self.grid()
        pass

    #masa numaralarını göstermek için masano fonskiyonu oluşturdum
    def masano(self,goster):
        #butona bastığı zaman buton numaralarını göstermesi için widget komutunu kullandım ve select sql komutu ile veritabanından verileri çektim
        self.numara = goster.widget#burda masa numarasını diğer fonksiyonalar içerisinde kullanmak için "numara"'ya atadım ve her yerde masa numarasını görmek için
        self.var.set(goster.widget['text']) 
        cursor.execute("SELECT * FROM rezervasyon WHERE masano=?",(self.var.get(),))
        data = cursor.fetchall()
        #eğer veritabınında masa numarasına ait rezervasyon var ise kontrol edip kullanıcıya aktardım
        if data:
            #veritabanı içindeki verileri for döngüsü ile "i" içerisine alıp kullanıcıya aktarmak için for döngüsünü kullandım
            for i in data:
                self.var.set(i[0])
                self.ad.set(i[1])
                self.telno.set(i[2])
                #burda ise eğer daha önceden rezervasyon edilmiş durumunda buton rengi kırmızı rengine dönüyor
                if data[0][0] == self.var.get():
                    goster.widget.config(bg="red")
        #olmaması durumunda eğer eskiden seçilen rezervasyonu kullanıcı görmemesi için sadece masa numarasını gösterip diğer değerleri boş bıraktım
        else:
            self.ad.set('')
            self.telno.set('')
        con.commit()
        pass
    
    #rezervasyon kaydı için sil guncelle_kaydet fonksiyonu oluşturdum
    def guncelle_kaydet(self):
        #masa numarası ,ad ,telefon numaralarını kullanıcının girmesi ile çektim
        masano = self.var.get()
        ad = self.ad.get()
        telno = self.telno.get()
        #daha sonra çektiğim bilgilerinin boş olmaması sonucunda gerekli sql kodu yazarak işlemi ikinci bir kontrol için if parametresini kullandım
        if masano and ad and telno:
            #burda kullancı eğer telefon numarasını integer değerde girerse sql kodu çalıştırarak gerekli mesajı kullanıcıya aktardım
            if telno.isdigit():
                cursor.execute("Insert Into rezervasyon (masano,ad,telno) values(?,?,?)",(self.var.get(),self.entry1.get(), self.entry2.get()))
                con.commit()
                self.after(2000, self.after_method)
                self.label5.config(bg="green",text="Rezervasyon Oluşturuldu")
                self.numara.config(bg="red") #masano fonskiyonu içerisinde "goster.widget" komutunu numara içerisine aktararak guncelle_kaydet fonskiyonu içerisinde masa numarasının rengini değiştirmek için bu kodu yazdım.
                self.var.set('[Seçilmedi]')
                self.ad.set('')
                self.telno.set('')
            #eğer kullanıcı telefon numarasını string bir değerde girerse ona gerekli mesajı verdim
            else:
                self.var.set('[Seçilmedi]')
                self.ad.set('')
                self.telno.set('')
                self.after(2000, self.after_method)
                self.label5.config(bg="red",text="Tel. No Yalnızca Rakam İçermelidir")
        #burda ise kullanıcının bilgileri ekisk girmesi durumunda kullanıcıya gerekli mesajı ilettim
        else:
            self.var.set('[Seçilmedi]')
            self.ad.set('')
            self.telno.set('')
            self.after(2000, self.after_method)
            self.label5.config(bg="red",text="Rezervasyon İçin Eksik Bilgi")
        pass
    
    #rezervasyon silmek için kayit_sil fonksiyonu oluşturdum
    def kayit_sil(self):
        #masa numarası ,ad ,telefon numaralarını kullanıcının girmesi ile çektim
        masano = self.var.get()
        ad = self.ad.get()
        telno = self.telno.get()
        #daha sonra çektiğim bilgilerinin boş olmaması sonucunda gerekli sql kodu yazarak işlemi kullanıcıya olumlu bir mesaj ile aktardım
        if masano and ad and telno:
            cursor.execute("DELETE FROM rezervasyon WHERE masano=?",(self.var.get(),))
            con.commit()
            self.after(2000, self.after_method)
            self.label5.config(bg="red",text="Rezervasyon Silindi")
            self.numara.config(bg="green")#masano fonskiyonu içerisinde "goster.widget" komutunu "numara" içerisine aktararak kayit_Sil fonskiyonu içerisinde masa numarasının rengini değiştirmek için bu kodu yazdım.
            self.var.set('[Seçilmedi]')
            self.ad.set('')
            self.telno.set('')
        #çektiğim bilgiler eğer boş ise sql kod yazmadan kullancıya uyarı mesajı aktardım
        else:
            self.var.set('[Seçilmedi]')
            self.ad.set('')
            self.telno.set('')
            self.after(2000, self.after_method)
            self.label5.config(bg="red",text="Silinecek Rezervasyon Yok")
        pass

    #after methodunu kullanmak için fonksiyon oluşturudm ve gerekli yerde lazım olunca bu fonsiyonu çağırdım
    def after_method(self):
        self.label5.config(text="",bg="#f0f0f0")
        pass

#main fonksiyonu içerinde bir adet pencere ve oluşturduğum pencerenin adını belirledim, ek olarak restoran isimli bir class oluşturarak pencere içine aktardım.
def main():
    pencere = Tk()
    hesap = restoran(pencere)
    pencere.title("Restoran Rezervasyon Sistemi")
    pencere.mainloop()
main()
con.close()