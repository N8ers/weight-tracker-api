from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields

from tracker.extensions import db

from tracker.models.goals import Goal, GoalSchema, goal_schema

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


@blueprint.route("/goals/<int:user_id>", methods=["GET"])
@doc(tags=["goals"])
@use_kwargs({"show_progress": fields.Bool(required=False)}, location="query")
def get_goal_by_user(user_id, show_progress):
    goal_result = Goal.query.filter(Goal.user_id == user_id).first()

    goal = goal_schema.dump(goal_result)

    if show_progress:
        goal["last_recored_weight"] = goal_result.last_recorded_weight(user_id)
        goal["goal_progress"] = goal_result.total_lost(user_id)
        goal["distance_to_goal"] = goal_result.distance_to_goal(
            user_id, goal_result.goal_weight)

    return goal, 200
