import csv
import requests 
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

# filename = "경영,사무 직무별 회사 연봉 데이터.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f)
# title="연봉 회사명  사업분야".split("\t")
# writer.writerow(title)

# for i in range(1,2):
    url = "https://www.jobkorea.co.kr/Salary/Index?coKeyword=&tabindex=2&indsCtgrCode=&indsCode=&jobTypeCode=10012&haveAGI=0&orderCode=2&coPage={0}#salarySearchCompany".format(i)
    res = requests.get(url, headers=headers) 
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("ul",attrs={"id":"listCompany"}).find_all("li")
    for row in data_rows:
        columns= row.find_all("div")
        if len(columns)<=1:
            continue
        data1 = [column.get_text().strip() for column in columns]
        print(data1)
        # data2 =  list(set(data1))
        # trash = list()
        # search1="\n"
        # search2="채용중"
        # search3="매출액"
        # search4="사원수"
        # for datas in data2:
        #     if search1 in datas or search2 in datas or  search3 in datas or search4 in datas:
        #         trash.append(datas)
        # data=list(set(data2)-set(trash))
        # data.sort()
        # #writer.writerow(data)
        # print(data)
    