"""The hangman solver flask app server file."""

from flask import (Flask, jsonify, render_template, request)
from flask_debugtoolbar import DebugToolbarExtension
from hangman_logic1 import start_game, play_game

app = Flask(__name__)
# Required to use Flask sessions and debug toolbar
app.secret_key = "752398u5&9563!!hml"


@app.route('/')
def splashpage():
    """Mainpage."""

    return render_template("index.html")


@app.route('/play-game')
def send_play_game():
    """Responds to ajax request to start and play game."""

    gameId = start_game()
    play_dict = play_game(gameId)

    return jsonify(play_dict)

    
    


if __name__ == "__main__":

    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')