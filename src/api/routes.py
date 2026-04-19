from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from src.schemas.qr_models import QRRequest
from src.core.qr_service import generate_qr_in_memory

router = APIRouter()

@router.post("/generate-qr/")
async def create_qr(request: QRRequest):
    try:
        url_str = str(request.url)
        image_buffer = generate_qr_in_memory(url_str)
        
        return StreamingResponse(image_buffer, media_type="image/png")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno al generar el QR: {str(e)}")