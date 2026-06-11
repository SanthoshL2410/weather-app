import requests

API_KEY = "d533bd65dddb6f054b6a995e6d1c784b"

while True:
    city = input("\nEnter city name: ")

    if city.lower() == "exit":
        print("Exiting Weather App...")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Details")
        print("City:", city)
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("City not found or API issue!")