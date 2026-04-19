from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_generar_qr_exitoso():
    payload = {"url": "https://github.com"}
    response = client.post("/api/v1/generate-qr/", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

def test_generar_qr_url_invalida():
    payload = {"url": "esto-no-es-un-link"}
    response = client.post("/api/v1/generate-qr/", json=payload)
    assert response.status_code == 422