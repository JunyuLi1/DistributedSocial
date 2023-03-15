# unit_test.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module for testing functions"""
import unittest
from urllib import request
import json
from OpenWeather import OpenWeather
from LastFM import LastFM


def download_data(message: str, apikey: str, webapi):
    """transclude message"""
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    return result


class Openweathertest(unittest.TestCase):
    """Test OpenWeather()"""
    def test_openweather_transclude(self):
        """test OpenWeather function"""
        # Organize Phrase
        url = "http://api.openweathermap.org/data/2.5/weather?zip=" \
              "92697,US&appid=03657b48a28c90947a8068f1f2608dfc"
        with request.urlopen(url) as response:
            json_results = response.read()
            r_obj = json.loads(json_results)
            description = r_obj['weather'][0]['description']
        message = f"Testing the weather: {description}"
        # Action Phrase
        open_weather = OpenWeather()
        apikey = "03657b48a28c90947a8068f1f2608dfc"
        result = download_data("Testing the weather: @weather",
                               apikey, open_weather)
        # Assert Phrase
        assert message == result

    def test_setapi(self):
        """Test method set apikey."""
        apikey = '03657b48a28c90947a8068f1f2608dfc'
        open_weather = OpenWeather()
        open_weather.set_apikey(apikey)
        result = open_weather.apikey
        assert apikey == result


class lastfmtest(unittest.TestCase):
    """Test lastfm"""
    def test_openweather_transclude(self):
        """test lastfm function"""
        # Organize Phrase
        apikey = "9e378b414d40568750b1dcbc42d0d6cd"
        url = f"http://ws.audioscrobbler.com/2.0/?method=tag." \
              f"getTopTags&api_key={apikey}&format=json"
        with request.urlopen(url) as response:
            json_results = response.read()
            object = json.loads(json_results)
            tag = object['toptags']['tag'][0]['name']
        message = f"Testing lastFM: {tag}"
        # Action Phrase
        lastfm = LastFM()
        result = download_data("Testing lastFM: @lastfm", apikey, lastfm)
        # Assert Phrase
        assert message == result

    def test_setapi2(self):
        """Test method set apikey."""
        apikey = '9e378b414d40568750b1dcbc42d0d6cd'
        lastfm = LastFM()
        lastfm.set_apikey(apikey)
        result = lastfm.apikey
        assert apikey == result


if __name__ == "__main__":
    unittest.main()
