from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from django.contrib import admin
from django.urls import path, include

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [

] + router.urls
