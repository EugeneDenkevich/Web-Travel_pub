from rest_framework import serializers
from drf_yasg import openapi

from .models import *


class StringListSerializer(serializers.ListSerializer):
    child = serializers.CharField()

    def to_representation(self, data):
        res = data.instance.phones.all()
        phone_numbers = list(map(lambda phone_object: 
                                 str(phone_object.phone), res))
        return phone_numbers


class StringDictListSerializer(serializers.ListSerializer):
    child = serializers.DictField(child=serializers.CharField())


class InfoSerializer(serializers.ModelSerializer):
    social = StringDictListSerializer(required=False)
    phones = StringListSerializer(required=False)
    currency = serializers.ChoiceField(choices=CURRENCIES)

    class Meta:
        model = Info
        fields = '__all__'
        swagger_schema_fields = {
            'example': {
                'id': 0,
                'social': [
                    {
                        'type_1': openapi.TYPE_STRING,
                    },
                    {
                        'type_2': openapi.TYPE_STRING,
                    }

                ],
                'phones': [
                    openapi.TYPE_STRING,
                    openapi.TYPE_STRING,
                ],
                'address': openapi.TYPE_STRING,
                'comment': openapi.TYPE_STRING,
                'latitude': openapi.TYPE_STRING,
                'longitude': openapi.TYPE_STRING,
                "currency": openapi.TYPE_STRING,
            }
        }


class MealInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        exclude = ['feeding']
        swagger_schema_fields = {
            'example': {
                'id': 0,
                'title': openapi.TYPE_STRING,
                'time': openapi.TYPE_STRING,
                "price": openapi.FORMAT_DECIMAL,
            }
        }


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ['feeding']


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        exclude = ['rules', 'created_at', 'id']
