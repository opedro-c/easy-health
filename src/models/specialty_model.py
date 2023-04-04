from models import db


class SpecialtyModel(db.Model):
    __tablename__ = 'specialty'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    # subspecialties = db.relationship('SubspecialtyModel', backref='specialty', cascade='all, delete, delete-orphan')
    # professionals = db.relationship('ProfessionalModel', backref='specialty')
