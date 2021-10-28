weather = {
    'Monday': 12,
    'Tuesday': 16,
    'Wednesday': 17,
    'Thursday': 11,
    'Friday': 19,
    'Saturday': 18,
    'Sunday': 20
}
weather_in_fahrenheit = {day: temp * (9 / 5) + 32 for (day, temp) in weather.items()}
print(weather_in_fahrenheit)
