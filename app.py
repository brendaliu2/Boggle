from cgi import test
from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating uuid generates randomness (codes)
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return {"gameId": game_id, "board": game.board}

@app.post('/api/score-word')
def score_word():
    """Accepts post request with JSON for game id and the word"""

    #get word user typed via AJAX
    # check_word(word)
        # if not jsonify({result: 'not word})
    # check_word_on_board(word)
        # if not jsonifty ({resutl: 'not-on-board'})
    #jsonify({result:'ok'})

    word = request.json['word']
    game_id = request.json['gameId']

    # result = test
    # jsonify(result="test") another way to jsonify
    if not games[game_id].word_list.check_word(word):
        return jsonify({"result": 'not word'})
    if not games[game_id].check_word_on_board(word):
        return jsonify ({"result": 'not-on-board'})

    return jsonify({"result":'ok'})
