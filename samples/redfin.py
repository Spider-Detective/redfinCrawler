from bs4 import BeautifulSoup
import requests

URL = "https://www.redfin.com/stingray/api/gis-csv?al=1&market=socal&max_num_beds=3&max_price=750000&min_stories=1&num_baths=2&num_homes=350&ord=redfin-recommended-asc&page_number=1&region_id=9361&region_type=6&sf=1,2,3,5,6,7&status=9&uipt=1,2,3,4,5,6&v=8"
  # -H 'authority: www.redfin.com' \
  # -H 'pragma: no-cache' \
  # -H 'cache-control: no-cache' \
  # -H 'upgrade-insecure-requests: 1' \
  # -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' \
  # -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  # -H 'sec-fetch-site: none' \
  # -H 'sec-fetch-mode: navigate' \
  # -H 'sec-fetch-user: ?1' \
  # -H 'sec-fetch-dest: document' \
  # -H 'accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,fr;q=0.5,la;q=0.4' \
  # -H 'cookie: RF_BROWSER_ID=u_Sjh23ISFCgJzpw3dNB2w; RF_BID_UPDATED=1; _gcl_au=1.1.969439634.1593473109; _ga=GA1.2.2017846590.1593473110; _fbp=fb.1.1593473110252.1686430785; G_ENABLED_IDPS=google; RF_VISITED=true; RF_SEEN_VIRTUAL_TOUR_FLYOUT=true; _gid=GA1.2.449670115.1593561689; ki_r=; unifiedLastSearch=name%3DSan%2520Jose%26subName%3DSan%2520Jose%252C%2520CA%252C%2520USA%26url%3D%252Fcity%252F17420%252FCA%252FSan-Jose%26id%3D9_17420%26type%3D2%26isSavedSearch%3D%26countryCode%3DUS; RF_MARKET=socal; RF_MARKET=socal; RF_LAST_SEARCHED_CITY=Irvine; RF_CORVAIR_LAST_VERSION=321.0.0; AKA_A2=A; AMP_TOKEN=%24NOT_FOUND; g_state={"i_p":1593627122102,"i_l":1}; RF_BUSINESS_MARKET=4; ki_t=1593561694849%3B1593620521301%3B1593620521301%3B2%3B4; RF_LDP_VIEWS_FOR_PROMPT=%7B%22viewsData%22%3A%7B%2207-01-2020%22%3A%7B%22120948989%22%3A1%7D%7D%2C%22expiration%22%3A%222022-07-01T16%3A22%3A02.730Z%22%2C%22totalPromptedLdps%22%3A0%7D; RF_LISTING_VIEWS=120948989; RF_BROWSER_CAPABILITIES=%7B%22screen-size%22%3A3%2C%22ie-browser%22%3Afalse%2C%22events-touch%22%3Afalse%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%7D; userPreferences=parcels%3Dtrue%26schools%3Dfalse%26mapStyle%3Ds%26statistics%3Dtrue%26agcTooltip%3Dfalse%26agentReset%3Dfalse%26ldpRegister%3Dfalse%26afCard%3D2%26schoolType%3D0%26lastSeenLdp%3DnoSharedSearchCookie%26viewedSwipeableHomeCardsDate%3D1593621857139; FEED_COUNT=7%3Af; _uetsid=bd3c61ea-e50c-30fc-8de6-8afed6977e3f; _uetvid=7388308c-7e6d-4c07-fa18-1356439c660d' \
  # --compressed"
params = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
			'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,fr;q=0.5,la;q=0.4',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'authority': 'www.redfin.com',
  			'pragma': 'no-cache',
  			'cache-control': 'no-cache',
  			'upgrade-insecure-requests': '1',
  			'sec-fetch-site': 'same-origin',
  			'sec-fetch-mode': 'navigate',
  			'sec-fetch-user': '?1',
  			'sec-fetch-dest': 'document'}
  # -H 'sec-fetch-site: same-origin' \


html = requests.get(URL, params=params).text
print(html)