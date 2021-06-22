from rest_framework import filters


class LimitFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        limit = request.query_params.get('limit')
        if limit is not None and limit.isnumeric():
            return queryset[:int(limit)]

        return queryset
