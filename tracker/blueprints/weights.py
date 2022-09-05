from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields

from tracker.extensions import db

from tracker.models.weight import Weight, WeightSchema

blueprint = Blueprint("weights", __name__, url_prefix="/")


@blueprint.route("/weights", methods=["POST"])
@doc(tags=['weights'])
@use_kwargs({"date": fields.Date(), "weight": fields.Float(), "user_id": fields.Int()})
@marshal_with(WeightSchema)
def create_weight(date, weight, user_id):
    # TODO
    # Check that user id exists
    # Check if weight exists for user on date (if so INSERT not CREATE)
    new_weight = Weight(date=date, weight=weight, user_id=user_id)
    db.session.add(new_weight)
    db.session.commit()

    return new_weight, 200


@blueprint.route("/weights", methods=["GET"])
@doc(tags=['weights'])
@marshal_with(WeightSchema(many=True))
def get_all_weights():
    weights = Weight.query.all()

    return weights, 200

@blueprint.route("/weights/<int:user_id>", methods=["GET"])
@doc(tags=['weights'])
@marshal_with(WeightSchema(many=True))
def get_weight_by_user(user_id):
    weights = Weight.query.filter(Weight.user_id == user_id)

    return weights, 200
