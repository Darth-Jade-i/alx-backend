#!/usr/bin/env python3
"""
A simple Flask app that supports internationalization (i18n)
and localization (l10n) with timezone handling.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError

# Mock user database
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
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user(user_id: int) -> Optional[Dict[str, Optional[str]]]:
    """
    Retrieve a user from the mock database by ID.

    :param user_id: The ID of the user to retrieve.
    :return: The user dictionary if found, otherwise None.
    """
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """
    This function runs before each request
    and sets the user in the global context.
    """
    user_id = request.args.get("login_as")
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determine the best match for supported
    languages in the following order of priority:
    1. Locale from URL parameters.
    2. Locale from user settings (if logged in).
    3. Locale from request header.
    4. Default locale (English).
    """
    # Locale from URL parameters
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale

    # Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # locale from request header
    url_locale = request.headers.get('locale', None)
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # locale default
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the appropriate time zone
    for the user in the following order:
    1. Time zone from URL parameters.
    2. Time zone from user settings (if logged in).
    3. Default time zone (UTC).

    Validate the time zone before returning it.
    """
    # 1. Time zone from URL parameters
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except UnknownTimeZoneError:
            pass

    # 2. Time zone from user settings
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except UnknownTimeZoneError:
                pass

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    Renders the index page.

    :return: The rendered HTML page.
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run()
