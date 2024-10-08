#!/usr/bin/env python3
"""
This module contains a basic Flask
application that renders a simple HTML page.
"""

# Import the necessary module from the Flask package.
from flask import Flask, render_template

# Create a Flask application instance.
app = Flask(__name__)


# Define a route for the root URL '/'.
@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    The index function serves the homepage of the application.
    It renders an HTML template called '0-index.html'.

    Returns:
        The rendered HTML template as a string.
    """
    # Render and return the '0-index.html' template.
    return render_template('0-index.html')


# Check if the script is executed directly (and not imported as a module).
if __name__ == '__main__':
    # Run the Flask application on the local development server.
    app.run(debug=True)
