from django.conf.urls import url
from django.contrib import admin

from .views import (
    PlaylistCreateAPIView,
    PlaylistDeleteAPIView,
    PlaylistDetailAPIView,
    PlaylistListAPIView,
    PlaylistUpdateAPIView,
    )

urlpatterns = [
    url(r'^$', PlaylistListAPIView.as_view(), name='list'),
    url(r'^create/$', PlaylistCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PlaylistDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PlaylistUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PlaylistDeleteAPIView.as_view(), name='delete'),
]
