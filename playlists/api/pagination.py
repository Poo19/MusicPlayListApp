from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )
from rest_framework.response import Response


class PlayListLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'length'
    offset_query_param = 'start'
    default_limit = 10
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'recordsFiltered': self.count,
            'recordsTotal': self.count,
            'results': data
    })


class PlayListPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    