#!/usr/bin/python3
"""
testcases for city class
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def tearDown(self):
        self.city = None

    def test_attributes_initializatiom(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_str_method(self):
        city_str = str(self.city)
        self.assertIn("[City]", city_str)
        self.assertIn("id", city_str)
        self.assertIn("created_at", city_str)
        self.assertIn("updated_at", city_str)

    def test_save_method(self):
        current_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

if __name__ == "__main__":
    unittest.main()





