AIM:
To fetch weather data from the JSON: Write a python program to fetch current weather
data from the JSON file
ALGORITHM:
1. Start
2. Import the json module
3. Define a function fetch_weather_from_json(file_path)
4. Open the JSON file in read mode
5. Use json.load() to parse the JSON content into a Python dictionary
6. Access the following data from the dictionary:
a) location["name"] – Name of the city
b) location["country"] – Name of the country
c) current["temperature"] – Current temperature
d) current["humidity"] – Current humidity
e) current["wind_speed"] – Current wind speed
f) current["weather_descriptions"][0] – Current weather description
7. Print the weather report in a readable format
8. End the function
9. Call the function with the path to the JSON file
Sample JSON File (weather.json)
{
"location": {
"name": "Chennai",
"country": "India"
},
"current": {
"temperature": 31,
"humidity": 76,
"wind_speed": 12
"weather_descriptions": ["Partly cloudy"]
}
}
PROGRAM:
import json
def fetch_weather_from_json(file_path):
with open(file_path, 'r') as f:
data = json.load(f)
location = data['location']['name']
country = data['location']['country']
temperature = data['current']['temperature']
humidity = data['current']['humidity']
wind_speed = data['current']['wind_speed']
description = data['current']['weather_descriptions'][0]
print(f"Weather Report for {location}, {country}")
print(f"Condition : {description}")
print(f"Temperature : {temperature}°C")
print(f"Humidity : {humidity}%")
print(f"Wind Speed : {wind_speed} km/h")
OUTPUT
Weather Report for Chennai, India
Condition : Partly cloudy
Temperature : 31°C
Humidity : 76%
Wind Speed : 12 km/h
