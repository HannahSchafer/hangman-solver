"""The hangman solver flask app server file."""

from flask import (Flask, jsonify, render_template, request)
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension


# Required to use Flask sessions and debug toolbar
app.secret_key = "752398u5&9563!!hml"


@app.route('/')
def splashpage():
    """Mainpage."""

    return render_template("splashpage.html")


@app.route('send-letter')
def send_letter():
    """AJAX response to send new letter choice to client."""

    return jsonify()
    
    


if __name__ == "__main__":

    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')