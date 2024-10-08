#!/usr/bin/env python3
"""Module for task 0
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index() -> str:
    """The index function displays the home page of the web application.

    Returns:
        str: contents of the home page.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
