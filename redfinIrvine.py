from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json
import os
import re

URL = "https://www.redfin.com/city/9361/CA/Irvine/filter/property-type=house+condo+townhouse,max-price=750k,max-beds=3,min-baths=2"
base_path = '/Users/zixxu/Downloads/'
work_path = '/Users/zixxu/Documents/Learning/crawler/'

for filename in os.listdir(base_path):
	if re.match("redfin.*.csv", filename):
		os.remove(os.path.join(base_path, filename))

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless
# install using driver manager to avoid cannot found error
try:
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
except:
	print("[Error]: open chrome driver failed!")
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# add missing support for chrome "send_command"  to selenium webdriver
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': base_path}}
command_result = driver.execute("send_command", params)

print("Start to get redfin website...")
driver.get(URL)
print("Get screen shot...")
driver.get_screenshot_as_file(os.path.join(work_path, "img/sreenshot1.png"))
print("Download property data...")
driver.find_element_by_id("download-and-save").click()
# dataLink = driver.find_element_by_id("download-and-save").get_attribute('href')
# driver.get(dataLink)
driver.close()






