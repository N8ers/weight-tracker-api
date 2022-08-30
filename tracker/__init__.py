from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apispec import use_kwargs
from marshmallow import fields
from flask_marshmallow import Marshmallow


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    ma = Marshmallow(app)

    """
    User Model
    """
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return f'<User {self.id} {self.username}>'

    """
    User Schema
    """
    class UserSchema(ma.Schema):
        class Meta:
            # Fields to expose
            fields = ("id", "username", "email")

    user_schema = UserSchema()
    users_schema = UserSchema(many=True)

    @app.route("/")
    def hi():
        return "<h1>Hi there!</h1>"

    """
    User Routes (CRUD)
    """
    @app.route("/users", methods=["POST"])
    @use_kwargs({"username": fields.Str(), "email": fields.Str()})
    def create_user(username, email):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user), 200

    @app.route("/users", methods=["GET"])
    def get_all_users():
        pass

    @app.route("/users/<int:id>", methods=["GET"])
    def get_user_by_id(id):
        pass

    @app.route("/users", methods=["PUT"])
    def update_user_by_id():
        pass

    @app.route("/users/<int:id>", methods=["DELETE"])
    def delete_user(id):
        pass

    return app
