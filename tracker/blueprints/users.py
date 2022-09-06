from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields

from tracker.extensions import db

from tracker.models.users import UserSchema, User

blueprint = Blueprint("users", __name__, url_prefix="/")


@blueprint.route("/users", methods=["POST"])
@doc(tags=['users'])
@use_kwargs({"username": fields.Str(), "email": fields.Str()})
@marshal_with(UserSchema)
def create_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return new_user, 200


@blueprint.route("/users", methods=["GET"])
@doc(tags=['users'])
@marshal_with(UserSchema(many=True))
def get_all_users():
    users = User.query.all()

    return users, 200


@blueprint.route("/users/<int:id>", methods=["GET"])
@doc(tags=['users'])
@marshal_with(UserSchema)
def get_user_by_id(id):
    user = User.query.get(id)

    return user, 200


@blueprint.route("/users", methods=["PUT"])
@doc(tags=['users'])
@use_kwargs({"id": fields.Int(), "username": fields.Str(), "email": fields.Str()})
@marshal_with(UserSchema)
def update_user_by_id(id, username, email):
    # todo, make sure id exists - try/catch or something
    user = User.query.get(id)
    user.username = username
    user.email = email
    db.session.commit()

    return user, 200


@blueprint.route("/users/<int:id>", methods=["DELETE"])
@doc(tags=['users'])
def delete_user(id):
    User.query.filter(User.id == id).delete()
    db.session.commit()

    return f"user {id} has been deleted.", 200
