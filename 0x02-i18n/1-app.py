#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """config class to configure available languages"""

    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = app.Config(['LANGUAGES'])
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """index function"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
