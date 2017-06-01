from unittest import TestCase
from server import app


class MyAppTests(TestCase):
    """Unit tests"""

    def setUp(self):
        print "(setUp ran)"
        self.client = app.test_client()
        app.config['SECRET_KEY'] = 'key'


    def test_homepage(self):
        """Tests home page rendering."""

        result = self.client.get('/')
        self.assertIn(u'<title>Hangman Solver</title>', result.data)


    def test_show_game_result(self):
        """Tests play_game functionality and display."""

        result = self.client.get('/play-game')
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
#
    import unittest

    unittest.main()
