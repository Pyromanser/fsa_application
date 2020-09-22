from rest_framework import serializers


class GEOReadOnlySerializer(serializers.Serializer):
    address = serializers.CharField(read_only=True)
    latlng = serializers.ListField(child=serializers.FloatField(), min_length=2, max_length=2, read_only=True)


class AddressSerializer(serializers.Serializer):
    address = serializers.CharField(required=True)
    latlng = serializers.ListField(child=serializers.FloatField(), min_length=2, max_length=2, read_only=True)


class LatLngSerializer(serializers.Serializer):
    address = serializers.CharField(read_only=True)
    latlng = serializers.ListField(child=serializers.FloatField(), min_length=2, max_length=2, required=True)


class CoordinatesSerializer(serializers.Serializer):
    coordinates = serializers.ListField(child=LatLngSerializer(), min_length=2, max_length=2, required=True)
