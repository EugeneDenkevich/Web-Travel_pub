from decimal import Decimal

from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib import admin

from object.admin import *
from object.models import *
from object.logic import *


class ObjectFeatureTestCase(TestCase):

    def test_add_feature(self):
        object_1 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=False)
        feature_1 = ObjectFeature.objects.create(type='Shower',
                                                 object_id=object_1)
        feature_2 = ObjectFeature.objects.create(type='Shower',
                                                 object_id=object_1)
        data = [
            {'type': feature_1.type},
            {'type': feature_2.type}
        ]
        self.assertEqual(is_features_dublicates(data), True)


class PurchaseTestCase(TestCase):

    def setUp(self):
        self.object_1 = Object.objects.create(title='Title1',
                                              pers_num=5,
                                              description_short='Description',
                                              description_long='DescriptionDescriptionDescription',
                                              price_weekday=Decimal('120'),
                                              price_holiday=Decimal('220'),
                                              created_date='2023-05-01',
                                              is_reserved=False)
        self.object_2 = Object.objects.create(title='Title1',
                                              pers_num=5,
                                              description_short='Description',
                                              description_long='DescriptionDescriptionDescription',
                                              price_weekday=Decimal('120'),
                                              price_holiday=Decimal('220'),
                                              created_date='2023-05-01',
                                              is_reserved=False)
        self.purchase = Purchase.objects.create(fio='Eugene',
                                                sex="m",
                                                passport_country='Беларусь',
                                                address='21 Судиловского',
                                                phone_number="+375336680390",
                                                email="eugenestudio@mail.ru",
                                                telegram="@eugenvazgen",
                                                object=self.object_1,
                                                desired_arrival="2023-06-05",
                                                desired_departure="2023-06-16")

    def test_change_status(self):
        self.purchase = Purchase.objects.create(fio='Eugene',
                                           sex="m",
                                           passport_country='Беларусь',
                                           address='21 Судиловского',
                                           phone_number="+375336680390",
                                           email="eugenestudio@mail.ru",
                                           telegram="@eugenvazgen",
                                           object=self.object_1,
                                           desired_arrival="2023-06-05",
                                           desired_departure="2023-06-16")
        change_status(self.purchase)
        self.assertEqual(self.purchase.status, True)

    def test_is_object_reserved_true(self):
        data = {
            'fio': 'Eugene',
            'sex': "m",
            'passport_country': 'Беларусь',
            'address': '21 Судиловского',
            'phone_number': "+375336680390",
            'email': "eugenestudio@mail.ru",
            'telegram': "@eugenvazgen",
            'object': self.object_2,
            'desired_arrival': "2023-06-05",
            'desired_departure': "2023-06-16"
        }
        form = PurchaseAdminObjectFrom(data=data)
        self.assertTrue(form.is_valid())
    
    def test_is_object_reserved_false(self):
        data = {
            'fio': 'Eugene',
            'sex': "m",
            'passport_country': 'Беларусь',
            'address': '21 Судиловского',
            'phone_number': "+375336680390",
            'email': "eugenestudio@mail.ru",
            'telegram': "@eugenvazgen",
            'object': self.object_1,
            'desired_arrival': "2023-06-05",
            'desired_departure': "2023-06-16"
        }
        form = PurchaseAdminObjectFrom(data=data)
        self.assertFalse(form.is_valid())

    def test_check_departure_date(self):
        data = {
            'fio': 'Eugene',
            'sex': "m",
            'passport_country': 'Беларусь',
            'address': '21 Судиловского',
            'phone_number': "+375336680390",
            'email': "eugenestudio@mail.ru",
            'telegram': "@eugenvazgen",
            'object': self.object_2,
            'desired_arrival': "2023-06-05",
            'desired_departure': "2023-05-16"
        }
        form = PurchaseAdminObjectFrom(data=data)
        expected_report = {'desired_departure': [ValidationError(['Дата выезда должна быть раньше даты заезда'])]}
        self.assertEqual(str(form.errors.as_data()), str(expected_report))

    def test_finish_purchase(self):
        object_1 = Object.objects.create(title='Title1',
                                         pers_num=5,
                                         description_short='Description',
                                         description_long='DescriptionDescriptionDescription',
                                         price_weekday=Decimal('120'),
                                         price_holiday=Decimal('220'),
                                         created_date='2023-05-01',
                                         is_reserved=True)
        purchase = Purchase.objects.create(fio='Eugene',
                                                sex="m",
                                                passport_country='Беларусь',
                                                address='21 Судиловского',
                                                phone_number="+375336680390",
                                                email="eugenestudio@mail.ru",
                                                telegram="@eugenvazgen",
                                                object=object_1,
                                                desired_arrival="2023-06-05",
                                                desired_departure="2023-06-16")
        finish_purchase(purchase)
        self.assertEqual(object_1.is_reserved, False)
