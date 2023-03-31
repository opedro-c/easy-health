from schemas import ma
from models.specialty_model import SpecialtyModel


class SpecialtyModel(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SpecialtyModel
