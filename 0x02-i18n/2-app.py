#!/usr/bin/env python3
"""Module for task 2
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def index_2() -> str:
    """The index function displays the home page of the web application.

    Returns:
        str: contents of the home page.
    """
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the client's preferred language.

    This function uses Flask's request object to access the client's preferred
    languages and the app's supported languages (defined in the Config class)
    to determine the best match. The best match is then returned as the locale.

    Returns:
        str: The locale code for the best match (e.g. "en", "fr").
    """
    # Get list of supported languages from Config
    supported_languages = app.config["LANGUAGES"]
    # Use request.accept_languages to get the best match
    best_match = request.accept_languages.best_match(supported_languages)
    return best_match


if __name__ == "__main__":
    app.run(debug=True)
