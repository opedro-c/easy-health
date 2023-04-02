from models.professional_model import ProfessionalModel
from schemas.subspecialty_serializer import SubspecialtySerializer
from schemas import ma
from marshmallow import fields

class ProfessionalSerializer(ma.SQLAlchemyAutoSchema):
    password = fields.Str(load_only=True)
    subspecialties = fields.Nested(SubspecialtySerializer)
    class Meta:
        model = ProfessionalModel