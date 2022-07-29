from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            ...
            # test that you're getting a template
            #set response data to html variable
            #assert equal to test response code 200
            #assert in to test heading of html
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('comment: for testing', html)


    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            # write a test for this route

            resp = client.post('/api/new-game')
            json = resp.get_json()
            # breakpoint()

            """Test json[board] is equal to a list of list
            json[gameId] is equal to a type of string
            test that games[json[gameId]] is not None answer should be true

            """
            self.assertIsInstance(json["gameId"], str)
            self.assertNotEqual(games[json["gameId"]], None)



