# django-yasg
SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "api_key": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization"
        }
    },
    "DEFAULT_API_URL": None,
}

# drf
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    # "DEFAULT_PERMISSION_CLASSES": (
    #     "rest_framework.permissions.IsAuthenticated",
    # ),
    "PAGINATE_BY": 10,
    "PAGINATE_BY_PARAM": "page_size",
    "MAX_PAGINATE_BY": 100,
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
    ),
    "DEFAULT_METADATA_CLASS": "rest_framework.metadata.SimpleMetadata",
    "DEFAULT_THROTTLE_RATES": {
        "default_throttle": "1/second",
        "default_scoped_throttle": "10/second",
    },
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
}
