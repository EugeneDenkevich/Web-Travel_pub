from rest_framework import serializers

from .models import *


class FileListSerializer(serializers.ListSerializer):
    child = serializers.FileField()


class EntertainmentPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentPrice
        fields = '__all__'

    def to_representation(self, instance):
        return {instance.header: instance.price}
    

class EntertainmentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoEntertainment
        fields = [
            'file'
        ]


class EntertainmentSerializer(serializers.ModelSerializer):
    prices = EntertainmentPriceSerializer(many=True)
    photos = EntertainmentPhotoSerializer(many=True)

    class Meta:
        model = Entertainment
        fields = [
            'title',
            'description_short',
            'description_long',
            'prices',
            'photos',
        ]


class NearestPlaceSerializer(serializers.ModelSerializer):
    places_photos = FileListSerializer()

    class Meta:
        model = NearestPlace
        fields = '__all__'


class GaleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGalery
        fields = ['file',]
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res['file']


class GalerySerializer(serializers.ModelSerializer):
    photos = GaleryPhotoSerializer(many=True)

    class Meta:
        model = Galery
        fields = '__all__'