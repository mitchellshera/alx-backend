#!/usr/bin/env python3
"""
This module contains a Flask app with Flask-Babel integration,
language selection, parametrized templates, and user login emulation.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config as config for the Flask app
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best-matching language from the supported languages.

    Returns:
        str: Best-matching language code.
    """
    forced_locale = request.args.get('locale')
    if forced_locale and forced_locale in app.config['LANGUAGES']:
        return forced_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Get user details based on user ID.

    Returns:
        dict: User details or None if not found.
    """
    user_id = request.args.get('login_as', None)
    if user_id is not None and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Executed before all other functions.
    Find a user using get_user and set it as a global on flask.g.user.
    """
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page with parametrized templates.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('5-index.html', user=g.user)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
