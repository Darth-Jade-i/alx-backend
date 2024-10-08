#!/usr/bin/env python3
"""
This module contains a Flask application with Babel
integration for handling translations and timezone settings.
"""

# import babel
# Import necessary modules from Flask and Flask-Babel packages.
from flask import Flask, render_template
from flask_babel import Babel

# Create a Flask application instance.
app = Flask(__name__)


# Create a Config class for configuring the application.
class Config:
    """
    Config class used to configure available
    languages, default locale, and timezone.
    """
    # Define the supported languages for the application.
    LANGUAGES = ["en", "fr"]

    # Set the default locale to English ("en").
    BABEL_DEFAULT_LOCALE = "en"

    # Set the default timezone to UTC.
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Apply the configuration to the Flask app.
app.config.from_object(Config)

# Instantiate the Babel object using the configured Flask app.
babel = Babel(app)


# Define a route for the root URL '/'.
@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    The index function serves the homepage of the application.
    It renders an HTML template called '1-index.html'.

    Returns:
        The rendered HTML template as a string.
    """
    # Render and return the '1-index.html' template.
    return render_template('1-index.html')


# Check if the script is executed directly (and not imported as a module).
if __name__ == '__main__':
    # Run the Flask application on the local development server.
    app.run(debug=True)
