#import requests
import forecastio
api_url = "https://api.darksky.net/forecast/3c90535ae519d3b35f5139f0d0e60e31/39.8507186,116.4742262"
api_key = "3c90535ae519d3b35f5139f0d0e60e31"
lat = 39.8507186
lng = 116.4742262
forecast = forecastio.load_forecast(api_key, lat, lng, units = "zh")
byhour = forecast.hourly()
print(byhour)
