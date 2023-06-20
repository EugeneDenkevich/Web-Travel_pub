from django.urls import path
from .views import *


urlpatterns = [
    path('info/', InfoListAPIView.as_view()),
    path('dishes/', DishListAPIView.as_view()),
    path('feeding-info/', FeedingInfoListAPIView.as_view()),
    path('rules/', RuleListAPIView.as_view()),
]
