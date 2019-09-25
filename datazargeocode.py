import googlemaps
import requests
import json


api_key = ""
gm = googlemaps.Client(key=api_key)

city = input("Please enter a city: ")

geocode_result = gm.geocode(city)[0]

coordinates = geocode_result['geometry']['location']
coordinates.setdefault("city", city)
coordinates['lat'] = coordinates.pop(u'lat')
coordinates['long'] = coordinates.pop(u'lng')


print(coordinates)

url = ''

requests.post(url, json=coordinates)
