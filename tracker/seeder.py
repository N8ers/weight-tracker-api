users = []

def create_users():
    def create_user(username, email):

        from tracker.extensions import db
        from tracker.models.users import User

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        # db.session.commit()
        print(f"{new_user.username} created")
        users.append(new_user)

    create_user("tsuki_cat", "tsuki_cat@meow.net")
    create_user("whiskey_whiskers", "whiskey_whiskers@meow.net")
    create_user("claw_paw", "claw_paw@meow.net")

def create_weights(): 
    def create_weight(date, weight, user_id):

        from tracker.extensions import db
        from tracker.models.users import User

        new_weight = Weight(date=date, weight=weight, user_id=user_id)
        db.session.add(new_weight)
        # db.session.commit()
        print(f"{new_weight} created")

        
    today = null
    one_week_ago = null
    two_weeks_ago = null
    three_weeks_ago = null
    four_weeks_ago = null

    for user in users:
        weight = null
        create_weight(today, weight, user.id)
        create_weight(one_week_ago, weight, user.id)
        create_weight(two_weeks_ago, weight, user.id)
        create_weight(three_weeks_ago, weight, user.id)
        create_weight(four_weeks_ago, weight, user.id)