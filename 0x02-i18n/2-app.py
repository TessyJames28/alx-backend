#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """config class to configure available languages"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """select the best match for supported languages"""
    return request.accept_languages.best_match(app.Config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """index function"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
