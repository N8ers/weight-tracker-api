from tracker.extensions import db, ma


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_weight = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Goal {self.id} {self.goal_weight}>'

    @classmethod
    def goal_progress(cls):
        # query weight by user
        # get highest weight
        # subtract it from the goal
        # progress = result
        return 12

    @staticmethod
    def distance_from_goal():
        # get last recoreded weight
        # subtract from goal
        return 12


class GoalSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "goal_weight", "user_id")


goal_schema = GoalSchema()
goals_schema = GoalSchema(many=True)
