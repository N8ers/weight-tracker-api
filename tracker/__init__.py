from flask import Flask

from tracker.extensions import db, migrate, ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from tracker.blueprints import hi, users

    app.register_blueprint(hi.blueprint)
    app.register_blueprint(users.blueprint)
