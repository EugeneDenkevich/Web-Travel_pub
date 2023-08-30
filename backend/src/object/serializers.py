from drf_yasg import openapi
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import exceptions
from .models import *


class FileListSerializer(serializers.ListSerializer):
    child = serializers.FileField()


class StringListSerializer(serializers.ListSerializer):
    child = serializers.CharField()


class StringDictListSerializer(serializers.ListSerializer):
    child = serializers.DictField(child=serializers.CharField())


class SocialSerializer(serializers.Serializer):
    link = serializers.CharField()
    icon = serializers.FileField()


class ObjectPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoObject
        fields = ['file',]

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res['file']


class ObjectRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def to_representation(self, instance):
        return dict(ROOMS)[instance.type]


class ObjectFeaturesSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = ObjectFeature
        fields = [
            'id',
            'type'
        ]

    def get_id(self, obj):
        for i in range(len(FEATURES_CHOICES)):
            if FEATURES_CHOICES[i][0] == obj.type:
                return i + 1



class IntegerDictListSerializer(serializers.ListSerializer):
    child = serializers.DictField(child=serializers.IntegerField())


class ObjectSerializer(serializers.ModelSerializer):
    photos = ObjectPhotoSerializer(many=True, required=False)
    features = ObjectFeaturesSerializer(many=True, required=False)
    bed_count = serializers.IntegerField(required=False)

    class Meta:
        model = Object
        exclude = [
            'created_date',
            'is_reserved'
        ]
        swagger_schema_fields = {
            'example': {
                "id": 0,
                "photos": [
                    openapi.TYPE_STRING,
                    openapi.TYPE_STRING,
                ],
                "features": [
                    {
                        "id": 0,
                        "type": openapi.TYPE_STRING,
                    }
                ],
                "bed_count": 0,
                "title": openapi.TYPE_STRING,
                "pers_num": 0,
                "description_short": openapi.TYPE_STRING,
                "description_long": openapi.TYPE_STRING,
                "price_weekday": openapi.FORMAT_DECIMAL,
                "price_holiday": openapi.FORMAT_DECIMAL,
                "beds_types": [
                    {
                        "id": 0,
                        "type": openapi.TYPE_STRING,
                        "count": 0
                    }
                ],
                "rooms_types": [
                    {
                        "id": 0,
                        "type": openapi.TYPE_STRING,
                        "count": 0
                    }
                ]
            }
        }


class PurchaseSerializer(serializers.ModelSerializer):
    object = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all())

    class Meta:
        model = Purchase
        exclude = [
            'status',
            'is_finished',
            'was_object',
        ]
 
    def validate(self, data):
        """
        Check if desired arrival lower than desired departure
        """
        if data.get('desired_arrival') > data.get('desired_departure'):
            raise exceptions.DesiredArivalExeption()
        return data
    #     house = data.get('object')
    #     """
    #     Check if house is reserved
    #     """
    #     if house.purchases.all():
    #         raise exceptions.HouseIsTakenExeption()
    #     return data


class ImageListSerializer(serializers.ListSerializer):
    child = serializers.ImageField()
