from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields


from tracker.models.users import UserSchema, User

blueprint = Blueprint("auth", __name__, url_prefix="/")

@blueprint.route("/", methods=["POST"])
@doc(tags=['auth'])
@use_kwargs(
    { 
        "username": fields.Str(required=True)
    }
)
@marshal_with(UserSchema)
def authenticate_user(username):
    # query db where user username & pw match

    user = User.query.filter(User.username == username).first()

    return user, 200

