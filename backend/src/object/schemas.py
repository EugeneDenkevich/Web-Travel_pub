from config.utils.schemas import BasicAPISchema
from . import serializers


class ObjectSchema(BasicAPISchema):
    def retrieve(self):
        return self.swagger_auto_schema(
            operation_summary='Get house',
            operation_description='Get house',
            responses={
                200: serializers.ObjectSerializer(),
                **self.get_responses(404),
            },
        )

    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get houses',
            operation_description='Get houses',
        )
    

class PurchaseSchema(BasicAPISchema):
    def create(self):
        return self.swagger_auto_schema(
            operation_summary='Create purhase',
            operation_description='Create purchase',
            responses={
                201: serializers.PurchaseSerializer(),
                **self.get_responses(400, 401, 403)
            }
        )

    
house_schema = ObjectSchema(tags=['House'])
purchase_schema = PurchaseSchema(tags=['Purchase'])