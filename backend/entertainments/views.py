from rest_framework import generics

from .models import *
from .serializers import *


class EntertainmentListAPIView(generics.ListAPIView):
    queryset = Entertainment.objects.all().prefetch_related('prices', 'photos')
    serializer_class = EntertainmentSerializer


class EntertainmentRetrieveApiView(generics.RetrieveAPIView):
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer


class NearestPlaceListAPIView(generics.ListAPIView):
    queryset = NearestPlace.objects.all().prefetch_related('photos')
    serializer_class = NearestPlaceSerializer


class GaleryListAPIView(generics.ListAPIView):
    queryset = Galery.objects.all().prefetch_related('photos')
    serializer_class = GalerySerializer


class GaleryRetrieveApiView(generics.RetrieveAPIView):
    queryset = Galery.objects.all()
    serializer_class = GalerySerializer