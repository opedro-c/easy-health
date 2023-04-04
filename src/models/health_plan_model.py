from models import db


health_plan_professional = db.Table(
    'health_plan_professional',
    db.Column('health_plan_id', db.String, db.ForeignKey('health_plan.id')),
    db.Column('professional_id', db.Integer, db.ForeignKey('professional.id')),
)


class HealthPlanModel(db.Model):
    __tablename__ = 'health_plan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    professionals = db.relationship('ProfessionalModel', secondary=health_plan_professional, back_populates='accepted_health_plans')
