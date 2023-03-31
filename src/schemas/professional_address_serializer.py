from schemas import ma
from models.professional_address_model import ProfessionalAddressModel


class ProfessionalAddressSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessionalAddressModel
