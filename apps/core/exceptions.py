from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_default_handler


def _code_from_exception(exc) -> str:
    if isinstance(exc, APIException):
        default = getattr(exc, "default_code", None) or "error"
        return str(default)
    return exc.__class__.__name__.lower().replace("error", "_error") or "error"


def envelope_exception_handler(exc, context):
    """Wrap DRF errors in `{"error": {"code", "message", "details"?}}`."""

    response = drf_default_handler(exc, context)
    if response is None:
        return None

    data = response.data
    code = _code_from_exception(exc)
    message = "An error occurred."
    details = None

    if isinstance(data, dict):
        if "detail" in data and len(data) == 1:
            message = str(data["detail"])
        else:
            details = {
                key: value if isinstance(value, list) else [str(value)]
                for key, value in data.items()
            }
            message = "Validation failed."
    elif isinstance(data, list):
        message = ", ".join(str(item) for item in data) or message

    body = {"error": {"code": code, "message": message}}
    if details:
        body["error"]["details"] = details

    return Response(body, status=response.status_code, headers=response.headers)


def status_code_for_validation():
    return status.HTTP_400_BAD_REQUEST
