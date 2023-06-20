from rest_framework.test import APITestCase
from django.core.files.images import ImageFile

from entertainments.serializers import *
from entertainments.models import *


class NearestAPITestCase(APITestCase):

    def setUp(self):
        self.nearest_1 = NearestPlace.objects.create(
            title='test nearest 1',
            description='test description',
            location='test location'
        )
        self.nearest_2 = NearestPlace.objects.create(
            title='test nearest 2',
            description='test description',
            location='test location'
        )
        self.photo_1 = PhotoNearestPlace.objects.create(
            file=ImageFile(open("mesye.png", "rb")),
            places=self.nearest_1
        )

    def test_get(self):
        url = 'http://127.0.0.1:8000/api/nearests/'
        response = self.client.get(url)
        serializer_data = NearestPlaceSerializer(self.nearest_1).data
        self.assertTrue('/media/' in serializer_data['places_photos'][0])
