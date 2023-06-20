from django.urls import path
from .views import *


urlpatterns = [
    path('objects/', ObjectListAPIView.as_view()),
    path('objects/<int:pk>', ObjectRetrieveApiView.as_view()),
    # path('entertaiments/<int:pk>', EntertaimentRetrieveApiView.as_view()),
    # path('dishes/', DishListAPIView.as_view()),
    # path('feeding-info/', FeedingInfoListAPIView.as_view()),
    # path('entertaiments/', EntertaimentListAPIView.as_view()),
    # path('rules/', RuleListAPIView.as_view()),
    # path('info/', InfoListAPIView.as_view()),
    path('purchases/', PurchaseCreateAPIView.as_view()),
    # path('galeries/', GaleryListAPIView.as_view()),
    # path('galeries/<int:pk>', GaleryRetrieveApiView.as_view()),
    # path('nearests/', NearestPlaceListAPIView.as_view()),
]
