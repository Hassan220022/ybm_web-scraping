import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

# Generate a unique filename based on the current date and time
filename = datetime.now().strftime("myip_(%Y,%m,%d)_(%H:%M:%S).csv")
# web scrapping for myip.ms

data = input("please enter a url like ('https://myip.ms/browse/sites/1/sort/6#sites_tbl_top') don't skip a part: ")

page = requests.get(data)

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")


    web_site = soup.find_all("tbody")

    site=[]
    def get_site_name(web_site):
        rank_=[]
        row_name = web_site[0].find_all('td', {'class': 'row_name'})
        number_of_visites = web_site[0].find_all('span', {'class': 'bold arial grey'})
        for i in range(len(number_of_visites)):
                        number=number_of_visites[i].text.strip()
                        if number[0] == '#':
                            number__ = number.replace('# ', '')
                            rank_.append(number__)
        for i in range(len(row_name)):
            name = row_name[i].text.strip()
            rank=number_of_visites[i].text.strip().replace('# ', '').replace('\n', '')
            site.append({"number":i+1,"web site":name,"rank":rank_[i]})
    get_site_name(web_site)
    keys = site[0].keys()
    with open(filename,'w',newline='') as webfile:
        dict_writer =csv.DictWriter(webfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(site)
    print("done")
main(page)

