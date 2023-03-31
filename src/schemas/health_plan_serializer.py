from schemas import ma
from models.health_plan_model import HealthPlanModel


class HealthPlanSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = HealthPlanModel