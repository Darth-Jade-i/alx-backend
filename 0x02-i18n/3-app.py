#!/usr/bin/env python3
"""
This module contains a Flask application with Babel integration,
including localization and translation of text using message IDs.
"""

# import babel
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

# Initialize the Flask application
app = Flask(__name__)


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


@babel.localeselector
def get_locale():
    """
    Selects the best match language from the client's request.

    Returns:
        str: The best matching language from supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The main route that renders the home page template with translated text.

    Returns:
        str: Rendered HTML template for the home page.
    """
    # Render the template with translated title and header
    return render_template('3-index.html',
                           title=gettext("home_title"),
                           header=gettext("home_header"))


if __name__ == '__main__':
    # Run the application
    app.run()
