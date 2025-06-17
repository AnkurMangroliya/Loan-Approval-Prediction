import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict_route(self):
        sample_data = {
            'Gender': 'Male',
            'Married': 'Yes',
            'Dependents': '0',
            'Education': 'Graduate',
            'Self_Employed': 'No',
            'ApplicantIncome': '5000',
            'CoapplicantIncome': '2000',
            'LoanAmount': '100',
            'Loan_Amount_Term': '360',
            'Credit_History': '1',
            'Property_Area': 'Urban'
        }
        response = self.app.post('/predict', data=sample_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main() 