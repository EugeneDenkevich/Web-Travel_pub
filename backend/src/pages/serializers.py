from rest_framework import serializers
from drf_yasg import openapi

from . import models

class PhotoMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoMainPage
        fields = ['file',]

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res.get('file')


class MainPageModelSerializer(serializers.ModelSerializer):
    photos = PhotoMainPageSerializer(many=True)

    class Meta:
        model = models.MainPage
        exclude = ['id', 'was_changed']
        swagger_schema_fields = {
            'required': [
                'title',
                'kitchen_title',
                'house_title',
                'entertainment_title',
            ],
            'example': {
                "photos": [
                    openapi.TYPE_STRING,
                    openapi.TYPE_STRING
                ],
                "title": openapi.TYPE_STRING,
                "description": openapi.TYPE_STRING,
                "house_title": openapi.TYPE_STRING,
                "house_description": openapi.TYPE_STRING,
                "kitchen_title": openapi.TYPE_STRING,
                "kitchen_description": openapi.TYPE_STRING,
                "entertainment_title": openapi.TYPE_STRING,
                "entertainment_description": openapi.TYPE_STRING,
            }
        }


class BackPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BackPhoto
        exclude = ['id']
        swagger_schema_fields = {
            'required': [
                'photo_m',
                'photo_h',
                'photo_k',
                'photo_e',
            ],
        }

class PolicyAgreementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PolicyAgreement
        exclude = ['id']
        swagger_schema_fields = {
            'required': [
                'policy',
                'agreement',
            ],
        }