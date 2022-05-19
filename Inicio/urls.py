from django.db import router
from .views import  homepage
from rest_framework import routers, urlpatterns, views
from django.urls import path, include
from .views import homepage
router = routers.DefaultRouter()


urlpatterns = [
    path('', homepage),
]