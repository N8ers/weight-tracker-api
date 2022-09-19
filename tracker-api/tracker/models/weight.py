from tracker.extensions import db, ma


class Weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Weight {self.id} {self.weight} {self.user_id}>'


class WeightSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "date", "weight", "user_id")


weight_schema = WeightSchema()
weights_schema = WeightSchema(many=True)
