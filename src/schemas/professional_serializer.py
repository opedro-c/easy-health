from models.professional_model import ProfessionalModel
from schemas.subspecialty_serializer import SubspecialtySerializer
from schemas.professional_address_serializer import ProfessionalAddressSerializer
from schemas.health_plan_serializer import HealthPlanSerializer
from schemas import ma


class ProfessionalSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessionalModel
        include_relationships = True
        include_fk = True
        load_instance = True
    password = ma.Str(load_only=True)
    subspecialties = ma.Nested(SubspecialtySerializer, many=True)
    addresses = ma.Nested(ProfessionalAddressSerializer, many=True)
    accepted_health_plans = ma.Nested(HealthPlanSerializer, many=True)
