from flask_login import current_user, login_required
from flask_restful import Resource, request
from services.user_service import UserService


class UserController(Resource):


    @login_required
    def get(self):
        user_service = UserService(current_user.type)
        user = user_service.get_user_by_id(id)
        return user_service.user_serializer.dump(user)


    def post(self):
        user_service = UserService(request.json.get('type'))
        user = user_service.create_user(request.json)
        return user_service.user_serializer.dump(user), 201
        

    def put(self):
        pass

    def delete(self, id):
        pass
