import json
import requests

url = 'http://20.185.44.219:5000/'
myobj =  {"latitude":40.590286, "longitude": -75.554245 }

x = requests.post(url, json = myobj)
data = x.json()

print(myobj)
print(x)
print(data)