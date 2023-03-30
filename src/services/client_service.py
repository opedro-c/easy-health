from flask_restful import Resource, request
from models import db


class ClientService(Resource):

    
    def get(self, id=None):
        return {'hello': f'world com {id}'} if id else {'hello': 'world sem id'}

    def post(self):
        pass

    def put(self):
        pass

    def delete(self, id):
        pass
