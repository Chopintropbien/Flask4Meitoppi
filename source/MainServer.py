__author__ = 'andrei'

from flask import Flask, jsonify
from SQLengine import andrei_dict
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/user/<username>")
def show_user_profile(username):
    if username == 'chiffa' or username == 'andrei':
        return jsonify(andrei_dict)
    else:
        return jsonify({'Error':'No Such User!'})


if __name__ == "__main__":
    app.run()
