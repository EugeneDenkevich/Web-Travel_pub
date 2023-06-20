from rest_framework import serializers

from .models import *


class StringListSerializer(serializers.ListSerializer):
    child = serializers.CharField()


class StringDictListSerializer(serializers.ListSerializer):
    child = serializers.DictField(child=serializers.CharField())


class InfoSerializer(serializers.ModelSerializer):
    social = StringDictListSerializer()
    phones = StringListSerializer()

    class Meta:
        model = Info
        fields = '__all__'


class FeedingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingInfo
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'
