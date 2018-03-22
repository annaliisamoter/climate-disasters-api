import os
import unittest
from server import app
from flask import json, jsonify

class FlaskTests(unittest.TestCase):
    """Testing of app routes, both functional and unittest."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

    def tearDown(self):
        """Do at end of every test."""


    def test_index(self):
        """tests rendering index"""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn('index.html', result.data)

    def test_api_call(self):
        """tests api call route"""
        result = self.client.("/api-call")
        self.


        


if __name__ == '__main__':
    unittest.main()