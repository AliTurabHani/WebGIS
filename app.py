from flask import Flask, render_template, jsonify
import requests
import time

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aircraft_data')
def aircraft_data():
    latitude = 57.2037  #  Airport latitude
    longitude = 2.2  # Airport longitude
    radius = 200  # 200-mile radius

    api_url = f'http://api.airplanes.live/v2/point/{latitude}/{longitude}/{radius}'
    response = requests.get(api_url)

    if response.status_code == 200:
        aircraft_data = response.json()
        return jsonify(aircraft_data)
    else:
        return jsonify({"error": "Failed to fetch aircraft data"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000, use_reloader=False)
