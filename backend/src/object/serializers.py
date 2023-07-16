from collections import OrderedDict

from drf_yasg import openapi
from rest_framework import serializers
from django.db.models import Count
from django.core.exceptions import ValidationError

from .models import *


class Test(serializers.Serializer):
    rooms_count = serializers.CharField()
    bed_types = serializers.CharField()


class FileListSerializer(serializers.ListSerializer):
    child = serializers.FileField()


class StringListSerializer(serializers.ListSerializer):
    child = serializers.CharField()


class StringDictListSerializer(serializers.ListSerializer):
    child = serializers.DictField(child=serializers.CharField())


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        exclude = '__all__'


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
    class Meta:
        model = ObjectFeature
        fields = '__all__'

    def to_representation(self, instance):
        return dict(FEATURES_CHOICES)[instance.type]


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
                    openapi.TYPE_STRING,
                    openapi.TYPE_STRING,
                ],
                "bed_count": 0,
                "title": openapi.TYPE_STRING,
                "pers_num": 0,
                "description_short": openapi.TYPE_STRING,
                "description_long": openapi.TYPE_STRING,
                "price_weekday": openapi.FORMAT_DECIMAL,
                "price_holiday": openapi.FORMAT_DECIMAL,
                # "created_date": openapi.FORMAT_DATE,
                # "is_reserved": openapi.TYPE_BOOLEAN,
                "beds_types": [
                    {
                        "type_1": 0,
                    },
                    {
                        "type_2": 0,
                    },
                ],
                "rooms_types": [
                    {
                        "type_1": 0,
                    },
                    {
                        "type_2": 0,
                    },
                ]
            },
        }


class PurchaseSerializer(serializers.ModelSerializer):
    object = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all())

    class Meta:
        model = Purchase
        fields = [
            'fio',
            'sex',
            'passport_country',
            'address',
            'phone_number',
            'email',
            'telegram',
            'object',
            'desired_arrival',
            'desired_departure',
        ]


    def validate(self, data):
        """
        Check if desired arrival lower than desired departure
        """
        if data.get('desired_arrival') > data.get('desired_departure'):
            raise ValidationError({
                'desired_departure': 'Дата выезда должна быть раньше даты заезда'
            })
        house = data.get('object')
        """
        Check if house is reserved
        """
        if house.purchases.all():
            raise ValidationError({
                'object': 'Этот домик уже занят'
            })
        return data


class ImageListSerializer(serializers.ListSerializer):
    child = serializers.ImageField()
