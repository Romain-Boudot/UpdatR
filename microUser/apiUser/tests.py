from django.test import TestCase
from .tools.getURL import getJSON

class TestGetModelMethod(TestCase):
    def setUp(self):
        # Setup run before every test method.
        # 
        pass

    def test_wrong_url(self):
        return_value = {'error': 'requests'}
        self.assertTrue(getJSON('WRONGURL') == return_value) # dans le cas d'une URL incorrect

    def test_bad_url(self):
        return_value = {'error': 'json parse'}
        self.assertTrue(getJSON('https://www.djangoproject.com/') == return_value) # dans le cas d'une mauvaise url

    def test__url(self):
        return_value = ['all', 'exist/username/{username}', 'exist/token/{access_token}']
        self.assertTrue(getJSON('http://127.0.0.1:3000/api') == return_value) # dans le cas d'une réussite