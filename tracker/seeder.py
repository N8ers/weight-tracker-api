import datetime
import random


def plant_seed():

    user_ids = []

    def create_users():
        def create_user(username, email):

            from tracker.extensions import db
            from tracker.models.users import User

            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            print(f"{new_user.username} created")
            user_ids.append(new_user.id)

        create_user("tsuki_cat", "tsuki_cat@meow.net")
        create_user("whiskey_whiskers", "whiskey_whiskers@meow.net")
        create_user("claw_paw", "claw_paw@meow.net")

    def create_weights():
        def create_weight(date, weight, user_id):

            from tracker.extensions import db
            from tracker.models.weight import Weight

            new_weight = Weight(date=date, weight=weight, user_id=user_id)
            db.session.add(new_weight)
            db.session.commit()
            print(
                f"{new_weight.date} {new_weight.weight} {new_weight.user_id} created")

        # This will break if it's not March of any given year
        today = datetime.date.today()

        one_month_offset = today.month - 1
        one_month_ago = today.replace(month=one_month_offset)

        two_month_offset = today.month - 2
        two_months_ago = today.replace(month=two_month_offset)

        for user_id in user_ids:
            weight_one = round(random.uniform(20, 5), 1)
            weight_two = round(random.uniform(20, 5), 1)
            weight_three = round(random.uniform(20, 5), 1)

            create_weight(today, weight_one, user_id)
            create_weight(one_month_ago, weight_two, user_id)
            create_weight(two_months_ago, weight_three, user_id)

    create_users()
    create_weights()
