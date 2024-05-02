#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        """Test Place inheritance"""
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

    def test_attributes(self):
        """Test Place attributes"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'reviews'))
        self.assertTrue(hasattr(place, 'amenities'))

    def test_table_name(self):
        """Test Place table name"""
        self.assertEqual(Place.__tablename__, 'places')

    def test_city_id_column(self):
        """Test Place city_id column"""
        city_id_column = Place.__table__.columns['city_id']
        self.assertEqual(city_id_column.type.length, 60)
        self.assertFalse(city_id_column.nullable)

    def test_user_id_column(self):
        """Test Place user_id column"""
        user_id_column = Place.__table__.columns['user_id']
        self.assertEqual(user_id_column.type.length, 60)
        self.assertFalse(user_id_column.nullable)

    def test_name_column(self):
        """Test Place name column"""
        name_column = Place.__table__.columns['name']
        self.assertEqual(name_column.type.length, 128)
        self.assertFalse(name_column.nullable)

    def test_description_column(self):
        """Test Place description column"""
        description_column = Place.__table__.columns['description']
        self.assertEqual(description_column.type.length, 1024)
        self.assertTrue(description_column.nullable)

    def test_number_rooms_column(self):
        """Test Place number_rooms column"""
        number_rooms_column = Place.__table__.columns['number_rooms']
        self.assertIsInstance(number_rooms_column.type, Integer)
        self.assertFalse(number_rooms_column.nullable)

    def test_number_bathrooms_column(self):
        """Test Place number_bathrooms column"""
        number_bathrooms_column = Place.__table__.columns['number_bathrooms']
        self.assertIsInstance(number_bathrooms_column.type, Integer)
        self.assertFalse(number_bathrooms_column.nullable)

    def test_max_guest_column(self):
        """Test Place max_guest column"""
        max_guest_column = Place.__table__.columns['max_guest']
        self.assertIsInstance(max_guest_column.type, Integer)
        self.assertFalse(max_guest_column.nullable)

    def test_price_by_night_column(self):
        """Test Place price_by_night column"""
        price_by_night_column = Place.__table__.columns['price_by_night']
        self.assertIsInstance(price_by_night_column.type, Integer)
        self.assertFalse(price_by_night_column.nullable)

    def test_latitude_column(self):
        """Test Place latitude column"""
        latitude_column = Place.__table__.columns['latitude']
        self.assertIsInstance(latitude_column.type, Float)
        self.assertTrue(latitude_column.nullable)

    def test_longitude_column(self):
        """Test Place longitude column"""
        longitude_column = Place.__table__.columns['longitude']
        self.assertIsInstance(longitude_column.type, Float)
        self.assertTrue(longitude_column.nullable)


if __name__ == '__main__':
    unittest.main()
