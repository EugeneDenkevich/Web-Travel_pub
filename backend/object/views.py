from rest_framework import generics
from django.db.models import Count

from .logic import get_beds_and_rooms
from .models import *
from .serializers import *


class ObjectListAPIView(generics.ListAPIView):
    queryset = Object.objects.all().prefetch_related('photos', 'features').annotate(
        bed_count=Count('beds')
    )
    serializer_class = ObjectSerializer

    def list(self, request, *args, **kwargs):
        """
        Append beds_types and rooms_count by 2 query instead of the whole list of COUNT(*) query
        """
        response = super().list(request, *args, **kwargs)
        response.data = get_beds_and_rooms(response.data)
        return response


class ObjectRetrieveApiView(generics.RetrieveAPIView):
    queryset = Object.objects.all().annotate(
        bed_count=Count('beds')
    )
    serializer_class = ObjectSerializer


# class DishListAPIView(generics.ListAPIView):
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer


# class FeedingInfoListAPIView(generics.ListAPIView):
#     queryset = FeedingInfo.objects.all()
#     serializer_class = FeedingInfoSerializer


# class EntertaimentListAPIView(generics.ListAPIView):
#     queryset = Entertaiment.objects.all().prefetch_related('prices', 'photos')
#     serializer_class = EntertaimentSerializer


# class EntertaimentRetrieveApiView(generics.RetrieveAPIView):
#     queryset = Entertaiment.objects.all()
#     serializer_class = EntertaimentSerializer


# class RuleListAPIView(generics.ListAPIView):
#     queryset = Rule.objects.all()
#     serializer_class = RuleSerializer


# class InfoListAPIView(generics.ListAPIView):
#     queryset = Info.objects.all().prefetch_related('socials')
#     serializer_class = InfoSerializer


class PurchaseCreateAPIView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


# class GaleryListAPIView(generics.ListAPIView):
#     queryset = Galery.objects.all().prefetch_related('photos')
#     serializer_class = GalerySerializer


# class GaleryRetrieveApiView(generics.RetrieveAPIView):
#     queryset = Galery.objects.all()
#     serializer_class = GalerySerializer


# class NearestPlaceListAPIView(generics.ListAPIView):
#     queryset = NearestPlace.objects.all().prefetch_related('photos')
#     serializer_class = NearestPlaceSerializer
