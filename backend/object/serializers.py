from rest_framework import serializers

from django.core.exceptions import ValidationError

from .models import *


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
    photos = ObjectPhotoSerializer(many=True)
    features = ObjectFeaturesSerializer(many=True)
    bed_count = serializers.IntegerField()

    class Meta:
        model = Object
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
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
