from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# DRF Yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('computadora_app.urls')),
]
