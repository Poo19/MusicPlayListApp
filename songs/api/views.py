from django.db.models import Q
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.decorators import list_route, detail_route

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

from songs.models import Song

from .pagination import SongLimitOffsetPagination, SongPageNumberPagination
#from .permissions import IsOwnerOrReadOnly

from .serializers import (
    SongListSerializer
    )


# class SongDetailSerializer(RetrieveAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongDetailSerializer
#     lookup_field = 'slug'
#     permission_classes = [AllowAny]
   


# class SongListAPIView(ListAPIView):
#     serializer_class = SongListSerializer
#     filter_backends= [SearchFilter, OrderingFilter]
#     permission_classes = [AllowAny]
#     search_fields = ['title', 'artist__name', 'genre__name']
#     pagination_class = SongPageNumberPagination #PageNumberPagination

#     def get_queryset(self, *args, **kwargs):
#         #queryset_list = super(SongListAPIView, self).get_queryset(*args, **kwargs)
#         queryset_list = Song.objects.all() #filter(user=self.request.user)
#         query = self.request.GET.get("q")
#         print (query)
#         if query:
#             queryset_list = queryset_list.filter(
#                     Q(title__icontains=query)|
#                     Q(artist__name__icontains=query)|
#                     Q(artist__name__icontains=query) 
#                     ).distinct()
#         return queryset_list



class SongViewSet(viewsets.ModelViewSet):

    """ Songs List """

    serializer_class = SongListSerializer
    model = Song
    permission_classes = (IsAuthenticated,)
    #permission_classes = (IsAuthenticated, permissions.DjangoModelPermissions, permissions.DjangoObjectPermissions)
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer, renderers.BrowsableAPIRenderer,)
    queryset = Song.objects.all()

    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            context = {}
            return Response(context, template_name='song-list.html')
        response = super(SongViewSet, self).list(request, *args, **kwargs)
        return response

    @list_route(renderer_classes=[renderers.JSONRenderer, renderers.BrowsableAPIRenderer], pagination_class = SongLimitOffsetPagination)
    def songTable(self, request, *args, **kwargs):
        data = dict(request.GET.items())
        print(data)
        search = data.get('search[value]', '')
        orderByColumn = data.get('order[0][column]', '')
        sortOrder = data.get('order[0][dir]', '')
        print(search)
        print(orderByColumn)

        if sortOrder == 'desc':
            sortOrder = '-'
        else:
            sortOrder = ''
        orderBy = data.get('columns['+orderByColumn+'][data]', '')

        if not orderBy:
            orderBy = "title"
        else:
            if orderBy == "title":
                orderBy = sortOrder + "title"
            elif orderBy == "artist":
                orderBy = sortOrder + "artist__name"
            elif orderBy == "genre":
                orderBy = sortOrder + "genre__name"
            elif orderBy == "year":
                orderBy = sortOrder + "date"
            else:
                orderBy = sortOrder + orderBy

        if search:
            songs = Song.objects.filter(Q(title__icontains=search)|Q(artist__name__icontains=search)|Q(artist__name__icontains=search)).order_by(orderBy)
        else:
            songs= Song.objects.all().order_by(orderBy)
        page = self.paginate_queryset(songs)
        serializer = SongListSerializer(page, many = True, context={'request': request})
        print(serializer.data)
        return self.get_paginated_response(serializer.data)

    

