from schemas import ma
from models.subspecialties_model import SubspecialtyModel


class SubspecialtySerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SubspecialtyModel
