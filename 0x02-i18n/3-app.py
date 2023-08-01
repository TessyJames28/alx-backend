#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """index function"""
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('3-index.html', home_title=home_title, home_header=home_header)  # nopep8


if __name__ == "__main__":
    app.run(debug=True)
