import requests
from datetime import datetime
import json

# Asking user for input- city
city = input("Insert city name which you want to check the weather for ")

# Get data in JSON
url = f"http://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()

# Get today date
today = datetime.now().date()
print(f"\nWeather in {city} from today ({today}) for 3 days: \n")

# Create list to save in JSON
forecast_list = []

# 3 days weather forecast
for day_data in data["weather"][:3]:
    date = day_data["date"]
    avg_temp = day_data["avgtempC"]
    max_temp = day_data["maxtempC"]
    min_temp = day_data["mintempC"]
    desc = day_data["hourly"][4]["weatherDesc"][0]["value"]  # np. średnia popołudniowa godzina
    
    # Agents decision
    advice = ""
    if int(max_temp) > 25:
        advice += "Take your sunglasses 😎. "
    if int(min_temp) < 10:
        advice += "Wear a coat 🧥. "
    if int(max_temp) > 12:
        advice += "Wear casual 👕. "
    if "rain" in desc.lower():
        advice += "Take an umbrella ☔"
    if not advice:
        advice = "No need for umbrella 🌂"
    
    # Add data to the list
    forecast_list.append({
        "date": date,
        "description": desc,
        "avg_temp_C": avg_temp,
        "max_temp_C": max_temp,
        "min_temp_C": min_temp,
        "advice": advice
    })
    
    # Show in console
    print(f"{date}: {desc}, average: {avg_temp}°C, max: {max_temp}°C, min: {min_temp}°C")
    print(f"Agent's advice: {advice}\n")

# Save to JSON
filename = f"{city}_forecast.json"
with open(filename, "w") as f:
    json.dump(forecast_list, f, indent=4)

print(f"Saved as: {filename}")