from models.user_model import UserModel
from models import db


class ClientModel(UserModel):
    __tablename__ = 'client'

    address = db.relationship('ClientAddressModel', backref='client', uselist=False)
    health_plan_id = db.Column(db.String, db.ForeignKey('health_plan.name'))
