#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class TestUser(unittest.TestCase):
    def test_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_table_name(self):
        """Test User table name"""
        self.assertEqual(User.__tablename__, 'users')

    def test_email_column(self):
        """Test User email column"""
        email_column = User.__table__.columns['email']
        self.assertEqual(email_column.type.length, 128)
        self.assertFalse(email_column.nullable)

    def test_password_column(self):
        """Test User password column"""
        password_column = User.__table__.columns['password']
        self.assertEqual(password_column.type.length, 128)
        self.assertFalse(password_column.nullable)

    def test_first_name_column(self):
        """Test User first_name column"""
        first_name_column = User.__table__.columns['first_name']
        self.assertEqual(first_name_column.type.length, 128)
        self.assertTrue(first_name_column.nullable)

    def test_last_name_column(self):
        """Test User last_name column"""
        last_name_column = User.__table__.columns['last_name']
        self.assertEqual(last_name_column.type.length, 128)
        self.assertTrue(last_name_column.nullable)


if __name__ == '__main__':
    unittest.main()
