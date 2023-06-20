from rest_framework import generics

from .models import *
from .serializers import *


class InfoListAPIView(generics.ListAPIView):
    queryset = Info.objects.all().prefetch_related('socials')
    serializer_class = InfoSerializer
    

class DishListAPIView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class FeedingInfoListAPIView(generics.ListAPIView):
    queryset = FeedingInfo.objects.all()
    serializer_class = FeedingInfoSerializer


class RuleListAPIView(generics.ListAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
