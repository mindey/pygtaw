import unittest
import os
import pygtaw


class TestPyGoogleTranslateAPIWrapper(unittest.TestCase):

    def setUp(self):
        self.make_client()

    def make_client(self):
        self.client = pygtaw.Client(os.environ['TRANSLATE_KEY'])

    def test_get_translated_text(self):
        query = self.client.translate('Hola', 'English')
        self.assertEqual(query.translated_text, 'Hello')

    def test_get_detected_source_lang(self):
        query = self.client.translate('Hello', 'German')
        self.assertEqual(query.detected_source_language, 'English')

    def test_get_translated_text_non_standard_ascii(self):
        query = self.client.translate('World', 'Korean')
        self.assertEqual(query.translated_text, u'\uc138\uacc4')

    def test_try_get_detected_source_lang(self):
        query = self.client.translate('El mundo', target='English', source='Spanish')
        self.assertEqual(query.detected_source_language,
            'No detected source language, source provided by user: Spanish')        

    def test_invalid_language(self):
        self.assertRaises(Exception, self.client.translate, 'Invalid', 'Klingon')

    def tearDown(self):
        self.make_client()

    def test_incorrect_key(self):
        self.client = pygtaw.Client('foo')
        self.assertRaises(Exception, self.client.translate, 'Attempt', 'Spanish')
