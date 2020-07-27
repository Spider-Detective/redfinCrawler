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
import smtplib
import ssl
from email import encoders
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
            print("[Info] Working on getting: " + row['URL'])
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

####################################
# send http request for the json data

####################################
# send notification email
sender_email = 'eldritchTest1@gmail.com'
password = 'P@ss1234'

context = ssl.create_default_context()

# 端口465好像是在gmail官方说明里查的，具体忘了
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)

    def send_mail(subject, mail_text, mail_address):

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = mail_address
        text = mail_text
        part1 = MIMEText(text, "plain")
        message.attach(part1)

        text = message.as_string()

        server.sendmail(
            sender_email, mail_address, message.as_string())

    mail_text = 'Hi Zixi and Miao, \nThis is your Robot. \
                 I have pulled the data from Redfin for you. \
                 Please have a look.\n Have a great day!'
    receiver = 'Zixi'
    mail_address = 'xduniverse@hotmail.com'
        
    subject = f"{receiver}, the Redfin data is updated"
    send_mail(subject, mail_text, mail_address)
    print("[Info] Email to " + receiver + " is sent!")
