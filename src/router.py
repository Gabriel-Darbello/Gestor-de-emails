from src.services.classify_email import classify_email
from src.models.email import Email
from src.models.classification_result import ClassificationResult

def route_email(email: Email):
    result: ClassificationResult = classify_email(email)
    category = result.category

    if category == "DUVIDA":
        # resposta automática com RAG
        pass
    elif category == "TICKET":
        # abrir ticket
        pass
    elif category == "HUMANO":
        # escalar para humano
        pass
    else:
        raise ValueError(f"Categoria inválida: {category}")
