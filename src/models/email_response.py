from pydantic import BaseModel

class EmailResponse(BaseModel):
    subject: str
    sender: str
    body: str