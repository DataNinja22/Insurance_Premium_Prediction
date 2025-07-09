import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.api.main import app

client = TestClient(app)

def test_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Insurance Premium Prediction API" in response.json()["message"]

def test_health():
    """Test the health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "OK"
    assert "version" in data
    assert "model_loaded" in data

def test_predict_endpoint():
    """Test the prediction endpoint"""
    test_data = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.0,
        "smoker": False,
        "city": "Pune",
        "occupation": "private_job"
    }
    
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "predicted_category" in data["response"]
    assert "confidence" in data["response"]
    assert "class_probabilities" in data["response"]

def test_predict_invalid_data():
    """Test prediction with invalid data"""
    test_data = {
        "age": -5,  # Invalid age
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.0,
        "smoker": False,
        "city": "Pune",
        "occupation": "private_job"
    }
    
    response = client.post("/predict", json=test_data)
    assert response.status_code == 422  # Validation error
