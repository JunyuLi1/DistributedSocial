# lastfm.py

# My apikey for lastfm is: 9e378b414d40568750b1dcbc42d0d6cd

# Junyu Li
# junyul24@uci.edu
# junyul031030@gmail.com
# 86676906
"""Module for Lastfm WebAPI"""
from WebAPI import WebAPI
# How to work LastFM:
# I choose the api method called chart.getTopTags
# Link:https://www.last.fm/api/show/chart.getTopTags
# This method can get some tags of popular music.
# In this assignment, @lastfm will be replaced
# by the most popular music category
# If you run this module, you can see
# The most popular music tag is rock music.


class LastFM(WebAPI):
    """Class of lastFM."""

    def __init__(self):
        super().__init__()
        self.toptagname = ''
        self.apikey = ''

    def load_data(self) -> None:
        """Load data."""
        try:
            url = f"http://ws.audioscrobbler.com/2.0/?method=tag." \
                  f"getTopTags&api_key={self.apikey}&format=json"
            json_obj = self._download_url(url)
        except Exception as e:
            print(f'Failed to download contents of URL because {e}')
        else:
            self.toptagname = json_obj['toptags']['tag'][0]['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude

        :returns: The transcluded message
        '''
        newmessage = message.replace('@lastfm', self.toptagname)
        return newmessage


def main() -> None:
    """Test how API runs."""
    apikey = "9e378b414d40568750b1dcbc42d0d6cd"
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag." \
          f"getTopTags&api_key={apikey}&format=json"
    obj = LastFM()
    weather_obj = obj._download_url(url)
    if weather_obj is not None:
        print(weather_obj)
    obj.set_apikey(apikey)
    obj.load_data()
    print(obj.toptagname)


if __name__ == '__main__':
    main()
