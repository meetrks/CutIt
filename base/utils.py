from rest_framework.pagination import PageNumberPagination


def pagination(queryset, request, page_size=10, pagination_class=PageNumberPagination()):
    paginator = pagination_class
    paginator.page_size = page_size
    result = paginator.paginate_queryset(queryset, request)
    return paginator, result
