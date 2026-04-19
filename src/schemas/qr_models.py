from pydantic import BaseModel, HttpUrl

class QRRequest(BaseModel):
    url: HttpUrl