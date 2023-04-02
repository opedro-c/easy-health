from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from schemas import ma


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///easy_health.db"
db.init_app(app)
ma.init_app(app)
api = Api(app)


# Imports so Migrate can recognize tables
from models.address_model import AddressModel
from models.client_model import ClientModel
from models.professional_model import ProfessionalModel
from models.specialty_model import SpecialtyModel
from models.subspecialties_model import subspecilaty_professional, SubspecialtyModel
from models.health_plan_model import health_plan_professional, HealthPlanModel
from models.professional_address_model import ProfessionalAddressModel
from models.client_address_model import ClientAddressModel


Migrate(app, db)


# API Resources
from controllers.client_controller import ClientController
api.add_resource(ClientController, '/clients', '/clients/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)