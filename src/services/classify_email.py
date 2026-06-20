from ollama import chat
from src.utils.prompts_loader import  CLASSIFIER_PROMPT
from src.models.classification_result import ClassificationResult
from src.models.email import Email


def classify_email(email: Email) -> ClassificationResult:
    messages = [
        {
            "role": "system",
            "content": CLASSIFIER_PROMPT
        },
        {
            "role": "user",
            "content": f"""
Sender: {email.sender}
Subject: {email.subject}
Body: {email.body}
    """
        }
    ]

    response = chat(
        model="qwen2.5:3b",
        messages=messages,
        format=ClassificationResult.model_json_schema()
    )

    return ClassificationResult.model_validate_json(
        response["message"]["content"]
    )