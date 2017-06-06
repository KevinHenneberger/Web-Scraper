import requests
from bs4 import BeautifulSoup
import re
import json

class WebScraper:

    def __init__(self, url):
        self.r = requests.get(url)
        self.c = self.r.content
        self.soup = BeautifulSoup(self.c, 'html.parser')

    def scrape(self):

        table = self.soup.find(class_='infobox vcard')
        trs = table.find_all('tr')

        name = table.caption.get_text()
        number = re.findall(r'\d+', trs[1].get_text().strip().split(' – ')[0])[0]
        team = trs[1].get_text().strip().split(' – ')[1]
        position = trs[2].a.get_text()
        age = re.findall(r'\d+', trs[5].find_all('span')[2].get_text())[0]
        height = trs[7].td.get_text()[0] + "'" + trs[7].td.get_text()[5] + '"'
        weight =  trs[8].td.get_text()[:3]

        self.bio = {
            "name": name,
            "number": number,
            "team": team,
            "position": position,
            "age": age,
            "height": height,
            "weight": weight
        }

        fptr = open('data.json', 'w')
        fptr.write(json.dumps(self.bio, indent=4))
        fptr.close()

    def __str__(self):
        return str(self.bio)
