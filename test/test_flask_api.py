import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"  # Change this if your Flask app runs on a different host/port


class FlaskAPITestCase(unittest.TestCase):
    def test_create_user(self):
        """Test creating a user"""
        payload = {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "created_at": "2024-01-01T10:00:00Z"
        }
        response = requests.post(f"{BASE_URL}/user", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("User created", response.json()["message"])
        self.assertEqual(response.json()["user"], payload)

    def test_get_users(self):
        """Test retrieving all users"""
        response = requests.get(f"{BASE_URL}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_account(self):
        """Test creating an account"""
        payload = {
            "id": 1,
            "user_id": 1,
            "account_type": "savings",
            "balance": 1000.50,
            "created_at": "2024-01-01T10:00:00Z"
        }
        response = requests.post(f"{BASE_URL}/account", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Account created", response.json()["message"])
        self.assertEqual(response.json()["account"], payload)

    def test_get_accounts(self):
        """Test retrieving all accounts"""
        response = requests.get(f"{BASE_URL}/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_transaction(self):
        """Test creating a transaction"""
        payload = {
            "id": 1,
            "account_id": 1,
            "amount": 200.75,
            "transaction_type": "credit",
            "created_at": "2024-01-02T10:00:00Z"
        }
        response = requests.post(f"{BASE_URL}/transaction", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Transaction created", response.json()["message"])
        self.assertEqual(response.json()["transaction"], payload)

    def test_get_transactions(self):
        """Test retrieving all transactions"""
        response = requests.get(f"{BASE_URL}/transactions")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)


if __name__ == "__main__":
    unittest.main()
