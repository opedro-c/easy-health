from flask_login import login_required
from flask_restful import Resource, request
from services.auth_service import auth_service


class AuthController(Resource):

   def post(self):
      login_data = auth_service.login(request.json)
      if login_data:
         return login_data
      else:
         return {'message': 'wrong credentials'}, 400
   
   @login_required
   def delete(self):
      auth_service.logout()
