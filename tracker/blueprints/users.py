from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from marshmallow import fields

from tracker.extensions import db

from tracker.models.users import UserSchema, User

blueprint = Blueprint("users", __name__, url_prefix="/")


@blueprint.route("/users", methods=["POST"])
@use_kwargs({"username": fields.Str(), "email": fields.Str()})
@marshal_with(UserSchema)
def create_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return new_user, 200


@blueprint.route("/users", methods=["GET"])
@marshal_with(UserSchema(many=True))
def get_all_users():
    users = User.query.all()

    return users, 200


@blueprint.route("/users/<int:id>", methods=["GET"])
@marshal_with(UserSchema)
def get_user_by_id(id):
    user = User.query.get(id)

    return user, 200


@blueprint.route("/users", methods=["PUT"])
@use_kwargs({"id": fields.Int(), "username": fields.Str(), "email": fields.Str()})
@marshal_with(UserSchema)
def update_user_by_id(id, username, email):
    user = User.query.get(id)
    user.username = username
    user.email = email
    db.session.commit()

    return user, 200


@blueprint.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    User.query.filter(User.id == id).delete()
    db.session.commit()

    return f"user {id} has been deleted.", 200
