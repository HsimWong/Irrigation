import requests
import json
url = "https://api.darksky.net/forecast/3c90535ae519d3b35f5139f0d0e60e31/39.8507186,116.4742262?units=auto&lang=zh"
weather = str(requests.get(url).content, "utf-8")
weather_dic = json.loads(weather)
for i in range(24):
    
    print(weather_dic["hourly"]["data"][i]["apparentTemperature"])
