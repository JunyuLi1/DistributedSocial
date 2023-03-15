# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module for a superclass of two API classes."""
from abc import ABC, abstractmethod
import urllib
import json
from urllib import request, error


class WebAPI(ABC):
    """Class of WebAPI"""
    def __init__(self):
        """Construct webapi objects."""
        self.apikey = ''

    def _download_url(self, url_to_download: str) -> dict:
        """Download url."""
        response = None
        r_obj = None
        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            r_obj = json.loads(json_results)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise Exception('Remote API is unavailable')
            if e.code == 503:
                raise Exception('The Server is unavailable now.')
            if e.code == 401:
                raise Exception('The APIkey is invalid.')
            else:
                raise Exception(e)
        except urllib.error.URLError:
            raise Exception('Loss of local connection to the Internet.')
        except ValueError:
            raise Exception('Invalid data formatting from the remote API.')
        finally:
            if response is not None:
                response.close()
        return r_obj

    def set_apikey(self, apikey: str) -> None:
        """Set apikey."""
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
        """Load data."""
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        """Transculde message."""
        pass
