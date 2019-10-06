
from django.urls import path,include
from rest_framework import routers
from .views import AppView,HelloView,AppView1
urlpatterns = [
path("ifsc/<ifsc>/",AppView.as_view()),#ifsc
path("name_city/<bank_name>/<city>/",AppView1.as_view()),#bank name and city
path('hello/',HelloView.as_view(), name='hello'),
]
