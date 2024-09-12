from functools import reduce

import  requests
import json
import math

API_KEY = 'b1e2515cfc3ec25e3c08c7329d1a9298'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast?q='
CITIES_LIST = ['tehran', 'Baghdad', 'Damascus', 'Kabul', 'Sanaa', 'Riyadh', 'Cairo', 'Beirut', 'Amman', 'Tripoli',
               'Khartoum', 'Mosul', 'Fallujah', 'Marrakesh', 'Kandahar', 'Marrakesh']


def get_weather_data_city(city):
    response = requests.get(f'{BASE_URL}{city}&appid={API_KEY}')
    json_data = json.loads(response.text)
    data_weather = {'condition': json_data['list'][4]['weather'][0]['main'],
                    'clouds': json_data['list'][4]['clouds']['all'],
                    'wind': json_data['list'][4]['wind']['speed'],
                    'lat': json_data['city']['coord']['lat'],
                    'lon': json_data['city']['coord']['lon'],}
    return data_weather

def weather_score(weather):
    if weather['condition'] == 'Rain':
        return 0.4
    elif weather['condition'] == 'Clear':
        return 1.0
    elif weather['condition'] == 'Clouds':
        return 0.7
    elif weather['condition'] == 'Stormy':
        return 0.2


def get_weather_cities(cities):
    result = list(map(lambda city: get_weather_data_city(city), cities))
    return result

def calculate_weather_score(cities_weather):
    for city in cities_weather:
        city.update(weather_score(cities_weather[city]))
    return cities_weather

list_of_weather_cities = get_weather_cities(CITIES_LIST)
print(calculate_weather_score(list_of_weather_cities))

def haversine_distance(lat1, lon1, lat2, lon2):
     r = 6371.0
     lat1_rad = math.radians(lat1)
     lon1_rad = math.radians(lon1)
     lat2_rad = math.radians(lat2)
     lon2_rad = math.radians(lon2)
     # Calculate differences between the coordinates
     dlat = lat2_rad - lat1_rad
     dlon = lon2_rad - lon1_rad
     # Apply Haversine formula
     a = (math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) *
          math.cos(lat2_rad) * math.sin(dlon / 2) ** 2)
     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
     # Calculate the distance
     distance = r * c
     return distance

