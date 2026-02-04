import re

SCAM_KEYWORDS = [
    "urgent",
    "otp",
    "bank",
    "verify",
    "click",
    "investment",
    "lottery",
    "account",
    "transfer"
]

def detect_scam(message: str) -> dict:
    message = message.lower()
    score = 0

    for word in SCAM_KEYWORDS:
        if word in message:
            score += 1

    if re.search(r"\b\d{10,16}\b", message):  # card/bank numbers
        score += 2

    return {
        "is_scam": score >= 2,
        "risk_score": score
    }

