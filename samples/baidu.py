import requests
import webbrowser

print("Use requests.get(): -------------------")
param = {"wd": "阿森纳"}
r = requests.get("http://www.baidu.com/s", params=param)
# r is requests.response object: https://requests.readthedocs.io/en/master/api/#requests.Response
print(r.url)
# webbrowser.open(r.url)

print("Use requests.post(): ------------------")
data = {'firstname': 'Zixi', 'lastname': 'Xu'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)

print("Use request.post() for file: ----------")
file = {'uploadFile': open('./ScreenShot.png', 'rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
print(r.text)