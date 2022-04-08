import requests
import folium
latitude = 43.6532
longitude = -79.3832

m = folium.Map(location=[latitude, longitude], zoom_start=12)
m.save("map.html")

url = "https://api.foursquare.com/v3/places/search?ll=43.6532%2C-79.3832"

headers = {
    "Accept": "application/json",
    "Authorization": "fsq389G1dW5rpyZXK8hM8aYJrVfIQulRs+pclsWRnaFed1I="
}

response = requests.request("GET", url, headers=headers)

print(response.text)
