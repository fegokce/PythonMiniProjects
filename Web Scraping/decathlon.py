import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.decathlon.com.tr/C-531486-erkek-tisortu"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

urunler = soup.find_all(id = "products_list")[0].find_all(class_ = "thumbnails-list thumbnails-list-modele")[0].find_all("li")

with open("erkek_tisortler.csv", "w", newline = '', encoding = 'utf-8') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["urun_linki", "urun_resmi", "urun_adi", "urun_markasi"])

    for urun in urunler:
        urun_linki = "https://www.decathlon.com.tr/" + urun.find("a")["href"]
        for resim in urun.find_all("img", attrs={'class':'product-picture swiper-lazy img-lazy product_visuel'}):
            urun_resmi = resim["data-src"]
        urun_adi = urun.find("h3").string
        urun_markasi = urun.find("p").string

        csv_writer.writerow([urun_linki, urun_resmi, urun_adi, urun_markasi])

with open("erkek_tisortler.csv", "r", newline = '', encoding = 'utf-8') as csv_file:
    oku = csv_file.readlines()
    for i in oku:
        print("ürün linki: " + i.split(",")[0] + "\nürün resmi: " + i.split(",")[1] + "\nürün adı: " + i.split(",")[2] + "\nürün markası: " + i.split(",")[3])
        print("********************".center(50))