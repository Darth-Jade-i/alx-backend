#!/usr/bin/env python3
"""Creating a basic flask app"""


from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_World() -> str:
    """Rendering the template for the flask"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
