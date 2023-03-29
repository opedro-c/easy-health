from flask import Flask
from flask_migrate import Migrate
from models import db
from controllers import api
from schemas import ma


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///easy_health.db"
    api.init_app(app)
    ma.init_app(app)
    db.init_app(app)
    Migrate(app, db)
    return app


if __name__ == '__main__':
    create_app()
