
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Weather dataset
weather_data = [
    {
        "city": "Denver",
        "forecast_number": 2,
        "icon": "☀️",
        "condition": "Sunny",
        "high": 72,
        "low": 45
    },
    {
        "city": "New York",
        "forecast_number": 2,
        "icon": "🌧️",
        "condition": "Rainy",
        "high": 61,
        "low": 48
    },
    {
        "city": "Chicago",
        "forecast_number": 2,
        "icon": "☁️",
        "condition": "Cloudy",
        "high": 58,
        "low": 42
    },
    {
        "city": "Miami",
        "forecast_number": 2,
        "icon": "⛈️",
        "condition": "Thunderstorms",
        "high": 84,
        "low": 73
    },
    {
        "city": "Seattle",
        "forecast_number": 1,
        "icon": "🌦️",
        "condition": "Showers",
        "high": 55,
        "low": 44
    }
]


# Filter forecasts using a traversal
def filter_weather():
    filtered_weather = []

    for i in range(len(weather_data)):
        if weather_data[i]["forecast_number"] == 2:
            filtered_weather.append(weather_data[i])

    return filtered_weather


# Generate a random forecast
def get_random_forecast():
    filtered_weather = filter_weather()

    if len(filtered_weather) == 0:
        return None

    return random.choice(filtered_weather)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/forecast")
def forecast():
    result = get_random_forecast()

    if result is None:
        return jsonify({"error": "No forecasts available"}), 404

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
