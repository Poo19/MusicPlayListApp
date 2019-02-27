from django.conf.urls import url
from django.contrib import admin
from songs.api.views import SongViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include


router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='songs')
urlpatterns = [
    url(r'^', include(router.urls)),
]