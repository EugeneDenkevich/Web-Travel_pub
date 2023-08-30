from config.utils.schemas import BasicAPISchema
from drf_yasg import openapi

from . import serializers, exceptions


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
                # 409: openapi.Schema(
                #     type=openapi.TYPE_OBJECT,
                #     properties={
                #         "details": openapi.Schema(
                #             type=openapi.TYPE_STRING,
                #             default=exceptions.HOUSE_TAKEN)
                #     }
                # ),
                422 : openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "details": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            default=exceptions.DESIRED_ARRIVAL)
                    }
                ),
                **self.get_responses(400, 404)
            }
        )


house_schema = ObjectSchema(tags=['House'])
purchase_schema = PurchaseSchema(tags=['Purchase'])
