from django.urls import path

from api.views import AddressToGeocodeView, GeocodeToAddressView, CalcDistanceView

urlpatterns = [
    path("geo/address-to-geocode/", AddressToGeocodeView.as_view(), name="address-to-geocode"),
    path("geo/geocode-to-address/", GeocodeToAddressView.as_view(), name="geocode-to-address"),
    path("geo/calc-distance/", CalcDistanceView.as_view(), name="calc-distance"),
]
