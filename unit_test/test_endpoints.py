import requests

# Set the base URL for your deployed FastAPI application
base_url = "http://localhost:8000"  # Replace with the actual URL of your deployed API

# Define sample payload for the predict endpoint
predict_payload = {"text": "This is a test sentence."}

# Test the health check endpoint
def test_health_check():
    response = requests.get(f"{base_url}/")
    assert response.status_code == 200
    data = response.json()
    assert data["health_check"] == "OK"
    print("Health check passed.")

# Test the predict endpoint
def test_predict():
    response = requests.post(f"{base_url}/predict", json=predict_payload)
    assert response.status_code == 200
    data = response.json()
    assert "language" in data
    print("Predict endpoint test passed.")

def test_ml_model():
    response = requests.post(f"{base_url}/predict", json=predict_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["language"] == "English"
    print("ML endpoint test passed.")

if __name__ == "__main__":
    # Run the tests
    test_health_check()
    test_predict()
    test_ml_model()
