import unittest

from ch11_1 import cityAndCountry

class CityAndCountryTestCase(unittest.TestCase):
	""" Tests for 'ch11_1.py' """

	def test_city_country(self):
		result = cityAndCountry("paris", "france")

		self.assertEqual(result, "Paris, France")
	
	def test_city_country_population(self):
		result = cityAndCountry("santiago", "chile", population=5000000)
		
		self.assertEqual(result, "Santiago, Chile - population 5000000")

unittest.main()

		
