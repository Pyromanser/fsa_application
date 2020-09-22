import json

from django.core.cache import cache
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AddressToGeocodeTests(APITestCase):
    def setUp(self):
        cache.clear()

    def test_correct_address(self):
        url = reverse('address-to-geocode')
        data = {'address': '1600 Amphitheatre Parkway, Mountain View, CA'}
        expected_response = {"latlng": [37.4218651, -122.0846744], "address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_incorrect_address(self):
        url = reverse('address-to-geocode')
        data = {"address": "this place doesn't exists"}
        expected_response = {"detail": "This address doesn't exists"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_throttling(self):
        url = reverse('address-to-geocode')
        _ = self.client.post(url, {}, format='json')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)


class GeocodeToAddressTests(APITestCase):
    def setUp(self):
        cache.clear()

    def test_correct_geocode(self):
        url = reverse('geocode-to-address')
        data = {"latlng": [37.4218651, -122.0846744]}
        expected_response = {"latlng": [37.4218651, -122.0846744], "address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_incorrect_geocode(self):
        url = reverse('geocode-to-address')
        data = {"latlng": [91, 0]}
        expected_response = {"detail": "Coords are not within the world's geographical boundary"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_throttling(self):
        url = reverse('geocode-to-address')
        _ = self.client.post(url, {}, format='json')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)


class CalcDistanceTests(APITestCase):
    def setUp(self):
        cache.clear()

    def test_simple_correct_coordinates(self):
        url = reverse('calc-distance')
        data = {"coordinates": [{"latlng": [0, 0]}, {"latlng": [0, 0]}]}
        expected_response = {"distance": 0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_correct_coordinates(self):
        url = reverse('calc-distance')
        data = {"coordinates": [{"latlng": [37.4218651, -122.0846744]}, {"latlng": [51.5216889, -0.1260132]}]}
        expected_response = {"distance": 8654.68964661197}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_incorrect_geocode(self):
        url = reverse('calc-distance')
        data = {"coordinates": [{"latlng": [91, 0]}, {"latlng": [-91, 0]}]}
        expected_response = {"detail": "Latitude must be in the [-90; 90] range."}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_throttling(self):
        url = reverse('calc-distance')
        _ = self.client.post(url, {}, format='json')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
