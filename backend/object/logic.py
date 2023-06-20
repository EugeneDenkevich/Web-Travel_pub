from django.db.models import Count
from django.shortcuts import redirect

from .models import *


def get_beds_and_rooms(response_data):
    query_beds = Bed.objects.values(
        'type', 'object_id').annotate(Count('id')).order_by()
    query_rooms = Room.objects.values(
        'type', 'object_id').annotate(Count('id')).order_by()
    for object in response_data:
        object['beds_types'] = []
        object['rooms_count'] = []
        for bed, room in zip(query_beds, query_rooms):
            if bed['object_id'] == object['id']:
                object['beds_types'].append(
                    {dict(BEDS)[bed['type']]: bed['id__count']})
            if room['object_id'] == object['id']:
                object['rooms_count'].append(
                    {dict(ROOMS)[room['type']]: room['id__count']})
    return response_data


def is_features_dublicates(cleaned_data):
    """
    Check if object's feature has a dublicate
    """
    res = [f.get('type') for f in cleaned_data]
    if res[-1] in res[:-1]:
        return True
    else:
        return False
    
def change_status(purchase):
    if purchase is None:
            return
    else:
        try:
            house = purchase.object
            house_is_reserved = purchase.object.is_reserved
        except:
            return
        if purchase.status == True:
            if house_is_reserved == True:
                purchase.status = False
                purchase.save()
                house.is_reserved = False
                house.save()
            else:
                purchase.status = False
                purchase.save()
        elif purchase.status == False:
            if house.is_reserved == False:
                purchase.status = True
                purchase.save()
                house.is_reserved = True
                house.save()
            else:
                purchase.status = True
                purchase.save()


def finish_purchase(purchase):
    purchase.is_finished = True
    purchase.was_object = purchase.object
    purchase.save()
    house = purchase.object
    house.is_reserved = False
    purchase.object = None
    purchase.save()
    house.save()