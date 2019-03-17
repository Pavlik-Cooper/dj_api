from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination


class Pagination(LimitOffsetPagination):
    # page_size = 1
    default_limit = 2
    max_limit = 20
