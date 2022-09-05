import os

from flask import Flask

from tracker.extensions import db, migrate, ma, docs
from tracker.models import users, weight


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    register_blueprints(app)

    docs.init_app(app)

    for (fpath, view_function) in app.view_functions.items():
        blueprints_to_add_to_swagger = ['hi', 'users', 'weights']

        blueprint_name = fpath.split(".")[0]
        if blueprint_name in blueprints_to_add_to_swagger:
            docs.register(view_function, blueprint=blueprint_name)

    @app.cli.command("seed_db")
    def seed_db():
        from tracker.seeder import plant_seed
        plant_seed()

    @app.cli.command("drop_data")
    def drop_data():
        from tracker.seeder import drop_all_data
        drop_all_data()

    return app


def register_blueprints(app):
    from tracker.blueprints import hi, users, weights

    app.register_blueprint(hi.blueprint)
    app.register_blueprint(users.blueprint)
    app.register_blueprint(weights.blueprint)
