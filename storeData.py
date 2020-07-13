import csv
import json
import os
import re

base_path = '/Users/zixxu/Downloads/'
work_path = '/Users/zixxu/Documents/Learning/crawler/'

# store the data to json
for filename in os.listdir(base_path):
	print("Check file: " + filename)
	if re.match("redfin.*.csv", filename):
		print("Start store data")
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
		    json.dump(row, jsonfile)
		    jsonfile.write(',')
		jsonfile.seek(jsonfile.tell() - 1)    #This will shift pointer to that place (one line up)
		jsonfile.truncate()
		jsonfile.write(']\'')
		jsonfile.close()