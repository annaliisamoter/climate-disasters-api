import os
import unittest
from csv_parse import parses_csv
from server import app
from flask import json, jsonify

class FlaskTestcase(unittest.TestCase):
    """Testing of app routes, both functional and unittest."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

    def tearDown(self):
        """Do at end of every test."""
        #no db to tear down in this case

    def test_index(self):
        """tests rendering index"""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        #self.assertIn('Climate Disasters', result.data)

    def test_api_call(self):
        """tests api call route returning proper jason"""
        result = self.client.get("/api-call?begin=2014&end=2014&type-of-disaster=Chemical")
        self.assertEqual(result.status_code, 200)

    def test_csv_parse_funct(self):
        """tests the parses_csv function"""
        result = parses_csv(2014, 2014, 'Chemical')
        self.assertEqual(result, {'West Virginia': 9})



if __name__ == '__main__':
    unittest.main()