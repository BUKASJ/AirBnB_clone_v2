#!/usr/bin/python3
import unittest
from models.state import State
from models.city import City
from models.base_model import BaseModel
from unittest.mock import patch


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes(self):
        """Test State attributes"""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertIsInstance(self.state.name, str)

    def test_table_name(self):
        """Test State table name"""
        self.assertEqual(State.__tablename__, 'states')

    def test_name_column(self):
        """Test State name column"""
        name_column = State.__table__.columns['name']
        self.assertEqual(name_column.type.length, 128)
        self.assertFalse(name_column.nullable)

    @patch('models.storage')
    def test_cities_property(self, mock_storage):
        """Test State cities property"""
        state = State()
        state.id = 'test_state_id'
        city1 = City()
        city1.state_id = 'test_state_id'
        city2 = City()
        city2.state_id = 'different_state_id'
        mock_storage.all.return_value = {'city1_id': city1, 'city2_id': city2}

        cities = state.cities
        self.assertEqual(len(cities), 1)
        self.assertEqual(cities[0], city1)


if __name__ == '__main__':
    unittest.main()
