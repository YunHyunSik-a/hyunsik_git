import csv
import requests 
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

filename = "잡플래닛_공공기관-협회.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title="회사명,사업분야,삭제,지역,삭제,삭제,평점,연봉".split(",")
writer.writerow(title)

for i in range(1,86+1):
    url = "https://www.jobplanet.co.kr/companies?industry_id=1000&page={0}".format(i)
    res = requests.get(url, headers=headers) 
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("div",attrs={"class":"section_group"}).find_all("section")
    for row in data_rows:
        columns1= row.find("dt").find_all("a")
        data1 = [column.get_text().strip() for column in columns1]

        columns2 = row.find("dl",attrs={"class":"content_col2_3 cominfo"}).find_all("span")
        data2 = [column.get_text().strip() for column in columns2]

        columns3 = row.find("dl",attrs={"class":"content_col2_4"}).find_all("span")
        data3 = [column.get_text().strip() for column in columns3]

        columns4 = row.find("dl",attrs={"class":"content_col2_4"}).find_all("strong")
        data4 = [column.get_text().strip() for column in columns4]
        data = data1 + data2 + data3 + data4
        writer.writerow(data)
        # print(data)