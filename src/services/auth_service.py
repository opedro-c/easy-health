from .client_service import client_service
from flask_login import login_user
from .professional_service import professional_service
from werkzeug.security import check_password_hash


class AuthService:
    
    def login(self, data):
         client = client_service.get_client_by_email(data.get('email'))
         professional = professional_service.get_professional_by_email(data.get('email'))
         user = client or professional
         password_ok = check_password_hash(user.password, data.get('password'))
         if password_ok:
            login_ok = login_user(user)
         if login_ok:
            return ['professional', user.id]

auth_service = AuthService()