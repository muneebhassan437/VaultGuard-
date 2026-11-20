from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_returns_true_or_false():
    transaction = {
        "amount": 1000,
        "dest_prev_amount_sum": 50000,
        "dest_prev_txn_count": 5,
        "dest_txn_count_24h": 2,
        "type": "TRANSFER",
        "is_night": 0,
        "dest_is_first_txn": 0,
        "amount_1M_to_10M": 0,
        "amount_is_10M": 0
    }
    response = client.post("/predict", json=transaction)
    assert response.status_code == 200
    assert response.json()["is_fraud"] in [True, False]
