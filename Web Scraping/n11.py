import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class" : "column"}, limit= 5)

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    old_price = li.find("div", {"class" : "proDetail"}).find_all("a")[0].text.strip().strip("TL")
    new_price = li.find("div", {"class" : "proDetail"}).find_all("a")[1].text.strip().strip("TL")

    print(f"name: {name}, link: {link}, old price: {old_price}, new price: {new_price}")