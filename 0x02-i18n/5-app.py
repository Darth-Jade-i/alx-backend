#!/usr/bin/env python3
"""
Flask application with mocked user login, Babel integration, and
dynamic content based on user login status.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Optional, Dict

# Initialize the Flask application
app = Flask(__name__)

# Mock user table to emulate a database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Configuration class for Flask and Babel settings
class Config:
    """
    Configuration class that defines supported languages,
    default locale, and timezone for the application.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language/locale
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


# Apply the configuration to the app
app.config.from_object(Config)

# Initialize Babel with the Flask app
babel = Babel(app)


def get_user() -> Optional[Dict[str, Optional[str]]]:
    """
    Retrieves a user dictionary based on the login_as parameter.

    Returns:
        dict: The user dictionary if found, otherwise None.
    """
    # Get the user ID from the 'login_as' URL parameter
    user_id = request.args.get('login_as')

    # If user_id is present and is in the
    # users dictionary, return the user data
    if user_id and int(user_id) in users:
        return users[int(user_id)]

    # If user_id is not valid or not present, return None
    return None


@app.before_request
def before_request():
    """
    This function runs before each request and sets the user
    in the global context if a valid user is logged in.
    """
    # Retrieve the user using the get_user function
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Selects the best match language from
    the client's request or URL parameter.

    Returns:
        str: The selected language/locale.
    """
    # Check if 'locale' parameter is in the URL
    # and if it matches supported languages
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    # If no locale parameter, fall back to the
    # user's preferred language if logged in
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Default behavior: return the best match based on request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The main route that renders the home
    page template with translated text.
    It displays a custom message if the user is logged in.

    Returns:
        str: Rendered HTML template for the home page.
    """
    # Render the template with appropriate messages based on user login status
    return render_template('5-index.html')


if __name__ == '__main__':
    # Run the application
    app.run()
