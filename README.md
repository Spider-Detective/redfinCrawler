# redfinCrawler
This is a Python crawler to check the newly available houses on Redfin website.

## Get Started Locally
1. Update the target URL in ```redfinIrvine.py``` as you like. 

   Redfin has a special ```region id``` for each city, e.g. Irvine is 9361.
```URL = "https://www.redfin.com/city/9361/CA/Irvine/filter/property-type=house+condo+townhouse,max-price=750k,max-beds=3,min-baths=2"```
Or you can go with zipcode:
``` https://www.redfin.com/zipcode/94086```
2. Update ```base_path``` and ```work_path``` in ```redfinIrvine.py``` on your machine.
3. Use ```crontab``` (on Mac or Linux) to schedule the Python scripts. e.g.:
   ```
   0 10,16 * * * /anaconda3/bin/python3 /Users/zixxu/Documents/Learning/crawler/redfinIrvine.py >| /Users/zixxu/Documents/Learning/crawler/log/redfinIrvine.log 2>&1
   5 13 * * * /anaconda3/bin/python3 /Users/zixxu/Documents/Learning/crawler/storeData.py >| /Users/zixxu/Documents/Learning/crawler/log/storeData.log 2>&1
   ```
   Note: ">|" means overwrite, need ```noclobber``` flag on (```set -o | grep noclobber```)
4. There will be a ```.csv``` file downloaded which will be processed by Python scripts. Then host the webpage through Nginx:
   ```
   sudo nginx
   ```
   And go to ```http://localhost:[port]``` to see the crawler results. You can edit the Nginx config file at ```/usr/local/etc/nginx/```.
## Possible Improvements
1. Server side: Use an actual server instead of local computer.
   We can use AWS to hold the Python scripts and Webpages, also move ```crontab``` scheduler there.
2. Client side: Use React.js instead of web component.
