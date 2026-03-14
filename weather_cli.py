import requests

API_KEY = "9482209c8a6d66f9fcf7a677f674c139"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
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

    except Exception as e:
        print("Error while fetching weather data:", e)


def main():
    print("=== Weather CLI ===")
    city = input("Enter city name: ")
    get_weather(city)


if __name__ == "__main__":
    main()
