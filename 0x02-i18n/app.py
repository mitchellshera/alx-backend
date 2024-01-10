from flask import Flask, render_template, request, g
from flask_babel import Babel

import datetime
import pytz

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
babel.init_app(app)


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


@babel.timezoneselector
def get_timezone():
    """
    Determine the best-matching time zone from the user settings.

    Returns:
        str: Best-matching time zone.
    """
    forced_timezone = request.args.get('timezone')
    if forced_timezone:
        try:
            pytz.timezone(forced_timezone)
            return forced_timezone
        except pytz.UnknownTimeZoneError:
            pass

    return g.user['timezone'] if g.user and 'timezone' in g.user else app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """
    Executed before all other functions.
    Find a user using get_user and set it as a global on flask.g.user.
    """
    user = get_user()
    g.user = user
    g.current_time = get_current_time()


def get_user():
    """
    Get user details based on user ID.

    Returns:
        dict: User details or None if not found.
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


def get_current_time():
    """
    Get the current time based on the inferred time zone.

    Returns:
        datetime.datetime: Current time.
    """
    tz = pytz.timezone(get_timezone())
    return datetime.datetime.now(tz)


@app.route('/', strict_slashes=False)
def index():
    """
    Render the index page with parametrized templates.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
