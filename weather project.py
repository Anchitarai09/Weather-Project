import requests , json

apikey = "17e2d4667e4b35031eaa0398a8cc6db1"

baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

cityName = input("Enter your city : ")

completeURL = baseURL + cityName + "&appid=" + apikey

response = requests.get(completeURL)
data = response.json()

# print(data)
print("Current Temprature : ",data["main"]["temp"])

print("Current Temprature Feels like : ",data["main"]["feels_like"])

print("Maximum Temprature : ",data["main"]["temp_max"])

print("Minimum Temprature : ",data["main"]["temp_min"])