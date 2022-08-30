from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    """
    User Model
    """
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username

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

    @app.route("/users/<int:id>")
    def get_user_by_id(id):
        pass

    @app.route("/users")
    def update_user_by_id():
        pass

    @app.route("/users/<int:id>")
    def delete_user(id):
        pass

    return app
