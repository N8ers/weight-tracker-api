from tracker.extensions import db, ma


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_weight = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Goal {self.id} {self.goal_weight}>'


class GoalSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "goal_weight", "user_id")


goal_schema = GoalSchema()
goals_schema = GoalSchema(many=True)
