"""
This module contains a Flask app with Flask-Babel integration,
language selection, and parametrized templates.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)

# Instantiate Babel object
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page with parametrized templates.

    Returns:
        str: Rendered HTML content.
    """
    home_title = _('Welcome to Holberton')
    home_header = _('Hello world!')

    return render_template('3-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run()
