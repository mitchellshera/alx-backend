#!/usr/bin/env python3
"""
This module contains a Flask app with Flask-Babel integration,
language selection, parametrized templates, user login emulation,
and time zone selection.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


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

    if g.user and 'locale' in g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        header_locale = header_locale.split(',')[0]
        if header_locale in app.config['LANGUAGES']:
            return header_locale

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    Determine the best-matching time zone.

    Returns:
        str: Best-matching time zone.
    """
    # 1. Time zone from URL parameters
    forced_timezone = request.args.get('timezone')
    if forced_timezone:
        try:
            pytz.timezone(forced_timezone)
            return forced_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 2. Time zone from user settings (if the user is logged in)
    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


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
    Find a user using get_user, set it as a global on flask.g.user,
    and set the time zone on flask.g.timezone.
    """
    user = get_user()
    g.user = user
    g.timezone = get_timezone()


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page with parametrized templates.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
