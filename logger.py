from datetime import datetime

def log_event(session_id, message, risk_score):
    with open("honeypot_logs.txt", "a") as f:
        f.write(
            f"{datetime.now()} | Session:{session_id} | Risk:{risk_score} | {message}\n"
        )

