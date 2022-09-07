from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields

from tracker.extensions import db

from tracker.models.goals import Goal, GoalSchema

blueprint = Blueprint("goals", __name__, url_prefix="/")


@blueprint.route("/goals", methods=["POST"])
@doc(tags=["goals"])
@use_kwargs({"goal_weight": fields.Float(), "user_id": fields.Int()})
@marshal_with(GoalSchema)
def create_goal(goal_weight, user_id):
    new_goal = Goal(goal_weight=goal_weight, user_id=user_id)
    db.session.add(new_goal)
    db.session.commit()

    return new_goal, 200


@blueprint.route("/goals", methods=["GET"])
@doc(tags=["goals"])
@marshal_with(GoalSchema(many=True))
def get_all_goals():
    goals = Goal.query.all()

    return goals, 200


@blueprint.route("/goals", methods=["PUT"])
@doc(tags=["goals"])
@use_kwargs({"id": fields.Integer(), "goal_weight": fields.Float()})
@marshal_with(GoalSchema)
def update_goal(id, goal_weight):
    goal_to_update = Goal.query.get(id)
    goal_to_update.goal_weight = goal_weight
    db.session.commit()

    return goal_to_update, 200
