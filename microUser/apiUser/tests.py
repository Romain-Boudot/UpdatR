from django.test import TestCase
from .tools.getURL import getJSON

class TestGetModelMethod(TestCase):
    def setUp(self):
        self.return_value =  {
            'WRONG': {'error': 'requests'},
            'BAD': {'error': 'json parse'},
            'RIGHT': ['all', 'exist/username/{username}', 'exist/token/{access_token}']
        }
        pass

    def test_wrong_url(self):
        self.assertTrue(getJSON('WRONGURL') == self.return_value['WRONG']) # dans le cas d'une URL incorrect

    def test_bad_url(self):
        self.assertTrue(getJSON('https://www.djangoproject.com/') == self.return_value['BAD']) # dans le cas d'une mauvaise url

    def test__url(self):
        self.assertTrue(getJSON('http://127.0.0.1:3000/api') == self.return_value['RIGHT']) # dans le cas d'une réussite