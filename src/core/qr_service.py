import qrcode
from io import BytesIO

def generate_qr_in_memory(url_data: str) -> BytesIO:
    # Configuramos el formato del QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_data)
    qr.make(fit=True)

    # Creamos la imagen
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardamos en un buffer de memoria
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0) # Rebobinamos el buffer para que FastAPI lo pueda leer desde el principio
    
    return buffer