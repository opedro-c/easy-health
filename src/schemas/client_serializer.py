from models.client_model import ClientModel
from marshmallow import post_load
from schemas import ma
from schemas.client_address_serializer import ClientAddressSerializer
from schemas.health_plan_serializer import HealthPlanSerializer


class ClientSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientModel

    password = ma.Str(load_only=True)
    address = ma.Nested(ClientAddressSerializer)
    health_plan_id = ma.Nested(HealthPlanSerializer)

    @post_load
    def user(self, data):
        return ClientModel(**data)
