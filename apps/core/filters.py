from rest_framework.filters import OrderingFilter


class SortFilter(OrderingFilter):
    """Maps the FE-friendly `sort=price_asc|price_desc|name_asc|name_desc|default`
    parameter to DRF's standard `ordering` value.
    """

    ordering_param = "sort"

    SORT_MAP = {
        "default": None,
        "price_asc": "price",
        "price_desc": "-price",
        "name_asc": "name",
        "name_desc": "-name",
    }

    def get_ordering(self, request, queryset, view):
        value = request.query_params.get(self.ordering_param)
        if value is None:
            return self.get_default_ordering(view)
        mapped = self.SORT_MAP.get(value)
        if mapped is None:
            return self.get_default_ordering(view)
        return [mapped]
