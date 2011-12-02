"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import anyblog.models as model

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ModelTest(TestCase):
    def test_creation(self):
        model = model.BlogPost(title="Test Title",
                               content="Some test content",
                               author="Joe Bloggs")
        model.put()
        self.assertEqual(model.title, "Test Title", "Creation test failed. Title property incorrect.")
        self.assertEqual(model.content, "Some test content", "Creation test failed. Content property incorrect.")
        self.assertEqual(model.author, "Joe Bloggs", "Creation test failed. Author property incorrect.")