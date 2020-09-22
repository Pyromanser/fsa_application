from drf_yasg import openapi

bad_request_response = openapi.Response("Bad request", openapi.Schema(
    title="ErrorMessage",
    type=openapi.TYPE_OBJECT,
    properties={
        "non_field_errors": openapi.Schema(
            type=openapi.TYPE_ARRAY, items=openapi.Schema(
                type=openapi.TYPE_STRING,
            ),
        ),
        "field_name": openapi.Schema(
            type=openapi.TYPE_ARRAY, items=openapi.Schema(
                type=openapi.TYPE_STRING,
            ),
        ),
    },
    example={
        "non_field_errors": ["Some non filed error.", "Extra error."],
        "field_name": ["This field is required.", "Extra error."],
    },
))

too_many_requests_response = openapi.Response("Too Many Requests", openapi.Schema(
    title="ErrorMessage",
    type=openapi.TYPE_OBJECT,
    properties={
        "detail": openapi.Schema(type=openapi.TYPE_STRING),
    },
    example={
        "detail": "Request was throttled. Expected available in 1 second.",
    },
))
