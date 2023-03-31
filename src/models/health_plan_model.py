from models import db


health_plan_professional = db.Table(
    'health_plan_professional',
    db.Column('health_plan_id', db.String, db.ForeignKey('health_plan.name')),
    db.Column('professional_id', db.Integer, db.ForeignKey('professional.id')),
)


class HealthPlanModel(db.Model):
    __tablename__ = 'health_plan'

    name = db.Column(db.String, primary_key=True)
    clients = db.relationship('ClientModel', backref='health_plan')
    professionals = db.relationship('ProfessionalModel', secondary=health_plan_professional, back_populates='health_plan')
