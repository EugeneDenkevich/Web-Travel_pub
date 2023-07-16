from config.utils.schemas import BasicAPISchema
from . import serializers


class EntertainmentsSchema(BasicAPISchema):
    def retrieve(self):
        return self.swagger_auto_schema(
            operation_summary='Get entertainment',
            operation_description='Get entertainment',
            responses={
                200: serializers.EntertainmentSerializer(),
                **self.get_responses(404),
            },
        )

    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get entertainments',
            operation_description='Get entertainments',
        )
    

class GalerySchema(BasicAPISchema):
    def retrieve(self):
        return self.swagger_auto_schema(
            operation_summary='Get galery',
            operation_description='Get galery',
            responses={
                200: serializers.GalerySerializer(),
                **self.get_responses(404),
            },
        )

    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get galeries',
            operation_description='Get galeries',
        )
    

class NearestSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get nearesrs',
            operation_description='Get nearesrs',
        )


entertainment_schema = EntertainmentsSchema(tags=['Entertainment'])
galery_schema = GalerySchema(tags=['Galery'])
nearest_schema = NearestSchema(tags=['Nearests Places'])