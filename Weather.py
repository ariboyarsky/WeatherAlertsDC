import requests
import keys

class Forecast(object):

    high = None
    low = None
    humidity = None
    conditions = None
    date = None

    def __init__(self):
        r = requests.get(
            "http://api.wunderground.com/api/" + keys.WU.token + "/forecast/geolookup/conditions/q/DC/Washington.json")

        data = r.json()

        self.high = data['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
        self.low = data['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
        self.humidity = data['forecast']['simpleforecast']['forecastday'][0]['avehumidity']
        self.conditions = str(data['forecast']['simpleforecast']['forecastday'][0]['conditions'])
        self.date = data['forecast']['simpleforecast']['forecastday'][0]['date']['pretty']

