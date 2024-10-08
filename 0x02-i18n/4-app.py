#!/usr/bin/env python3
"""
Flask application with Babel integration, supporting
forced locale selection via URL parameter.
"""

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

    # Default behavior: return the best match based on request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The main route that renders the home
    page template with translated text.

    Returns:
        str: Rendered HTML template for the home page.
    """
    # Render the template with translated title and header using gettext
    return render_template('4-index.html',
                           title=gettext("home_title"),
                           header=gettext("home_header"))


if __name__ == '__main__':
    # Run the application
    app.run()
