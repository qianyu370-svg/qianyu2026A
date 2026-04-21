import requests
url = "https://pyweb2026a-ten.vercel.app/about"
Data = requests.get(url)
print(Data.text)
