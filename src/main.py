from fastapi import FastAPI
from src.api.routes import router as qr_router

app = FastAPI(title="Generador de QR API")
app.include_router(qr_router, prefix="/api/v1")