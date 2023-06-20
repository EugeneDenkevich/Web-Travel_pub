from django.urls import path
from .views import *


urlpatterns = [
    path('entertainments/', EntertainmentListAPIView.as_view()),
    path('entertainments/<int:pk>', EntertainmentRetrieveApiView.as_view()),
    path('nearests/', NearestPlaceListAPIView.as_view()),
    path('galeries/', GaleryListAPIView.as_view()),
    path('galeries/<int:pk>', GaleryRetrieveApiView.as_view()),
]
