from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class EnvelopePagination(PageNumberPagination):
    """List response envelope expected by the frontend.

    Returns:
        {
          "data": [...],
          "meta": {"page": int, "pageSize": int, "totalItems": int, "totalPages": int}
        }
    """

    page_query_param = "page"
    page_size_query_param = "pageSize"
    page_size = 12
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("data", data),
                    (
                        "meta",
                        OrderedDict(
                            [
                                ("page", self.page.number),
                                ("pageSize", self.get_page_size(self.request)),
                                ("totalItems", self.page.paginator.count),
                                ("totalPages", self.page.paginator.num_pages),
                            ]
                        ),
                    ),
                ]
            )
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "data": schema,
                "meta": {
                    "type": "object",
                    "properties": {
                        "page": {"type": "integer"},
                        "pageSize": {"type": "integer"},
                        "totalItems": {"type": "integer"},
                        "totalPages": {"type": "integer"},
                    },
                },
            },
        }
