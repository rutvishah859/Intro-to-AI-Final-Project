import requests
import folium
import os
latitude = 43.6532
longitude = -79.3832

m = folium.Map(location=[latitude, longitude], zoom_start=12)
m.save("map.html")

url = "https://api.foursquare.com/v3/places/search?ll=43.6532%2C-79.3832"

headers = {
    "Accept": "application/json",
    "Authorization": os.getenv("AUTHORIZATION")
}

response = requests.request("GET", url, headers=headers)

print(response.text)
