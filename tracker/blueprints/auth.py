from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields


from tracker.models.users import UserSchema, User

blueprint = Blueprint("auth", __name__, url_prefix="/")

@blueprint.route("/auth", methods=["POST"])
@doc(tags=['auth'])
@use_kwargs(
    { 
        "username": fields.Str(required=True),
        "password": fields.Str(required=True)
    }
)
@marshal_with(UserSchema)
def authenticate_user(username, password):
    user = User.query.filter(User.username == username).filter(User.password == password).first()

    if user is None:
        return "Humm, that doesn't sound right", 400

    return user, 200

