from schemas.client_serializer import client_serializer, clients_serializer
from models.client_model import ClientModel
from models import db
from werkzeug.security import generate_password_hash

class ClientService:

    def create_client(self, obj):
        client = client_serializer.load(obj)
        client.password = generate_password_hash(client.password, method='sha256')
        db.session.add(client)
        db.session.commit()
        return client

    def get_client_by_id(self, id):
        query = ClientModel.query.get(id)
        return query
    
    def get_client_by_email(self, email):
        query = ClientModel.query.filter_by(email=email)
        return query.first()

    def get_all_clients(self):
        query = ClientModel.query.all()
        return query


client_service = ClientService()
