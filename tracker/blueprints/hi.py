from flask import Blueprint
from flask_apispec import doc


from tracker.extensions import docs

blueprint = Blueprint('hi', __name__, url_prefix="/")


@blueprint.route('/', methods=["get"])
@doc(tags=['hi'])
def hi_msg():
    return "<h1>Hi there!</h1>"


docs.register(hi_msg, blueprint=blueprint.name)
