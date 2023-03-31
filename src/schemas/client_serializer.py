from models.client_model import ClientModel
from schemas import ma


class ClientSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientModel