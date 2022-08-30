from flask import Flask


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def hi():
        return "<h1>Hi there!</h1>"

    """
    User Routes (CRUD)
    """
    @app.route("/users")
    def create_user():
        pass

    @app.route("/users")
    def get_all_users():
        pass

    @app.route("/users/<id:int>")
    def get_user_by_id():
        pass

    @app.route("/users")
    def update_user_by_id():
        pass

    @app.route("/users/<id:int>")
    def delete_user():
        pass

    return app
