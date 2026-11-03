
import os
import random
from pathlib import Path
from flask import Flask, render_template, jsonify

# Always locate frontend folders relative to this file
BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

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


# Traverse the dataset and filter forecasts
def filter_weather():
    filtered_weather = []

    for i in range(len(weather_data)):
        if weather_data[i]["forecast_number"] == 2:
            filtered_weather.append(weather_data[i])

    return filtered_weather


# Select a random forecast from the filtered data
def get_random_forecast():
    filtered_weather = filter_weather()

    if not filtered_weather:
        return None

    return random.choice(filtered_weather)


# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Forecast API
@app.route("/forecast")
def forecast():
    result = get_random_forecast()

    if result is None:
        return jsonify({"error": "No forecasts available"}), 404

    return jsonify(result)


# Health check
@app.route("/health")
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
