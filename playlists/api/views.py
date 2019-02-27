from rest_framework import viewsets
from django.db.models import Q
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )


from playlists.models import Playlist
from .serializers import PlayListSerializer,PlayListCreateUpdateSerializer
from .pagination import PlayListLimitOffsetPagination, PlayListPageNumberPagination
from .permissions import IsOwnerOrReadOnly


class PlaylistCreateAPIView(CreateAPIView):
    queryset = Playlist.objects.filter(deleted = False)
    serializer_class = PlayListCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlaylistDetailAPIView(RetrieveAPIView):
    queryset = Playlist.objects.filter(deleted = False)
    serializer_class = PlayListSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]



class PlaylistUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Playlist.objects.filter(deleted = False)
    serializer_class = PlayListCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        

class PlaylistDeleteAPIView(DestroyAPIView):
    queryset = Playlist.objects.filter(deleted = False)
    serializer_class = PlayListSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]



class PlaylistListAPIView(ListAPIView):
    serializer_class = PlayListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title', 'content', 'user__first_name','user__last_name__icontains']
    pagination_class = Playlist.objects.filter(deleted = False) 

    def get_queryset(self, *args, **kwargs):
        queryset_list = Playlist.objects.filter(deleted = False,user=self.request.user) 
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(access=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list














