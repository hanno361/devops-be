from rest_framework import status
from rest_framework.response import Response


class EnvelopeRetrieveMixin:
    """Wraps a single-object GET response in `{"data": ...}`."""

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"data": serializer.data})


class EnvelopeCreateMixin:
    """Wraps a CREATE response in `{"data": ...}` (default: 201)."""

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
