from fastapi import FastAPI
from src.api.routes import router as qr_router

app = FastAPI(title="Generador de QR API")

# Registramos las rutas con el prefijo que usamos en el test
app.include_router(qr_router, prefix="/api/v1")