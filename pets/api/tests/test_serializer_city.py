from django.test import TestCase

from cities.models import City
from api.serializers import CitySerializer


class CitySerializerTestCase(TestCase):
    def test_assert_correct_fields(self):
        """
        The serializer should include only the name and search_name fields
        """
        araras = City(name='Araras', search_name='araras')
        serializer_data = CitySerializer(araras).data

        self.assertEqual(2, len(serializer_data))
        self.assertEqual('Araras', serializer_data['name'])
        self.assertEqual('araras', serializer_data['search_name'])
