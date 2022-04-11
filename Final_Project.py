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
school_count = [0] * 140
neighborhoods = dataset.columns[:]
for n in range(len(neighborhoods) - 1):
    url = "https://api.foursquare.com/v3/places/search?query=school&near={}%2C%20Toronto".format(neighborhoods[n])
    response = requests.request("GET", url, headers=headers).json()

    names = ["elementary", "primary", "preschool", "middle", "high", "secondary"]
    for i in response["results"]:
        for j in i["categories"]:
            if any(name in j["name"].lower() for name in names):
                school_count[n] += 1

print(school_count)





# url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
#
# params = { "id": "6e19a90f-971c-46b3-852c-0c48c436d1fc" }
# package = requests.get(url, params=params).json()
# print(package["result"])
