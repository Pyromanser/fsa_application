import geocoder
from drf_yasg import openapi
from geopy.distance import geodesic

from django.template.loader import render_to_string

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from api.serializers import GEOReadOnlySerializer, AddressSerializer, LatLngSerializer, CoordinatesSerializer
from api.throttles import DefaultRateThrottle, DefaultScopedRateThrottle

from utils.views import bad_request_response, too_many_requests_response


class AddressToGeocodeView(GenericAPIView):
    serializer_class = AddressSerializer
    throttle_classes = [DefaultRateThrottle, DefaultScopedRateThrottle, ]

    @swagger_auto_schema(
        operation_description=render_to_string("api/base.html", context={
            "description": "Converts address to geocode with google API",
            "body_fields": [
                ("address", "address, for example <code>1600 Amphitheatre Parkway, Mountain View, CA</code>")
            ],
            "path_example": ["api", "geo", "address-to-geocode", ],
        }),
        operation_summary="Converts address to geocode",
        responses={
            status.HTTP_200_OK: GEOReadOnlySerializer,
            status.HTTP_400_BAD_REQUEST: bad_request_response,
            status.HTTP_429_TOO_MANY_REQUESTS: too_many_requests_response,
        },
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            geo = geocoder.google(serializer.data["address"])
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if not geo.latlng:
            return Response({"detail": "This address doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {
                "latlng": geo.latlng,
                "address": geo.address,
            },
            status=status.HTTP_200_OK,
        )


class GeocodeToAddressView(GenericAPIView):
    serializer_class = LatLngSerializer
    throttle_classes = [DefaultRateThrottle, DefaultScopedRateThrottle, ]

    @swagger_auto_schema(
        operation_description=render_to_string("api/base.html", context={
            "description": "Converts geocode to address with google API",
            "body_fields": [
                ("latlng", "list of latitude and longitude, for example <code>[37.4218651, -122.0846744]</code>")
            ],
            "path_example": ["api", "geo", "geocode-to-address", ],
        }),
        operation_summary="Converts geocode to address",
        responses={
            status.HTTP_200_OK: GEOReadOnlySerializer,
            status.HTTP_400_BAD_REQUEST: bad_request_response,
            status.HTTP_429_TOO_MANY_REQUESTS: too_many_requests_response,
        },
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            geo = geocoder.google(serializer.data["latlng"], method='reverse')
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if not geo.address:
            return Response({"detail": "This address doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {
                "latlng": geo.latlng,
                "address": geo.address,
            },
            status=status.HTTP_200_OK,
        )


class CalcDistanceView(GenericAPIView):
    serializer_class = CoordinatesSerializer
    throttle_classes = [DefaultRateThrottle, DefaultScopedRateThrottle, ]

    @swagger_auto_schema(
        operation_description=render_to_string("api/base.html", context={
            "description": "Calculating distance",
            "body_fields": [
                ("coordinates", "list of two points with latlng"),
                ("coordinates[latlng]", "list of latitude and longitude, for example <code>[37.4218651, -122.0846744]</code>")
            ],
            "path_example": ["api", "geo", "calc-distance", ],
        }),
        operation_summary="Calculating distance",
        responses={
            status.HTTP_200_OK: openapi.Schema(
                title="Distance",
                type=openapi.TYPE_OBJECT,
                properties={
                    "distance": openapi.Schema(
                        type=openapi.TYPE_NUMBER, title="distance",
                    )
                },
                example={
                    "distance": 0,
                },
            ),
            status.HTTP_400_BAD_REQUEST: bad_request_response,
            status.HTTP_429_TOO_MANY_REQUESTS: too_many_requests_response,
        },
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            distance = geodesic(*(i["latlng"] for i in serializer.data["coordinates"])).km
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {
                "distance": distance,
            },
            status=status.HTTP_200_OK
        )
