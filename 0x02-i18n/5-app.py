#!/usr/bin/env python3
"""Module for task 5
"""
from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

app.url_map.strict_slashes = False


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/")
def index_5() -> str:
    """The index function displays the home page of the web application.

    Returns:
        str: contents of the home page.
    """
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the client's preferred language.

    This function uses Flask's request object to access the client's preferred
    languages and the app's supported languages (defined in the Config class)
    to determine the best match. The best match is then returned as the locale.

    Returns:
        str: The locale code for the best match (e.g. "en", "fr").
    """
    # Get the locale parameter from the incoming request
    locale = request.args.get('locale')
    # Get list of supported languages from Config
    supported_languages = app.config["LANGUAGES"]
    if locale and locale in supported_languages:
        # If the locale parameter is present and is a supported locale,
        # return it
        return locale
    else:
        # Use request.accept_languages to get the best match
        best_match = request.accept_languages.best_match(supported_languages)
        return best_match


def get_user() -> Union[Dict, None]:
    """Returns a user dictionary based on the given ID

    Returns:
        Union[Dict, None]: The user dictionary if found, otherwise None.
    """
    # Get the user_id from the login_as URL parameters
    login_id = request.args.get('login_as')
    # If the user ID exists in the URL parameters
    if login_id:
        # Get the user dictionary from the `users` dictionary using the user ID
        return users.get(int(login_id))
    # If the user ID does not exist in the URL parameters, return None
    return None


@app.before_request
def before_request() -> None:
    """Function to be executed before every request.
    """
    # Use the get_user function to get the user details
    user = get_user()
    # Set the user as a global variable on flask.g
    g.user = user


# Register the before_request function to be executed before every request
app.before_request(before_request)


if __name__ == "__main__":
    app.run(debug=True)
