import operator #liste içindeki verileri sıralamak ve birden fazla olan veriyi silmek için "operator" import edildi
from recommendations import * #"recommendations" dosyası içindeki gerekli fonksiyonları kullanmak için import edildi("recommendations" dosyası bu uygulamaya çağrıldı)
from tkinter import * #arayüz tasarımı için "tkinter" kütüphanesi kullanıldı
import tkinter.filedialog #kullanıcı kendi istediği dosyayı uygulamaya yüklemek için "tkinter.filedialog" kütüphanesi kullanıldı
from tkinter import filedialog as fd #kullanıcının yüklediği dosyayı okumak için kütüphane içinden import edildi
from tkinter.ttk import Combobox #arayüz tasarımında combobox'ı kullanmak içinde kütüphane içinden import edildi

#"cerceve" adında bir adet frame oluşturuldu ve uygulama içinde yapılan işlemler bunun içinde yer alıyor
class cerceve(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI(parent)
    def initUI(self, parent):
        self.chkValue = IntVar() #"radibutton" seçili gelmesi için "IntVar" tanımlanıldı(daha sonra gerekli yerde "textvariable" ile çağırılacak)
        self.chkValue.set(1) #ilk başta "pearson" seçili gelsin diye 1 olarak güncellenildi
        self.tavsiye = IntVar() #kullanıcı tavsiye miktarını girmesi için "IntVar" tanımlanıldı(daha sonra gerekli yerde "textvariable" ile çağırılacak)
        self.tavsiye.set(3) #ilk başta tavsiye miktarı 3 gelmesi için güncellenildi
        self.box_value = StringVar() #kullanıcı "depo.txt" dosyasını yükledikten sonra filtre kısmına yazılım dillerini yüklemek için "StringVar" tanımlanıldı(daha sonra gerekli yerde "textvariable" ile çağırılacak)

        #aşağıdakiler arayüzde yer alması gereken widgetler için eklenildi ve gerekli özellikleri verildi
        self.baslik = Label(self, text="Github Depo Önerici", bg="orange", fg="white", font="serif 15 bold", width=80)
        self.baslik.grid(row=0, column=0, columnspan=5)
        self.kullanici_verisi = Button(self, text="Kullanıcı Verisi Yükle", height=2, command=self.kullaniciveri) #buton içine gerekli fonskiyon "command" methodu ile çağrıldı
        self.kullanici_verisi.grid(row=1, column=0, pady=(10,70), padx=(10,0))
        self.bos1 = Label(self, text=" ", bg="grey", height=2, width=43)
        self.bos1.grid(row=1, column=1, pady=(10,70))
        self.depo_verisi = Button(self, text="Depo Verisi Yükle", height=2, command=self.depoverisi) #buton içine gerekli fonskiyon "command" methodu ile çağrıldı
        self.depo_verisi.grid(row=1, column=2, pady=(10,70))
        self.bos2 = Label(self, text=" ", bg="grey", height=2, width=43)
        self.bos2.grid(row=1, column=3, pady=(10,70))
        self.yıldız_verisi = Button(self, text="Yıldız Verisi Yükle", height=2, command=self.yildizverisi) #buton içine gerekli fonskiyon "command" methodu ile çağrıldı
        self.yıldız_verisi.grid(row=1, column=4, pady=(10,70), padx=(0,10))

        #ayrı bir frame oluşturulup diğer widgetlerden ayrımak için tekrar widgetler eklenildi ve gerekli özellikleri verildi
        frame1 = Frame(self)
        frame1.grid(row=2, columns=2, sticky=W)
        self.mesaj1 = Label(frame1, text="Şunun için Depo Öner :")
        self.mesaj1.grid(row=3, column=0, padx=(10,0), pady=10)
        self.depo_oner_listebox = Listbox(frame1, height=20, width=30)
        self.depo_oner_listebox.grid(row=4, column=0, padx=(10,0))
        self.mesaj3 = Label(frame1, text="Programlama Diline Göre Filtrele :")
        self.mesaj3.grid(row=5, column=0, padx=(10,0), pady=10)
        self.filtre_combobox = Combobox(frame1, textvariable=self.box_value, state='readonly') #kullanıcı "depo.txt" dosyasını yükledikten sonra "box_value" içinde yazılım dilleri yer alması için "combobox" içine tanımlanıldı
        self.filtre_combobox.grid(row=6, column=0, padx=(10,0))
        self.mesaj4 = Label(frame1, text="Benzerlik Algoritması :")
        self.mesaj4.grid(row=7, column=0, padx=(10,0), pady=10)
        self.pearson = Radiobutton(frame1, text="Pearson", variable=self.chkValue,value=1) #yukarıda "radiobuton" için oluşturduğumuz "chkValue"'nin value değeri 1 olarak eklenildi yani program açıldığı zaman direk bu "radiobuton" otomatik olarak seçilecek
        self.pearson.grid(row=8, column=0, padx=(10,0))
        self.oklid = Radiobutton(frame1, text="Öklid", variable=self.chkValue,value=2) #"radibuton" varsayılan değeri 1 fakat kullanıcı eğer 2 yi seçerse aşağıdaki fonksiyonlar içinde ona göre işlem yapılacak
        self.oklid.grid(row=9, column=0, padx=(10,0), pady=10)
        self.mesaj5 = Label(self, text="Tavsiye Miktarı :")
        self.mesaj5.grid(row=10, column=0, padx=(10,0))
        self.entry = Entry(self, text="", width=5, textvariable=self.tavsiye) #yukarıda tavsiye olarak oluşturduğumuz argümanı burada tanımladık ve varsayılan değeri program açılınca 3 olarak gelecek
        self.entry.grid(row=10, column=1, padx=(10,0), pady=10, sticky=W)

        #başka bir frame oluşturulup diğer widgetlerden ayrımak için tekrar widgetler eklenildi ve gerekli özellikleri verildi
        frame2 = Frame(self)
        frame2.grid(row=2, columns=2, padx=(150,0), pady=(60,0))
        self.depo_tavsiye = Button(frame2, text="Depo Tavsiye Et", height=2, command=self.depo_tavsiye)
        self.depo_tavsiye.grid(row=3, column=0)
        self.github_tavsiye = Button(frame2, text="Github Kullanıcısı Tavsiye Et", height=2, command=self.github_tavsiye)
        self.github_tavsiye.grid(row=4, column=0)

        #son bir frame oluşturulup diğer widgetlerden ayrımak için tekrar widgetler eklenildi ve gerekli özellikleri verildi
        frame3 = Frame(self)
        frame3.grid(row=2, columns=5, sticky=E)
        self.mesaj2 = Label(frame3, text="Tavsiyeler")
        self.mesaj2.grid(row=3, column=0, padx=(0,10), pady=(0,10))
        self.tavsiye_listbox = Listbox(frame3, height=30, width=30)
        self.tavsiye_listbox.grid(row=4, column=0, padx=(0,10))

        #gerekli sözlükler oluşturulup kullanıcın yüklediği .txt'ler ile işleme alınacak
        self.yildiz_sözlük = {} #kullanıcının yüklediği "yildiz.txt" içindeki veriler bu sözlük içine oluşturmak için boş bir sözlük oluşturuldu
        self.kullanıcı_id_dict = {} #kullanıcının yüklediği "kullanici.txt" içindeki veriler bu sözlük içine oluşturmak için boş bir sözlük oluşturuldu
        self.depo_id_dict = {} #kullanıcının yüklediği "depo.txt" içindeki veriler bu sözlük içine oluşturmak için boş bir sözlük oluşturuldu

        self.grid()

    #kullanıcı, "yildiz.txt" dosyasını yükledikten sonra aşağıdaki fonksiyon içindeki kodlar çalışacak
    def yildizverisi(self):
        self.yildiz = fd.askopenfile() #kullanıcının yüklediği dosya burada açılacak
        for satir in self.yildiz: #yüklenilen dosya içindeki veriler for döngüsü ile dönecek
            self.user_id=satir.split('\t')[0] #"satir"ı "split" methodu ile ayırıp 1. indexi "user_id" içine aktarıldı('t' ile bitenler ayrıldı)
            self.id_1=satir.split('\t')[1].strip('\n') #"satir"ı "split" methodu ile ayırıp 2. indexi "id_1" içine aktarıldı('\t' ile bitenler ayrıldı ve '\n' ile bitenler silindi)
            self.id_2=self.id_1.split((',')) #2.index içinde yer alan verileri tekrar ',' ile ayırıp "id_2" içine aktarıldı
            self.yildiz_sözlük.setdefault(self.user_id,{}) #program başında belirtilen boş sözlük içine "key=user_id", "value=boş bir sözlük" eklenildi
            for i in range(len(self.id_2)): #2.index içindeki verileri uzunluğa kadar döngüye sokuldu
                self.yildiz_sözlük[self.user_id].setdefault(self.depo_id_dict[self.id_2[i]],5) #"yildiz_sözlük" artık {"user_id" : {"id_2" : 5} şeklinde iç içe sözlük oluşturuldu

    #kullanıcı, "depo.txt" dosyasını yükledikten sonra aşağıdaki fonksiyon içindeki kodlar çalışacak
    def depoverisi(self):
        filtre_listesi = [] #filtrelemek için boş bir liste oluşturuldu
        filtre_listesi.insert(0,"Hepsi") #boş listenin "0." indexine "Hepsi" verisi eklenildi
        self.box_value.set('Hepsi') #dosya yüklendikten sonra "combobox" içinde "Hepsi" verisi otomatik olarak kullanıcıya aktarılıcak
        self.depo = fd.askopenfile() #kullanıcının yüklediği dosya burada açılacak
        for satir in self.depo.readlines(): #yüklenilen dosya içindeki veriler for döngüsü ile dönecek
            veri = satir.split(',') #dosyanın içindekileri "," ile ayırıp veri içine atıldı
            filtre_dili = veri[3] #dosyanın içindeki 3. veriler "filtre_dili" içine atıldı
            filtre_listesi.append(filtre_dili) #"filtre_listesi" içine "filtre_dili" eklenildi
            self.depo_id_dict.setdefault(veri[0], veri[1]) #"depo_id_dict" sözlüğü içerisine "key=veri[0]" yani "id", "value=[1]" yani "depo" numaraları eklenildi
        self.filtre_combobox['values'] = sorted(set(filtre_listesi)) #"filtre_listesi" içindeki "filtre_dili" "combobox" içine aktarıldı(alfabetik ve tekrar eden veriler silindi)

    #kullanıcı, "kullanıcı.txt" dosyasını yükledikten sonra aşağıdaki fonksiyon içindeki kodlar çalışacak
    def kullaniciveri(self):
        self.depo_oner_listebox.delete(0,END) #her butona basıldığı zaman "depo_oner_listebox" temizlenecek
        self.kullanici = fd.askopenfile() #kullanıcının yüklediği dosya burada açılacak
        for satir in self.kullanici.readlines(): #yüklenilen dosya içindeki veriler for döngüsü ile dönecek
            veri = satir.split(',') #dosyanın içindekileri "," ile ayırıp "veri" içine atıldı
            self.kullanıcı_id_dict.setdefault(veri[1],veri[0]) #"kullanıcı_id_dict" sözlüğünün içine kullanıcının yüklediği dosyadan "isim" ve "id"'ler yer alıcak yani key'ler isim value'ler id olucak
        for ad,id in self.kullanıcı_id_dict.items(): #sözlük içindeki verileri alarak "ad" ve "id" içine atıldı
            self.depo_oner_listebox.insert(END,ad) #sözlükten alınan "ad" uygulamadaki "depo_oner_listebox"'a yazılacak

    #kullanıcı github tavsite et butonuna bastığı zaman aşağıdaki fonksiyon içindeki kodlar çalışacak
    def github_tavsiye(self):
        pass

    #kullanıcı depo tavsite et butonuna bastığı zaman aşağıdaki fonksiyon içindeki kodlar çalışacak
    def depo_tavsiye(self):
        pass

#"main" fonksiyonu içerisine 1 adet pencere, 1 adet yukarıda belirtilen "cervere" "pencere" içine tanımlandı ve son olarak "pencere" adı verildi
def main():
    pencere = Tk()
    class1 = cerceve(pencere)
    pencere.title("Github Depo Önerici")
    pencere.mainloop()
main()