import unittest
import json
from app import app

class TestCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'num1': 5, 'num2': 3, 'operator': 'add'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 8)

    def test_subtraction(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'num1': 10, 'num2': 4, 'operator': 'subtract'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 6)

    def test_multiplication(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'num1': 6, 'num2': 7, 'operator': 'multiply'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 42)

    def test_division(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'num1': 20, 'num2': 5, 'operator': 'divide'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 4)

    def test_division_by_zero(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'num1': 10, 'num2': 0, 'operator': 'divide'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Cannot divide by zero')

    def test_invalid_operator(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'num1': 5, 'num2': 3, 'operator': 'invalid'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Invalid operator')

if __name__ == '__main__':
    unittest.main()
