from config.utils.schemas import BasicAPISchema
from . import serializers

  
class InfoSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get info',
            operation_description='Get info',
        )


class DishSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get dishes',
            operation_description='Get dishes',
        )


class MealSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get meals',
            operation_description='Get meals',
        )

class RuleSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get rules',
            operation_description='Get rules',
        )


info_schema = InfoSchema(tags=['Info'])
dish_schema = DishSchema(tags=['Dish'])
feeding_info_schema = MealSchema(tags=['Meals'])
rule_schema = RuleSchema(tags=['Rule'])