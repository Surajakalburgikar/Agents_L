import requests

# Ask user for city
city_name = input("Enter a city name: ")

# Step 1: Convert city to coordinates
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"

geo_response = requests.get(geo_url)
if geo_response.status_code != 200:
    print("Failed to get location details")
    exit()

geo_data = geo_response.json()

if "results" not in geo_data or len(geo_data["results"]) == 0:
    print("City not found. Try again.")
    exit()

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]

print(f"Coordinates found: {lat}, {lon}")

# Step 2: Fetch weather from coordinates
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

weather_response = requests.get(weather_url)
if weather_response.status_code != 200:
    print("Weather data failed")
    exit()

weather_data = weather_response.json()
current = weather_data["current_weather"]

print("\nWeather Report:")
print("Temperature:", current["temperature"], "°C")
print("Wind Speed:", current["windspeed"], "km/h")
print("Weather Code:", current["weathercode"])
