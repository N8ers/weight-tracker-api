from tracker.extensions import db, ma


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_weight = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Goal {self.id} {self.goal_weight}>'

    # This query can porobably be a helper, it's used in 3 places
    @staticmethod
    def last_recorded_weight(user_id):
        from tracker.models.weight import Weight

        weight = (
            Weight.query
            .filter(Weight.user_id == user_id)
            .order_by(Weight.date.desc())
            .first()
        )

        return weight.weight

    @staticmethod
    def total_lost(user_id):
        from tracker.models.weight import Weight

        highest_weight = (
            Weight.query
            .filter(Weight.user_id == user_id)
            .order_by(Weight.weight.desc())
            .first()
        )

        current_weight = (
            Weight.query
            .filter(Weight.user_id == user_id)
            .order_by(Weight.date.asc())
            .first()
        )

        total_weight_lost = round(
            highest_weight.weight - current_weight.weight, 2)

        return total_weight_lost

    @staticmethod
    def distance_to_goal(user_id, goal_weight):
        from tracker.models.weight import Weight

        weight = (
            Weight.query
            .filter(Weight.user_id == user_id)
            .order_by(Weight.date.desc())
            .first()
        )

        weight_from_goal = weight.weight - goal_weight

        return weight_from_goal


class GoalSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "goal_weight", "user_id")


goal_schema = GoalSchema()
goals_schema = GoalSchema(many=True)
