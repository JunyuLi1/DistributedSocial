# Profile.py

# junyul24@uci.edu
# junyul031030@gmail.com
# 86676906
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
        path = Path(path)

        if path.exists() and path.suffix == '.dsu':
            try:
                file = open(path, 'w')
                json.dump(self.__dict__, file)
                file.close()
            except Exception as exc:
                raise DsuFileError("Error while attempting "
                                   "to process the DSU file.") from exc
        else:
            raise DsuFileError("Invalid DSU file path or type")

    def load_profile(self, path: str) -> None:
        """Load profile."""
        path = Path(path)

        if path.exists() and path.suffix == '.dsu':
            try:
                file = open(path, 'r')
                obj = json.load(file)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                self.bio = obj['bio']
                for post_obj in obj['_posts']:
                    post = Post(post_obj['entry'], post_obj['timestamp'])
                    self._posts.append(post)
                if 'friend_username' in obj:
                    self.friend_username = obj['friend_username']
                file.close()
            except Exception as exc:
                raise DsuProfileError() from exc
        else:
            raise DsuFileError()

    def extract_for_directmessage(self, lis_of_objects):
        """extract_for_directmessage."""
        for item in lis_of_objects:
            if item.recipient not in self.friend_username.keys():
                self.add_friend_username(item.recipient)
                self.add_history_to_username(item.recipient, item.message)
            else:
                self.add_history_to_username(item.recipient, item.message)

    def add_friend_username(self, name):
        """Add friend username locally."""
        self.friend_username[name] = []

    def add_history_to_username(self, friend_name, content):
        """Add chat history locally."""
        self.friend_username[friend_name].append(content)
