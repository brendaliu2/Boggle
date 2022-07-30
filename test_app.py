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

    def test_api_score_word(self):
        """Test the correct score for each word length."""
        """ """
        with self.client as client:
            ...


            resp = client.post('/api/new-game')
            gameId = resp.json["gameId"]
            game = games["gameId"]
            game.board = [['C', 'A', 'T', 'A', 'F'], ['D', 'O', 'S', 'L', 'R'], ['H', 'K', 'S', 'E', 'F'], ['M', 'O', 'E', 'M', 'J'], ['L', 'A', 'O', 'W', 'Y']]
            breakpoint()
            json_response = resp.get_json()

            resp = client.post('/api/score-word', json = {"gameId": gameId, "word": "CAT"})

            self.assertEqual(, 1)
            """test if the value of a passed in word equals the values below
                word length 3 would be 1 point,
                word length 7 would be the failing test with a score of 4
            """

            # self.assertIsInstance(json["gameId"], str)
            # self.assertNotEqual(games[json["gameId"]], None)
            # word_length_scores={3: 1, 4: 1, 5: 2, 6: 3, 7: 5},
            #      max_word_length_score=11,
            # games[game_id].word_list.check_word(word)