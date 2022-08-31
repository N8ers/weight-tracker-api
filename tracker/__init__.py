from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apispec import use_kwargs, marshal_with
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
    @marshal_with(UserSchema)
    def create_user(username, email):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user), 200

    @app.route("/users", methods=["GET"])
    def get_all_users():
        users = User.query.all()

        return users_schema.dump(users), 200

    @app.route("/users/<int:id>", methods=["GET"])
    def get_user_by_id(id):
        user = User.query.get(id)

        return user_schema.dump(user), 200

    @app.route("/users", methods=["PUT"])
    @use_kwargs({"id": fields.Int(), "username": fields.Str(), "email": fields.Str()})
    @marshal_with(UserSchema)
    def update_user_by_id(id, username, email):
        user = User.query.get(id)
        user.username = username
        user.email = email
        db.session.commit()

        return user_schema.dump(user), 200

    @app.route("/users/<int:id>", methods=["DELETE"])
    def delete_user(id):
        User.query.filter(User.id == id).delete()
        db.session.commit()

        return f"user {id} has been deleted.", 200

    return app
