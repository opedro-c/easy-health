from models.user_model import UserModel
from models import db


class ClientModel(UserModel):
    __tablename__ = 'client'

    health_plan = db.Column(db.String, nullable=False)
