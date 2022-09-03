def create_users():
    def create_user(username, email):

        from tracker.extensions import db
        from tracker.models.users import User

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        print(f"{new_user.username} created")

    create_user("tsuki_cat", "tsuki_cat@meow.net")
    create_user("whiskey_whiskers", "whiskey_whiskers@meow.net")
    create_user("claw_paw", "claw_paw@meow.net")
