# openweather.py

# My API key for Openweather is: 03657b48a28c90947a8068f1f2608dfc
# Junyu Li
# junyul24@uci.edu
# junyul031030@gmail.com
# 86676906
"""Module for Openweather WebAPI"""
from WebAPI import WebAPI


class OpenWeather(WebAPI):
    """Class of OpenWeather"""
    def __init__(self, zipcode="92697", ccode="US"):
        super().__init__()
        self.zipcode = zipcode
        self.ccode = ccode
        self.apikey = ''
        self.temperature = 0
        self.high_temperature = 0
        self.low_temperature = 0
        self.longitude = 0
        self.latitude = 0
        self.description = ''
        self.humidity = 0
        self.sunset = 0
        self.city = ''

    def load_data(self) -> None:
        """Calls the web api"""
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?" \
                  f"zip={self.zipcode},{self.ccode}&appid={self.apikey}"
            json_obj = self._download_url(url)
        except Exception as e:
            print(f'Failed to download contents of URL because {e}')
        else:
            self.temperature = json_obj['main']['temp']
            self.high_temperature = json_obj['main']['temp_max']
            self.low_temperature = json_obj['main']['temp_min']
            self.longitude = json_obj['coord']['lon']
            self.latitude = json_obj['coord']['lat']
            self.description = json_obj['weather'][0]['description']
            self.humidity = json_obj['main']['humidity']
            self.sunset = json_obj['sys']['sunset']
            self.city = json_obj['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude

        :returns: The transcluded message
        '''
        newmessage = message.replace('@weather', self.description)
        return newmessage


def main() -> None:
    """Test API how to run."""
    zip = "92617"
    ccode = "US"
    apikey = "03657b48a28c90947a8068f1f2608dfc"
    url = f"http://api.openweathermap.org/data/2.5/" \
          f"weather?zip={zip},{ccode}&appid={apikey}"
    obj = OpenWeather(zip, ccode)
    weather_obj = obj._download_url(url)
    if weather_obj is not None:
        print(weather_obj)
        print(weather_obj['weather'][0]['description'])


if __name__ == '__main__':
    main()
