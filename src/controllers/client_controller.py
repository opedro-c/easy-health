from flask_restful import Resource, request
from schemas.client_serializer import client_serializer as cs, clients_serializer as css
from services.client_service import client_service


class ClientController(Resource):

    def get(self, id=None):
        if id:
            return cs.dump(client_service.get_client_by_id(id))
        return css.dump(client_service.get_all_clients())

    def post(self):
        client = client_service.create_client(request.json)
        return cs.dump(client), 201
        

    def put(self):
        pass

    def delete(self, id):
        pass
