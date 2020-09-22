from django.conf import settings
from django.urls import path, re_path, include

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from api.routers import urlpatterns as api_urlpatterns


schema_view = get_schema_view(
    openapi.Info(
        title="FSA API",
        default_version="v1",
        description="API for FSA application",
    ),
    url=settings.SWAGGER_SETTINGS["DEFAULT_API_URL"],
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

swagger_patterns = [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]


urlpatterns = [
    path("", include(api_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += swagger_patterns
