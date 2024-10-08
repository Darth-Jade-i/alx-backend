#!/usr/bin/env python3
"""
A simple Flask app that supports
internationalization (i18n) and localization (l10n).
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict

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
    Determine the best match for supported languages
    in the following order of priority:
    1. Locale from URL parameters.
    2. Locale from user settings (if logged in).
    3. Locale from request header.
    4. Default locale (English).
    """
    # 1. Locale from URL parameters
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index page.

    :return: The rendered HTML page.
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
