import requests
from flask import Flask, render_template, request
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature', methods=['POST'])
def temperature():
    city = request.form['city']
    r = requests.get('http://api.apixu.com/v1/current.json?key=19c86fa41dd44838b1b153447182206&q={city}'.format(city=city))
    object = r.json()
    if 'current' in object:
        temp = object['current']['temp_c']
        wind = object['current']['wind_kph']
        country = object['location']['country']
        if r.status_code == 200:
            return render_template('temp.html', city=city, temp=temp, wind=wind, country=country)
        else:
            return "oops"
    else:
        return "Please enter city name"

if __name__ == '__main__':
    app.run(debug=True, port=3000)