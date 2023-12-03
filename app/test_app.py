import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        payload = {"text": "example text"}
        response = self.client.post("/predict", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"language", response.content)
        data = response.json()
        self.assertIn("language", data)
        self.assertIsInstance(data["language"], str)

if __name__ == "__main__":
    unittest.main()
