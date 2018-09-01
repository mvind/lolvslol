import requests, json
from key import api_key

url = 'http://api.champion.gg/champion?api_key='+api_key
r = requests.get(url)
url2 = 'http://api.champion.gg/champion/draven?api_key='+api_key
print(api_key)

r2 = requests.get(url2)

print(r2.json())
#print(r.json())
#/champion/:name?api_key=<API_KEY>
