from flask import Flask


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def hi():
        return "<h1>Hi there!</h1>"

    return app
