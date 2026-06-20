from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

def load_prompt(filename: str) -> str:
    with open(PROMPTS_DIR / filename, encoding="utf-8") as f:
        return f.read()

CLASSIFIER_PROMPT = load_prompt("classifier.md")