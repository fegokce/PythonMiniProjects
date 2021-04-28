import requests
from bs4 import BeautifulSoup

headers_param = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
html = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm", headers = headers_param).content

soup = BeautifulSoup(html, "html.parser")

jobs = soup.find("div", {"class" : "container mt-std"}).find_all("div", {"class" : "row listingBody d-flex align-items-center py-std"})
count = 1

for job in jobs:
    job_name = job.find("a").text
    min_salary = job.find("div", {"class" : "col-6 col-lg-4 dataPoint"}).text.strip("Median Base Salary")
    satisfaction = job.find_all("div", {"class" : "col-6 col-lg-4 dataPoint"})[1].text.strip("Job Satisfaction")
    opportunity =  job.find_all("div", {"class" : "col-6 col-lg-4 dataPoint"})[2].text.strip("Job Openings")
    count += 1

    print(f"{count}-) Job Name: {job_name}, Median Base Salary: {min_salary}, Job Satisfaction: {satisfaction}, Job Openings: {opportunity}")