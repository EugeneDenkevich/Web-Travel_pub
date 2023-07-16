from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.images import ImageFile
from django.urls import reverse

from pages import serializers, models


class MainPageAPITestCase(APITestCase):

    def setUp(self):
        self.main_page_1 = models.MainPage.objects.create(
            title='test',
            house_title='test',
            entertainment_title='test',
        )
        self.photo_main_page_1 = models.PhotoMainPage.objects.create(
            file=ImageFile(open('tests_media/mesye.png', 'rb')),
            main_page=self.main_page_1
        )

    def test_get(self):
        url = reverse('main-page-list')
        response = self.client.get(url)
        file_name = self.photo_main_page_1.file.path.split(
                                            'tests_media')[1][1:]
        expected_data = {'description': None,
                'entertainment_description': None,
                'entertainment_title': 'test',
                'house_description': None,
                'house_title': 'test',
                'id': 1,
                'kitchen_description': None,
                'kitchen_title': 'Кухня',
                'photos': [f'http://testserver/media/'
                           f'photo_main_page/tests_media/{file_name}'],
                'title': 'test'}
        real_data = dict(response.data[0])
        self.assertEqual(real_data, expected_data)
