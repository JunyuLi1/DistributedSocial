# Profile.py
#
# ICS 32
# Assignment #2: Journal
#
# Author: Mark S. Baldwin, modified by Alberto Krone-Martins
#
# v0.1.9

# You should review this code to identify what features you need to support
# in your program for assignment 2.
#
# YOU DO NOT NEED TO READ OR UNDERSTAND THE
# JSON SERIALIZATION ASPECTS OF THIS CODE
# RIGHT NOW, though can you certainly take a
# look at it if you are curious since we
# already covered a bit of the JSON format in class.
#
"""Module for Profile."""
import json
import time
from pathlib import Path


class DsuFileError(Exception):
    """Defile an exception."""
    pass


class DsuProfileError(Exception):
    """Defile an  exception."""
    pass


class Post(dict):
    """Class of posts"""
    def __init__(self, entry: str = None, timestamp: float = 0):
        """Construct post object."""
        self._timestamp = timestamp
        self.set_entry(entry)

        # Subclass dict to expose Post properties for serialization
        # Don't worry about this!
        dict.__init__(self, entry=self._entry, timestamp=self._timestamp)

    def set_entry(self, entry):
        """Set entry."""
        self._entry = entry
        dict.__setitem__(self, 'entry', entry)

        # If timestamp has not been set, generate a new from time module
        if self._timestamp == 0:
            self._timestamp = time.time()

    def get_entry(self):
        """Get entry"""
        return self._entry

    def set_time(self, time: float):
        """Set time"""
        self._timestamp = time
        dict.__setitem__(self, 'timestamp', time)

    def get_time(self):
        """Get time"""
        return self._timestamp

    entry = property(get_entry, set_entry)
    timestamp = property(get_time, set_time)


class Profile:
    """Class of Profile"""
    def __init__(self, dsuserver=None, username=None, password=None):
        """Construct object."""
        self.dsuserver = dsuserver  # REQUIRED
        self.username = username  # REQUIRED
        self.password = password  # REQUIRED
        self.bio = ''            # OPTIONAL
        self._posts = []         # OPTIONAL
        self.friend_username = {}  # List of username which type is string.

    def add_post(self, post: Post) -> None:
        """Add posts."""
        self._posts.append(post)

    def del_post(self, index: int) -> bool:
        """Delet posts."""
        try:
            del self._posts[index]
            return True
        except IndexError:
            return False

    def get_posts(self) -> list[Post]:
        """Get posts."""
        return self._posts

    def save_profile(self, path: str) -> None:
        """Save profile."""
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'w')
                json.dump(self.__dict__, f)
                f.close()
            except Exception as ex:
                raise DsuFileError("Error while attempting "
                                   "to process the DSU file.", ex)
        else:
            raise DsuFileError("Invalid DSU file path or type")

    def load_profile(self, path: str) -> None:
        """Load profile."""
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                self.bio = obj['bio']
                for post_obj in obj['_posts']:
                    post = Post(post_obj['entry'], post_obj['timestamp'])
                    self._posts.append(post)
                for name_obj in obj['friend_username']:
                    self.friend_username[name_obj] = []
                f.close()
            except Exception as ex:
                raise DsuProfileError(ex)
        else:
            raise DsuFileError()

    def add_friend_username(self, name):
        """Add friend username locally."""
        self.friend_username[name] = []

    def add_history_to_username(self, friend_name, content):
        """Add chat history locally."""
        self.friend_username[friend_name].append(content)
