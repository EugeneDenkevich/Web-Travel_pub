from django.db.models import Count

from .models import *


def get_beds_and_rooms(response_data):
    if isinstance(response_data, dict):
        # For one object
        query_beds = Bed.objects.filter(object_id=response_data.get('id')).values('type').annotate(Count('id')).order_by()
        print(query_beds)
        query_rooms = Room.objects.filter(object_id=response_data.get('id')).values('type').annotate(Count('id')).order_by()
        print(query_rooms)

        response_data['beds_types'] = []
        response_data['rooms_types'] = []
        for bed in query_beds:
            response_data['beds_types'].append(
                {dict(BEDS).get(bed.get('type')): bed.get('id__count')}
            )
        for room in query_rooms:
            response_data['rooms_types'].append(
                {dict(ROOMS).get(room.get('type')): room.get('id__count')}
            )
        return response_data
    # For all objects
    query_beds = Bed.objects.values(
        'type', 'object_id').annotate(Count('id')).order_by()
    query_rooms = Room.objects.values(
        'type', 'object_id').annotate(Count('id')).order_by()
    for object in response_data:
        object['beds_types'] = []
        object['rooms_types'] = []
        for bed in query_beds:
            if bed['object_id'] == object['id']:
                object['beds_types'].append(
                    {dict(BEDS).get(bed.get('type')): bed.get('id__count')}
                )
        for room in query_rooms:
            if room['object_id'] == object['id']:
                object['rooms_types'].append(
                    {dict(ROOMS).get(room.get('type')): room.get('id__count')}
                )
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
