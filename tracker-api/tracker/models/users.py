from tracker.extensions import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    weights = db.relationship('Weight', backref='user', lazy=True)
    goals = db.relationship('Goal', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.id} {self.username}>'


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "username", "email")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
