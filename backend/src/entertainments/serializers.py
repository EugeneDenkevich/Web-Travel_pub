from rest_framework import serializers
from drf_yasg import openapi

from .models import *


class FileListSerializer(serializers.ListSerializer):
    child = serializers.FileField()


class EntertainmentPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentPrice
        fields = '__all__'

    def to_representation(self, instance):
        return {instance.header: f'{instance.price}'}
    

class EntertainmentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoEntertainment
        fields = [
            'file'
        ]

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res['file']


class EntertainmentSerializer(serializers.ModelSerializer):
    prices = EntertainmentPriceSerializer(many=True, required=False)
    photos = EntertainmentPhotoSerializer(many=True)

    class Meta:
        model = Entertainment
        fields = '__all__'
        swagger_schema_fields = {
            'required': [
                'title',
                'description_short'
            ],
            'example': {
                'id': 0,
                'prices': [
                {
                    'serv_1': openapi.FORMAT_DECIMAL
                },
                {
                    'serv_2': openapi.FORMAT_DECIMAL
                }
                ],
                'photos': [
                    openapi.TYPE_STRING,
                    openapi.TYPE_STRING,
                ],
                'title': openapi.TYPE_STRING,
                'description_short': openapi.TYPE_STRING,
                'description_long': openapi.TYPE_STRING,
            }
        }


class NearestPlaceSerializer(serializers.ModelSerializer):
    places_photos = FileListSerializer(required=False)

    class Meta:
        model = NearestPlace
        fields = '__all__'
        swagget_schema_fields = {
            'required': [
                'title'
            ]
        }


class GaleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGalery
        fields = ['file',]
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res['file']


class GalerySerializer(serializers.ModelSerializer):
    photos = GaleryPhotoSerializer(many=True, required=False)

    class Meta:
        model = Galery
        fields = '__all__'
        swagger_schema_fields = {
            'example': {
                'id': 0,
                'photos': [
                    openapi.TYPE_STRING,
                    openapi.TYPE_STRING,
                ],
                'title': openapi.TYPE_STRING
            }
        }