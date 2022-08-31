from flask import Blueprint

blueprint = Blueprint('hi', __name__, url_prefix="/")


@blueprint.route('/', methods=["get"])
def hi():
    return "<h1>Hi there!</h1>"
