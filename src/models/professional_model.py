from models import db
from models.user_model import UserModel


class ProfessionalModel(UserModel):
    __tablename__ = 'professional'

    addresses = db.relationship('AddressModel', backref='professional')
    provides_home_service = db.Column(db.Boolean, nullable=False)
    specialty = db.Column(db.String, nullable=False)
