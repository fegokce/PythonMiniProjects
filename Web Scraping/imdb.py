import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class" : "lister-list"}).find_all("tr", limit = 100)
count = 1

for tr in list:
    title = tr.find("td", {"class" : "titleColumn"}).find("a").text
    year = tr.find("td", {"class" : "titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td", {"class" : "ratingColumn imdbRating"}).find("strong").text
    
    print(f"{count}-) Film Adı: {title.ljust(100)}, Yıl: {year.ljust(10)}, Değerlendirme: {rating}")
    count += 1   