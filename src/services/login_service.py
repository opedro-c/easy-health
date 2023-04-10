from flask import request
from models.client_model import ClientModel
from models.professional_model import ProfessionalModel


class LoginService:

    def authentication():

        email = request.form['email']
        password = request.form['password']

        client = ClientModel.query.filter_by(email=email).first()
        profissional = ProfessionalModel.query.filter_by(email=email).first()

        if client:
            if password == client.password:
                return True
        elif profissional:
            if password == profissional.password:
                return True
        else:
            return False