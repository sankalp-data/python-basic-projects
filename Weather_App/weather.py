import requests

try:
    city = input("City Name :- ").strip()
except ValueError:
    print("Invalid input!")


api_key = "your_api_key_here"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

city_name = data["name"]
country = data["sys"]["country"]
weather_description = data["weather"][0]["description"]
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

print(f"Weather in {city_name}, {country}: {weather_description}")
print(f"Temperature: {temperature}*C (Feels like) {feels_like}*C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
