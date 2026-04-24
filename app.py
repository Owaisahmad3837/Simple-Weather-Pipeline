import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 34.1983,
        "longitude": 72.0403,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    weather = data["current_weather"]

    return {
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "code": weather["weathercode"],
        "time": weather["time"]
    }

@app.route("/")
def home():
    weather_data = get_weather()
    print(weather_data)   # 👈 check this
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)