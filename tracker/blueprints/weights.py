from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields
import datetime

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
@use_kwargs(
    {
        "limit": fields.Int(required=False, description="Defaults to 60"),
        "start_date_range": fields.Str(
            required=False,
            description="YYYY-MM-DD, defaults to today if end_date_range is set"
        ),
        "end_date_range": fields.Str(required=False, description="YYYY-MM-DD")
    },
    location="query"
)
@marshal_with(WeightSchema(many=True))
def get_weight_by_user(user_id, limit=60, start_date_range=None, end_date_range=None):
    query = Weight.query.filter(Weight.user_id == user_id)

    # TODO check date range format
    if end_date_range:
        if start_date_range is None:
            start_date_range = datetime.date.today()

        query = (
            query
            .filter(Weight.date <= start_date_range)
            .filter(Weight.date >= end_date_range)
        )

    query = query.order_by(Weight.date.desc()).limit(limit)
    weights = query.all()

    return weights, 200


@blueprint.route("/weights", methods=["DELETE"])
@doc(tags=["weights"])
@use_kwargs(
    {
        "weight_ids": fields.Str(
            required=False,
            description="A comma seperated string of weight_ids: '4,7,22'"
        )
    },
    location="query"
)
def delete_users_by_id(weight_ids):
    # TODO - if any fail to delete, capture them here and return who was deleted and who was not
    weight_ids_to_delete = weight_ids.split(',')
    print("weight ids to delete \n\n", weight_ids_to_delete)

    for weight_id in weight_ids_to_delete:
        Weight.query.filter(Weight.id == weight_id).delete()

    db.session.commit()

    return f"weight_ids {weight_ids} have been deleted.", 200


@blueprint.route("/weights", methods=["PUT"])
@doc(tags=["weights"])
@use_kwargs({"id": fields.Int(), "weight": fields.Float()})
@marshal_with(WeightSchema)
def update_weight(id, weight):
    # todo, make sure id exists - try/catch or something
    weight_to_update = Weight.query.get(id)
    print("WEIGJT \n\n", weight)
    weight_to_update.weight = weight
    db.session.commit()

    return weight_to_update, 200
