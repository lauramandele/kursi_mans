import json
import requests
print("Enter coordinates where are you now")
lon = input("Longitude: ")
lat = input("Latitude: ")

# weather forecast for 7 days
src = "https://www.7timer.info/bin/civillight.php?lon="+lon+"&lat="+lat+"&ac=0&unit=metric&output=json&tzshift=0"
# src = "https://www.7timer.info/bin/civillight.php?lon=24.6&lat=56.8&ac=0&unit=metric&output=json&tzshift=0"

response = requests.get(src)
# print(response.text)

data_json = response.json()
print(data_json)
date = data_json['init']
print(date)
print(data_json["dataseries"][0])

with open("weather_"+date+".json", mode="w") as write_file:
    json.dump(data_json, write_file, indent=4)

with open("weather_"+date+".csv", mode="w") as f:
    column_names = ",".join(data_json["dataseries"][0].keys())
    f.write(column_names + "\n")
    for row in data_json["dataseries"]:  # each row is a dictionary
        values = ",".join([str(item) for item in row.values()])  # this manual method will break if there are commas in the values
        f.write(values + "\n")