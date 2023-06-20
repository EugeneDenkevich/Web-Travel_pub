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


class PurchaseCreateAPIView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
