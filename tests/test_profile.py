# Programming with Software Libraries in Python


# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module for testing profile"""
import unittest
from pathlib import Path
from Profile import Profile, Post
import ds_messenger


class TestProfile(unittest.TestCase):
    """Class for test"""
    def setUp(self):
        """set up"""
        self.profile = Profile("dsuserver", "username", "password")

    def test_add_post(self):
        """add post"""
        post = Post("Hello World", 12345)
        self.profile.add_post(post)
        self.assertIn(post, self.profile.get_posts())

    def test_del_post(self):
        """del post"""
        post1 = Post("Hello World", 12345)
        post2 = Post("Goodbye World", 12346)
        self.profile.add_post(post1)
        self.profile.add_post(post2)

        self.assertTrue(self.profile.del_post(0))
        self.assertNotIn(post1, self.profile.get_posts())

        self.assertFalse(self.profile.del_post(2))

    def test_save_profile(self):
        """save profile"""
        post = Post("Hello World", 12345)
        self.profile.load_profile("test.dsu")
        self.profile.add_post(post)
        self.profile.save_profile("test.dsu")
        self.assertTrue(Path("test.dsu").exists())

    def test_load_profile(self):
        """laod profile"""
        post = Post("Hello World", 12345)
        self.profile.add_post(post)
        self.profile.save_profile("test.dsu")
        self.assertTrue(Path("test.dsu").exists())
        new_profile = Profile()
        new_profile.load_profile("test.dsu")
        self.assertEqual(new_profile.dsuserver, self.profile.dsuserver)
        self.assertEqual(new_profile.username, self.profile.username)
        self.assertEqual(new_profile.password, self.profile.password)
        self.assertEqual(new_profile.bio, self.profile.bio)
        self.assertEqual(new_profile.get_posts(), self.profile.get_posts())

    def test_add_friend_username(self):
        """test username"""
        obj = ds_messenger.DirectMessage()
        obj.message = 'hello'
        obj.recipient = 'friend1'
        obj.timestamp = 1234
        self.profile.add_friend_username(obj.recipient)
        self.profile.save_profile('test.dsu')
        assert obj.recipient in self.profile.friend_username


if __name__ == '__main__':
    unittest.main()
