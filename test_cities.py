import unittest
from city_functions import make_city_country_string

class CityCountryStringTestCase(unittest.TestCase):
    """ Tests for city_functions.py """
    
    def test_city_country(self):
        """ Do inputs like driel netherlands work? """
        test_string = make_city_country_string('driel', 'netherlands')
        self.assertEqual(test_string, 'Driel, Netherlands')

    def test_city_country_population(self):
        "Do inputs like driel netherlands 4375 work?"
        test_string = make_city_country_string('driel', 'netherlands', 4375)
        self.assertEqual(test_string, 'Driel, Netherlands - Population: 4375')

unittest.main()