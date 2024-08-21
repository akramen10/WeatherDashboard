import requests

api_key = "f0776fd1eea98dfde8eab72e4cd90464"
city = input("Enter city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Construct the final URL
complete_url = f"{base_url}?q={city}&units=imperial&appid={api_key}"


# Make the request
response = requests.get(complete_url)

# Convert the response to JSON format
data = response.json()

if data["cod"] != "404":
    main = data["main"]
    weather = data["weather"][0]
    print(f"City: {city}")
    print(f"Temperature: {main['temp']}°F")
    print(f"Weather: {weather['description']}")
    print(f"Humidity: {main['humidity']}%")
    print(f"Wind Speed: {wind['speed']} mph")
else:
    print("City not found!")