from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json
import os
import re

URL = "https://www.redfin.com/city/9361/CA/Irvine/filter/max-price=750k,max-beds=3,min-baths=2"
base_path = '/Users/zixxu/Downloads/'

for filename in os.listdir(base_path):
	if re.match("redfin.*.csv", filename):
		os.remove(os.path.join(base_path, filename))

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless
# install using driver manager to avoid cannot found error
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# add missing support for chrome "send_command"  to selenium webdriver
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': base_path}}
command_result = driver.execute("send_command", params)

driver.get(URL)
# driver.find_element_by_id("download-and-save").click()
dataLink = driver.find_element_by_id("download-and-save").get_attribute('href')
driver.get(dataLink)
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()

# store the data to json
for filename in os.listdir(base_path):
	if re.match("redfin.*.csv", filename):
		csvfile = open(os.path.join(base_path, filename), 'r')
		jsonfile = open('./output.json', 'w')
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
		    json.dump(row, jsonfile)
		    jsonfile.write(',')
		jsonfile.seek(jsonfile.tell() - 1)    #This will shift pointer to that place (one line up)
		jsonfile.truncate()
		jsonfile.write(']\'')
		jsonfile.close()






