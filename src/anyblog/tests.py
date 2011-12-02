"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import anyblog.models as model

class ModelTest(TestCase):
    def setUp(self):
        model.BlogPost(title="Test Title",
                       content="Some test content",
                       author="Joe Bloggs").save()

    def test_creation(self):
        mo = model.BlogPost.objects.all()[0]
        self.assertEqual(mo.title, "Test Title", "Creation test failed. Title property incorrect.")
        self.assertEqual(mo.content, "Some test content", "Creation test failed. Content property incorrect.")
        self.assertEqual(mo.author, "Joe Bloggs", "Creation test failed. Author property incorrect.")