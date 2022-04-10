import requests
import folium
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# m = folium.Map(location=[latitude, longitude], zoom_start=12)
# m.save("map.html")
headers = {
    "Accept": "application/json",
    "Authorization": os.getenv("AUTHORIZATION")
}

dataset = pd.read_csv('Age_Vs_Crime.csv')
neighborhoods = dataset.columns[:]
for n in neighborhoods:
    print(n)
    url = "https://api.foursquare.com/v3/places/search?query=primary_school%2C%20elementary_school%2C%20secondary_school&near={}%2C%20Toronto".format(n)
    response = requests.request("GET", url, headers=headers).json()
    print(response["results"])





# url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
#
# params = { "id": "6e19a90f-971c-46b3-852c-0c48c436d1fc" }
# package = requests.get(url, params=params).json()
# print(package["result"])
