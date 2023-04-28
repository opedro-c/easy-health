from flask import request
from flask_restful import Resource
from schemas.professional_serializer import professional_serializer as ps, professionals_serializer as pss
from services.professional_service import professional_service


class ProfessionalController(Resource):


    def get(self, id=None):
        if id:
            return ps.dump(professional_service.get_professional_by_id(id))
        return pss.dump(professional_service.get_all_professionals())

    def post(self):
        professional = professional_service.create_professional(request.json)
        return ps.dump(professional), 201

    def put(self):
        pass

    def delete(self):
        pass
