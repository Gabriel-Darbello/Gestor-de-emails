from pydantic import BaseModel
from typing import Literal

class ClassifierResult(BaseModel):
    category: Literal[
        "DUVIDA",
        "BUG",
        "HUMANO"
    ]