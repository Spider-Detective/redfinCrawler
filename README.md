# redfinCrawler
This is a Python crawler to check the newly available houses on Redfin website.

## Get Started
1. Update the target URL in ```redfinIrvine.py``` as you like. 
Redfin has a special ```region id``` for each city
URL = "https://www.redfin.com/city/9361/CA/Irvine/filter/property-type=house+condo+townhouse,max-price=750k,max-beds=3,min-baths=2"
2. Update ```base_path``` and ```work_path``` in ```redfinIrvine.py``` on your machine.
3. Use ```crontab``` (on Mac or Linux) to schedule the Python scripts. e.g.:
   ```
   0 10,16 * * * /anaconda3/bin/python3 /Users/zixxu/Documents/Learning/crawler/redfinIrvine.py >| /Users/zixxu/Documents/Learning/crawler/log/redfinIrvine.log 2>&1
   5 13 * * * /anaconda3/bin/python3 /Users/zixxu/Documents/Learning/crawler/storeData.py >| /Users/zixxu/Documents/Learning/crawler/log/storeData.log 2>&1
   ```
Note: ">|" means overwrite, need ```noclobber``` flag on (```set -o | grep noclobber```)
