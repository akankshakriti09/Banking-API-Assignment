from rest_framework.pagination import LimitOffsetPagination

class BankListPagination(LimitOffsetPagination):
    default_limit = 10  # To set the number of records per page
    limit_query_param = 'mylimit'  # To set the limit_query_param to any word, default = limit
    offset_query_param = 'myoffset'  # To set the offset_query_param to any word, default = offset
    max_limit = 15  # To limit the number of records per page

class BankPagination(LimitOffsetPagination):
    default_limit = 1  # To set the number of records per page
    limit_query_param = 'mylimit'  # To set the limit_query_param to any word, default = limit
    offset_query_param = 'myoffset'  # To set the offset_query_param to any word, default = offset
    max_limit = 1  # To limit the number of records per page

class BranchPagination(LimitOffsetPagination):
    default_limit = 5  # To set the number of records per page
    limit_query_param = 'mylimit'  # To set the limit_query_param to any word, default = limit
    offset_query_param = 'myoffset'  # To set the offset_query_param to any word, default = offset
    max_limit = 6  # To limit the number of records per page