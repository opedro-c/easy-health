from models import db


class SubspecialtyModel(db.Model):
    __tablename__ = 'subspecialty'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
