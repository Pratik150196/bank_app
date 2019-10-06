from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from rest_framework_simplejwt import views as jwt_views
from app import views
from django.conf.urls import url
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()

#router.register(r'app/<bank_name>/city/',views.AppView.name_city)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('app-auth',include('rest_framework.urls')),

    path('app/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('app/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


    ]
