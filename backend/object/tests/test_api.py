from decimal import Decimal

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from django.db.models import Count

from object.serializers import *
from object.models import *
from object.logic import *


class ObjectAPITestCase(APITestCase):

    def setUp(self) -> None:
        object_1 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        object_2 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        object_3 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        object_4 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        object_5 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        object_6 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        beds = list(dict(BEDS).keys())
        bed_1 = Bed.objects.create(type=beds[0],
                                   object_id=object_1)
        bed_2 = Bed.objects.create(type=beds[0],
                                   object_id=object_1)
        bed_3 = Bed.objects.create(type=beds[2],
                                   object_id=object_2)
        bed_4 = Bed.objects.create(type=beds[1],
                                   object_id=object_3)
        bed_5 = Bed.objects.create(type=beds[2],
                                   object_id=object_3)
        bed_6 = Bed.objects.create(type=beds[2],
                                   object_id=object_3)
        bed_7 = Bed.objects.create(type=beds[3],
                                   object_id=object_6)
        bed_8 = Bed.objects.create(type=beds[3],
                                   object_id=object_6)
        bed_9 = Bed.objects.create(type=beds[5],
                                   object_id=object_6)
        bed_10 = Bed.objects.create(type=beds[5],
                                    object_id=object_6)

    def test_get(self):
        url = 'http://127.0.0.1:8000/api/objects/'
        response = self.client.get(url)
        objects = Object.objects.all().prefetch_related('photos', 'features').annotate(
            bed_count=Count('beds')
        )
        serializer_data = ObjectSerializer(objects, many=True).data
        serializer_data = get_beds_and_rooms(serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class PurchaseAPITestCase(APITestCase):

    def test_post(self):
        object_1 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        url = 'http://127.0.0.1:8000/api/purchases/'
        data_wrong_date = {
            "fio": "Eugene",
            "sex": "m",
            "passport_country": "Беларусь",
            "address": "21 Судиловского",
            "phone_number": "+375336680390",
            "email": "eugenestudio@mail.ru",
            "telegram": "@eugenvazgen",
            "object": object_1.pk,
            "desired_arrival": "2023-06-05",
            "desired_departure": "2023-06-03"
        }
        data_isnt_reserved = {
            "fio": "Eugene",
            "sex": "m",
            "passport_country": "Беларусь",
            "address": "21 Судиловского",
            "phone_number": "+375336680390",
            "email": "eugenestudio@mail.ru",
            "telegram": "@eugenvazgen",
            "object": object_1.pk,
            "desired_arrival": "2023-06-05",
            "desired_departure": "2023-07-03"
        }
        data_is_reserved = {
            "fio": "Eugene",
            "sex": "m",
            "passport_country": "Беларусь",
            "address": "21 Судиловского",
            "phone_number": "+375336680390",
            "email": "eugenestudio@mail.ru",
            "telegram": "@eugenvazgen",
            "object": object_1.pk,
            "desired_arrival": "2023-06-05",
            "desired_departure": "2023-07-03"
        }
        res_wrong_date = self.client.post(url, data=data_wrong_date)
        res_isnt_reserved = self.client.post(url, data=data_isnt_reserved)
        res_already_reserved = self.client.post(url, data=data_is_reserved)
        error_wrong_date = {
            'desired_departure': [
                ErrorDetail(string='Дата выезда должна быть раньше даты заезда', code='invalid')
            ]
        }
        error_already_reserved = {
            'object': [
                ErrorDetail(string='Этот домик уже занят', code='invalid')
            ]
        }
        self.assertEqual(res_wrong_date.data, error_wrong_date)
        self.assertEqual(res_already_reserved.data, error_already_reserved)
