import requests

print("Login: -------------------")
payload = {"username": "Zixi Xu", "password": "password"}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data=payload)
print(r.cookies.get_dict())
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
#print(r.text)