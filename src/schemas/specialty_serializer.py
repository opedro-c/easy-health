from schemas import ma
from schemas.subspecialty_serializer import SubspecialtySerializer
from models.specialty_model import SpecialtyModel


class SpecialtyModel(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SpecialtyModel
        include_relationships = True
        include_fk = True
        load_instance = True

    subspecialties = ma.Nested(SubspecialtySerializer, many=True)
