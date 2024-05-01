#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
from sqlalchemy import Column, String, DateTime


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        """Test BaseModel attributes"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save(self):
        """Test BaseModel save method"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test BaseModel to_dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_delete(self):
        """Test BaseModel delete method"""
        base_model = BaseModel()
        base_model.save()
        base_model.delete()
        self.assertIsNone(storage.get(BaseModel, base_model.id))


if __name__ == '__main__':
    unittest.main()
