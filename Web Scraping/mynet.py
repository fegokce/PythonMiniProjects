import requests
from bs4 import BeautifulSoup

url = "https://www.mynet.com/"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

haberler = soup.find_all("ul", {"class" : "box-news-item row"})[1].find_all("li")

print("***** Mynet Haberler *****".center(100))

for haber in haberler:
    haber_linki = haber.find("a")["href"]
    haber_basligi = haber.find("a")["title"]

    print("********************")
    print(f"Haber Başlığı: {haber_basligi}\nHaber Linki: {haber_linki}")