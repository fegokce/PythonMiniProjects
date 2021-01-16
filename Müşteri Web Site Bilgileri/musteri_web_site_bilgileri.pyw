from tkinter import *
import sqlite3

con = sqlite3.connect("musteri_web_site_bilgileri.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS musteri_web_site_bilgileri 
                (domain_adi TEXT,
                domain_baslangic_tarihi TEXT,
                domain_bitis_tarihi TEXT,
                wp_kullanici_adi TEXT,
                wp_sifre TEXT,
                cpanel_kullanici_adi TEXT,
                cpanel_sifre TEXT,
                google_ads_kullanici_adi TEXT,
                google_ads_sifre TEXT,
                mail_kullanici_adi TEXT,
                mail_sifre TEXT,
                instagram_kullanici_adi TEXT,
                instagram_sifre TEXT)''')

class musteri_web_site_bilgileri(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI(parent)
    def initUI(self, parent):

        self.frame1 = LabelFrame(self, text="", fg="#3b4652", font="serif 13 bold")
        self.frame1.grid(row=0, column=0, pady=(20,0))

        self.domain = StringVar()
        self.domain_adi = Label(self.frame1, text="Domain Adı", fg="#3b4652", font="serif 13 bold")
        self.domain_adi.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        self.domain_adii = Entry(self.frame1, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.domain)
        self.domain_adii.grid(row=0, column=1, padx=(0,10), pady=10)

        self.bul_buton = Button(self.frame1, text="Bul", bg="#42eb88", fg="#3b4652", width=10, font="serif 13 bold", command=self.bul)
        self.bul_buton.grid(row=0, column=2, padx=10)

        self.kaydet_buton = Button(self.frame1, text="Kaydet", bg="#42eb88", fg="#3b4652", width=10, font="serif 13 bold", command=self.kaydet)
        self.kaydet_buton.grid(row=0, column=3, padx=(0,10))

        self.guncelle_buton = Button(self.frame1, text="Güncelle", bg="#42eb88", fg="#3b4652", width=10, font="serif 13 bold", command=self.guncelle)
        self.guncelle_buton.grid(row=0, column=4, padx=(0,10))

        self.sil_buton = Button(self.frame1, text="Sil", bg="#42eb88", fg="#3b4652", width=10, font="serif 13 bold", command=self.sil)
        self.sil_buton.grid(row=0, column=5, padx=(0,10))

        self.temizle_buton = Button(self.frame1, text="Temizle", bg="#42eb88", fg="#3b4652", width=10, font="serif 13 bold", command=self.temizle)
        self.temizle_buton.grid(row=0, column=6, padx=(0,10))

        self.frame2 = LabelFrame(self, text="", fg="#3b4652", font="serif 13 bold")
        self.frame2.grid(row=1, column=0, padx=20, pady=20)

        self.baslangic = StringVar()
        self.domain_baslangic_tarihi = Label(self.frame2, text="Domain Başlangıç Tarihi", fg="#3b4652", font="serif 13 bold")
        self.domain_baslangic_tarihi.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.domain_baslangic_tarihii = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.baslangic)
        self.domain_baslangic_tarihii.grid(row=1, column=1, padx=(0,10), pady=10)
        self.bitis = StringVar()
        self.domain_bitis_tarihi = Label(self.frame2, text="Domain Bitiş Tarihi", fg="#3b4652", font="serif 13 bold")
        self.domain_bitis_tarihi.grid(row=2, column=0, padx=10, pady=(0,20), sticky="W")
        self.domain_bitis_tarihii = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.bitis)
        self.domain_bitis_tarihii.grid(row=2, column=1, padx=(0,10), pady=(0,20))

        self.wp_kullanici = StringVar()
        self.wp_kullanici_adi = Label(self.frame2, text="WordPress Kullanıcı Adı", fg="#3b4652", font="serif 13 bold")
        self.wp_kullanici_adi.grid(row=1, column=2, padx=10, pady=10, sticky="W")
        self.wp_kullanici_adii = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.wp_kullanici)
        self.wp_kullanici_adii.grid(row=1, column=3, padx=(0,10), pady=10)
        self.wp_password = StringVar()
        self.wp_sifre = Label(self.frame2, text="WordPress Şifre", fg="#3b4652", font="serif 13 bold")
        self.wp_sifre.grid(row=2, column=2, padx=10, pady=(0,20), sticky="W")
        self.wp_sifree = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.wp_password)
        self.wp_sifree.grid(row=2, column=3, padx=(0,10), pady=(0,20))

        self.cpanel_kullanici = StringVar()
        self.cpanel_kullanici_adi = Label(self.frame2, text="cPanel Kullanıcı Adı", fg="#3b4652", font="serif 13 bold")
        self.cpanel_kullanici_adi.grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.cpanel_kullanici_adii = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.cpanel_kullanici)
        self.cpanel_kullanici_adii.grid(row=3, column=1, padx=(0,10), pady=10)
        self.cpanel_password = StringVar()
        self.cpanel_sifre = Label(self.frame2, text="cPanel Şifre", fg="#3b4652", font="serif 13 bold")
        self.cpanel_sifre.grid(row=4, column=0, padx=10, pady=(0,20), sticky="W")
        self.cpanel_sifree = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.cpanel_password)
        self.cpanel_sifree.grid(row=4, column=1, padx=(0,10), pady=(0,20))

        self.google_kullanici = StringVar()
        self.google_ads_kullanici_adi = Label(self.frame2, text="Google Ads Kullanıcı Adı", fg="#3b4652", font="serif 13 bold")
        self.google_ads_kullanici_adi.grid(row=3, column=2, padx=10, pady=10, sticky="W")
        self.google_ads_kullanici_adii = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.google_kullanici)
        self.google_ads_kullanici_adii.grid(row=3, column=3, padx=(0,10), pady=10)
        self.google_password = StringVar()
        self.google_ads_sifre = Label(self.frame2, text="Google Ads Şifre", fg="#3b4652", font="serif 13 bold")
        self.google_ads_sifre.grid(row=4, column=2, padx=10, pady=(0,20), sticky="W")
        self.google_ads_sifree = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.google_password)
        self.google_ads_sifree.grid(row=4, column=3, padx=(0,10), pady=(0,20))

        self.mail_kullanici = StringVar()
        self.mail_kullanici_adi = Label(self.frame2, text="E-Mail Kullanıcı Adı", fg="#3b4652", font="serif 13 bold")
        self.mail_kullanici_adi.grid(row=5, column=0, padx=10, pady=10, sticky="W")
        self.mail_kullanici_adii = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.mail_kullanici)
        self.mail_kullanici_adii.grid(row=5, column=1, padx=(0,10), pady=10)
        self.mail_password = StringVar()
        self.mail_sifre = Label(self.frame2, text="E-Mail Şifre", fg="#3b4652", font="serif 13 bold")
        self.mail_sifre.grid(row=6, column=0, padx=10, pady=(0,10), sticky="W")
        self.mail_sifree = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.mail_password)
        self.mail_sifree.grid(row=6, column=1, padx=(0,10), pady=(0,10))

        self.instagram_kullanici = StringVar()
        self.instagram_kullanici_adi = Label(self.frame2, text="İnstagram Kullanıcı Adı", fg="#3b4652", font="serif 13 bold")
        self.instagram_kullanici_adi.grid(row=5, column=2, padx=10, pady=10, sticky="W")
        self.instagram_kullanici_adii = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.instagram_kullanici)
        self.instagram_kullanici_adii.grid(row=5, column=3, padx=(0,10), pady=10)
        self.instagram_password = StringVar()
        self.instagram_sifre = Label(self.frame2, text="İnstagram Şifre", fg="#3b4652", font="serif 13 bold")
        self.instagram_sifre.grid(row=6, column=2, padx=10, pady=(0,10), sticky="W")
        self.instagram_sifree = Entry(self.frame2, text="", width=30, fg="#42eb88", font="serif 13", justify="center", textvariable=self.instagram_password)
        self.instagram_sifree.grid(row=6, column=3, padx=(0,10), pady=(0,10))

        self.mesaj1 = Label(self, text="", fg="#3b4652", font="serif 13 bold")
        self.mesaj1.grid(row=7, column=0, pady=(0,20))

        self.grid()
        pass

    def bul(self):
        cursor.execute("Select * From musteri_web_site_bilgileri Where domain_adi=?",(self.domain_adii.get(),))
        data = cursor.fetchall()
        if data:
            for i in data:
                self.domain.set(i[0])
                self.baslangic.set(i[1])
                self.bitis.set(i[2])
                self.wp_kullanici.set(i[3])
                self.wp_password.set(i[4])
                self.cpanel_kullanici.set(i[5])
                self.cpanel_password.set(i[6])
                self.google_kullanici.set(i[7])
                self.google_password.set(i[8])
                self.mail_kullanici.set(i[9])
                self.mail_password.set(i[10])
                self.instagram_kullanici.set(i[11])
                self.instagram_password.set(i[12])
        else:
            self.after(2000, self.after_method)
            self.mesaj1.config(text="Domain Bilgileri Bulunamadı", bg="#42eb88", fg="#3b4652", font="serif 13 bold", width=30, height=1)
        pass

    def kaydet(self):
        domain = self.domain.get()
        baslangic = self.baslangic.get()
        bitis = self.bitis.get()
        wpkullanici = self.wp_kullanici.get()
        wppassword = self.wp_password.get()
        cpanelkullanici = self.cpanel_kullanici.get()
        cpanelpassword = self.cpanel_password.get()
        googlekullanici = self.google_kullanici.get()
        googlepassword = self.google_password.get()
        mailkullanici = self.mail_kullanici.get()
        mailpassword = self.mail_password.get()
        instagramkullanici = self.instagram_kullanici.get()
        instagrampassword = self.instagram_password.get()
        if(not domain):
            self.after(2000, self.after_method)
            self.mesaj1.config(text="Domain Adı Girilmedi", bg="#42eb88", fg="#3b4652", font="serif 13 bold", width=30, height=1)
        else:
            cursor.execute("Insert Into musteri_web_site_bilgileri(domain_adi, domain_baslangic_tarihi, domain_bitis_tarihi, wp_kullanici_adi, wp_sifre, cpanel_kullanici_adi, cpanel_sifre, google_ads_kullanici_adi, google_ads_sifre, mail_kullanici_adi, mail_sifre, instagram_kullanici_adi, instagram_sifre) values(?,?,?,?,?,?,?,?,?,?,?,?,?)", (domain, baslangic, bitis, wpkullanici, wppassword, cpanelkullanici, cpanelpassword, googlekullanici, googlepassword, mailkullanici, mailpassword, instagramkullanici, instagrampassword))
            con.commit()
            self.after(2000, self.after_method)
            self.mesaj1.config(text="Domain Bilgileri Kayıt Edildi", bg="#42eb88", fg="#3b4652", font="serif 13 bold", width=30, height=1)
        pass

    def guncelle(self):
        domain = self.domain.get()
        baslangic = self.baslangic.get()
        bitis = self.bitis.get()
        wpkullanici = self.wp_kullanici.get()
        wppassword = self.wp_password.get()
        cpanelkullanici = self.cpanel_kullanici.get()
        cpanelpassword = self.cpanel_password.get()
        googlekullanici = self.google_kullanici.get()
        googlepassword = self.google_password.get()
        mailkullanici = self.mail_kullanici.get()
        mailpassword = self.mail_password.get()
        instagramkullanici = self.instagram_kullanici.get()
        instagrampassword = self.instagram_password.get()
        if(not domain):
            self.after(2000, self.after_method)
            self.mesaj1.config(text="Güncellenecek Domain Adı Yok", bg="#42eb88", fg="#3b4652", font="serif 13 bold", width=30, height=1)
        else:
            sql_update_query = "Update musteri_web_site_bilgileri Set domain_adi = ?, domain_baslangic_tarihi = ?, domain_bitis_tarihi = ?, wp_kullanici_adi = ?, wp_sifre = ?, cpanel_kullanici_adi = ?, cpanel_sifre = ?, google_ads_kullanici_adi = ?, google_ads_sifre = ?, mail_kullanici_adi = ?, mail_sifre = ?, instagram_kullanici_adi = ?, instagram_sifre = ? Where domain_adi = ?"
            data = (domain, baslangic, bitis, wpkullanici, wppassword, cpanelkullanici, cpanelpassword, googlekullanici, googlepassword, mailkullanici, mailpassword, instagramkullanici, instagrampassword, domain)
            cursor.execute(sql_update_query, data)
            con.commit()
            self.after(2000, self.after_method)
            self.mesaj1.config(text="Domain Bilgileri Güncellendi", bg="#42eb88", fg="#3b4652", font="serif 13 bold", width=30, height=1)
        pass

    def sil(self):
        domain = self.domain.get()
        if(domain):
            cursor.execute("Delete From musteri_web_site_bilgileri Where domain_adi=?",(self.domain_adii.get(),))
            con.commit()
            self.after(2000, self.after_method)
            self.mesaj1.config(text="Domain Bilgileri Silindi", bg="#42eb88", fg="#3b4652", font="serif 13 bold", width=30, height=1)
            self.domain.set("")
            self.baslangic.set("")
            self.bitis.set("")
            self.wp_kullanici.set("")
            self.wp_password.set("")
            self.cpanel_kullanici.set("")
            self.cpanel_password.set("")
            self.google_kullanici.set("")
            self.google_password.set("")
            self.mail_kullanici.set("")
            self.mail_password.set("")
            self.instagram_kullanici.set("")
            self.instagram_password.set("")
        else:
            self.after(2000, self.after_method)
            self.mesaj1.config(text="Silinecek Domain Bilgisi Yok", bg="#42eb88", fg="#3b4652", font="serif 13 bold", width=30, height=1)
        pass

    def temizle(self):
        self.domain.set("")
        self.baslangic.set("")
        self.bitis.set("")
        self.wp_kullanici.set("")
        self.wp_password.set("")
        self.cpanel_kullanici.set("")
        self.cpanel_password.set("")
        self.google_kullanici.set("")
        self.google_password.set("")
        self.mail_kullanici.set("")
        self.mail_password.set("")
        self.instagram_kullanici.set("")
        self.instagram_password.set("")
        pass

    def after_method(self):
        self.mesaj1.config(text="", bg="#f0f0f0")
    pass

def main():
    pencere = Tk()
    cerceve = musteri_web_site_bilgileri(pencere)
    pencere.iconbitmap('favicon.ico')
    pencere.title('Atılım Web | Müşteri Web Site Bilgileri')
    pencere.mainloop()
main()
con.close()
