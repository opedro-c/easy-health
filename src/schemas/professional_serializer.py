from models.professional_model import ProfessionalModel
from schemas import ma


class ProfessionalSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessionalModel