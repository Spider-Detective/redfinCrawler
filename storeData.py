import csv
import json
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import validators

base_path = '/Users/zixxu/Downloads/'
work_path = '/Users/zixxu/Documents/Learning/crawler/'

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless
# install using driver manager to avoid cannot found error
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# add missing support for chrome "send_command"  to selenium webdriver
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': base_path}}
command_result = driver.execute("send_command", params)

# store the data to json
for filename in os.listdir(base_path):
    print("[Info] Check file: " + filename)
    if re.match("redfin.*.csv", filename):
        print("[Info] Start store data...")
        csvfile = open(os.path.join(base_path, filename), 'r')
        jsonfile = open(os.path.join(work_path, 'output.json'), 'w')
        fieldnames = ("SALE TYPE", "SOLD DATE", 
                      "PROPERTY TYPE", "ADDRESS", 
                      "CITY", "STATE", "ZIP CODE", 
                      "PRICE", "BEDS", "BATHS", 
                      "LOCATION", "SQUARE FEET", 
                      "LOT SIZE", "YEAR BUILT", 
                      "DAYS ON MARKET", "$/SQUARE FEET", 
                      "HOA", "STATUS", 
                      "NEXT OPEN HOUSE START TIME", 
                      "NEXT OPEN HOUSE END TIME", 
                      "URL", "SOURCE", "MLS#", 
                      "FAVORITE", "INTERESTED", 
                      "LATITUDE", "LONGITUDE")
        reader = csv.DictReader(csvfile, fieldnames)
        jsonfile.write('test = \'[')
        for row in reader:
            print(row['URL'])
            if validators.url(row['URL']):
                driver.get(row['URL'])
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                img_ul = soup.find_all('img', {"class": "img-card"})
                if len(img_ul) > 0:
                    img = img_ul[0]
                    url = img['src']
                    row['IMG_URL'] = url
                else:
                    print("[Warn] No image exists for this property: " + row['URL'])
                
                schools = soup.find_all('div', {"class": "school-title"})
                schoolNames = []
                for school in schools:
                    schoolNames.append(school.string)
                row['SCHOOLS'] = schoolNames

                ratings = soup.find_all('span', {"class": "rating-num"})
                ratingScores = []
                for rating in ratings:
                    ratingScores.append(rating.string)
                row['RATINGS'] = ratingScores
            else:
                print("[Warn] Unnecessary or Invalid url: " + row['URL'])
            json.dump(row, jsonfile)
            jsonfile.write(',')
        jsonfile.seek(jsonfile.tell() - 1)    #This will shift pointer to that place (one line up)
        jsonfile.truncate()
        jsonfile.write(']\'')
        jsonfile.close()

print("[Info] Writing data success!")
driver.close()
