from pydantic import BaseModel
from typing import Literal

class ClassificationResult(BaseModel):
    category: Literal[
        "DUVIDA",
        "TICKET",
        "HUMANO"
    ]