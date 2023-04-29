from .client_service import client_service
from flask_login import login_user, current_user, logout_user
from .professional_service import professional_service
from werkzeug.security import check_password_hash


class AuthService:
    
   def login(self, data):
      professional = professional_service.get_professional_by_email(data.get('email'))
      client = client_service.get_client_by_email(data.get('email'))
      user = client or professional

      if client:
         user_type = 'client'
      if professional:
         user_type = 'professional'

      if not (client or professional):
         return None
      
      password_ok = check_password_hash(user.password, data.get('password'))

      if password_ok:
         login_ok = login_user(user)
      if login_ok:
         return {'id': user.id}

   def logout(self):
      logout_user(current_user)

auth_service = AuthService()