import requests

API_KEY = "9482209c8a6d66f9fcf7a677f674c139"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\nWeather in {city}")
    print("Temperature:", temperature, "°C")
    print("Condition:", weather)

else:
    print("City not found.")
