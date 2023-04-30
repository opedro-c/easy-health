from secrets import token_hex
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_restful import Api
from models import db
from schemas import ma


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///easy_health.db"
app.config['SECRET_KEY'] = token_hex(16)
db.init_app(app)
ma.init_app(app)
api = Api(app)
login_manager = LoginManager(app)


# Imports so Migrate can recognize tables
from models.user_model import UserModel
from models.address_model import AddressModel
from models.client_model import ClientModel
from models.professional_model import ProfessionalModel
from models.subspecialties_model import subspecilaty_professional, SubspecialtyModel
from models.health_plan_model import health_plan_professional, HealthPlanModel
from models.professional_address_model import ProfessionalAddressModel
from models.client_address_model import ClientAddressModel


Migrate(app, db)


# API Resources
from controllers.client_controller import ClientController
api.add_resource(ClientController, '/clients', '/clients/<int:id>')
from controllers.professional_controller import ProfessionalController
api.add_resource(ProfessionalController, '/professionals', '/professionals/<int:id>')
from controllers.user_controller import UserController
api.add_resource(UserController, '/users')
from controllers.auth_controller import AuthController
api.add_resource(AuthController, '/auth')


# Error Mapping
api.errors = {
    'ValidationError': {
        'status': 400,
        'message': 'Data provided could not be validated!'
    }
}


@login_manager.user_loader
def load_user(user_id):
    if current_user.type == 'professional':
        user_model = ProfessionalModel
    elif current_user.type == 'client':
        user_model = ClientModel
    else:
        raise ValueError('Could not stablish user loader')
    return user_model.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)