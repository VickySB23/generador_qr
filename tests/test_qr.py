from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_generar_qr_exitoso():
    # Simulamos que un usuario envía esta URL en formato JSON
    payload = {"url": "https://github.com"}
    
    # Hacemos una petición POST al endpoint que vamos a crear
    response = client.post("/api/v1/generate-qr/", json=payload)
    
    # Verificamos que la respuesta sea exitosa (200 OK)
    assert response.status_code == 200
    
    # Verificamos que lo que nos devuelve sea efectivamente una imagen PNG
    assert response.headers["content-type"] == "image/png"

def test_generar_qr_url_invalida():
    # Simulamos el envío de texto que no es un enlace válido
    payload = {"url": "esto-no-es-un-link"}
    response = client.post("/api/v1/generate-qr/", json=payload)
    
    # Pydantic debería atrapar el error de validación (422 Unprocessable Entity)
    assert response.status_code == 422