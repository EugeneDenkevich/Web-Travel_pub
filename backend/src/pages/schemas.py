from config.utils.schemas import BasicAPISchema
from . import serializers


class MainPageSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get main page',
            operation_description='Get main page',
        )
    

class BackPhotoSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get background photos',
            operation_description='Get background photos',
        )
    

class PolicyAgreementSchema(BasicAPISchema):
    def list(self):
        return self.swagger_auto_schema(
            operation_summary='Get Policy and Agreement',
            operation_description='Get Policy and Agreement',
        )
    

main_page_schema = MainPageSchema(tags=['Main page'])
page_names_schema = BackPhotoSchema(tags=['Background photos'])
policy_agreement_schema = PolicyAgreementSchema(tags=['Policy and Agreement'])