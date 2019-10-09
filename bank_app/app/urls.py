
from django.urls import path,include
from rest_framework import routers
from .views import AppView,HelloView,AppView1
from django.conf.urls import url
urlpatterns = [
url(r"^ifsc/$",AppView.as_view()),#ifsc
url(r"^name_city/$",AppView1.as_view()),#bank name and city
path('hello/',HelloView.as_view(), name='hello'),
]
