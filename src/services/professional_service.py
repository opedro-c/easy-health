from models import db
from models.professional_model import ProfessionalModel
from schemas.professional_serializer import professional_serializer, professionals_serializer
from werkzeug.security import generate_password_hash


class ProfessionalService:

    def create_professional(self, obj):
        professional = professional_serializer.load(obj)
        professional.password = generate_password_hash(professional.password, method='sha256')
        db.session.add(professional)
        db.session.commit()
        return professional

    def get_professional_by_id(self, id):
        query = ProfessionalModel.query.get(id)
        return query
    
    def get_professional_by_email(self, email):
        query = ProfessionalModel.query.filter_by(email=email)
        return query.first()

    def get_all_professionals(self):
        query = ProfessionalModel.query.all()
        return query


professional_service = ProfessionalService()
