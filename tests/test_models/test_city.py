#!/usr/bin/python3

import unittest
from models.city import City
from models.state import State
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_table_name(self):
        """Test City table name"""
        self.assertEqual(City.__tablename__, 'cities')

    def test_name_column(self):
        """Test City name column"""
        name_column = City.__table__.columns['name']
        self.assertEqual(name_column.type.length, 128)
        self.assertFalse(name_column.nullable)

    def test_state_id_column(self):
        """Test City state_id column"""
        state_id_column = City.__table__.columns['state_id']
        self.assertEqual(state_id_column.type.length, 60)
        self.assertFalse(state_id_column.nullable)
        self.assertEqual(state_id_column.foreign_keys, {State.__table__.c.id})


if __name__ == '__main__':
    unittest.main()
