from flask import Flask, request, jsonify
from auth import validate_api_key
from intelligence import detect_scam
from honeypot import fake_human_response
from memory import save_message
from logger import log_event

app = Flask(__name__)

@app.route("/message", methods=["POST"])
def incoming_message():

    # STEP 1: API KEY VALIDATION
    if not validate_api_key(request):
        return jsonify({"error": "Invalid API key"}), 401

    data = request.get_json()
    session_id = data.get("session_id")
    message = data.get("message")

    if not session_id or not message:
        return jsonify({"error": "session_id and message required"}), 400

    # Save incoming message
    save_message(session_id, "attacker", message)

    # STEP 2: SCAM PROBABILITY DETECTION
    analysis = detect_scam(message)

    # STEP 3: LOG EVIDENCE
    log_event(session_id, message, analysis["risk_score"])

    # STEP 4: DECISION
    if analysis["is_scam"]:
        # Honeypot Mode
        reply = fake_human_response()
    else:
        # Normal Response
        reply = "Okay, noted."

    # Save reply
    save_message(session_id, "system", reply)

    return jsonify({
        "reply": reply,
        "is_scam": analysis["is_scam"],
        "risk_score": analysis["risk_score"]
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
