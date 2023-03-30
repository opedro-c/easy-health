from models import db


class AddressModel(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    complement = db.Column(db.String, nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professional.id'), nullable=False)
