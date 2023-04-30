from models import db
from models.professional_model import ProfessionalModel
from models.client_model import ClientModel
from schemas.professional_serializer import professional_serializer
from schemas.client_serializer import client_serializer
from werkzeug.security import generate_password_hash


class UserService:

    def __init__(self, user_type: str) -> None:
        if user_type == 'professional':
            self.user_serializer = professional_serializer
            self.user_model = ProfessionalModel
        elif user_type == 'client':
            self.user_serializer = client_serializer
            self.user_model = ClientModel
        else:
            raise ValueError(f'UserService cannot be instanciated with user type: {user_type}')

    def create_user(self, obj):
        user = self.user_serializer.load(obj)
        user.password = generate_password_hash(user.password, method='sha256')
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, id):
        query = self.user_model.query.get(id)
        return query
    
    def get_user_by_email(self, email):
        query = self.user_model.query.filter_by(email=email)
        return query.first()

    def get_all_users(self):
        query = self.user_model.query.all()
        return query
