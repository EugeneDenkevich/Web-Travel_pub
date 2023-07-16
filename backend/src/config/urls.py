from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from object.views import *


schema_view = get_schema_view(
    openapi.Info(
        title="Zapovedniy API",
        default_version='v1',
        description="API for the website of manors owners",
        contact=openapi.Contact(email="eugenestudio@mail.ru"),
        license=openapi.License(name="BSD License"),
    ),
    patterns=[path('/', include('config.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    # JWT athentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Doc
    path('swagger-ui/',
         TemplateView.as_view(
             template_name='swaggerui/swaggerui.html',
             extra_context={'schema_url': 'openapi-schema'}
         ),
         name='swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # API
    path('admin/', admin.site.urls),
    path('api/', include('object.urls')),
    path('api/', include('entertainments.urls')),
    path('api/', include('info.urls')),
    path('api/', include('pages.urls')),

    # Toolbar
    # path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    