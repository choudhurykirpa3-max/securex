sessions = {}

def save_message(session_id, role, message):
    if session_id not in sessions:
        sessions[session_id] = []
    sessions[session_id].append({
        "role": role,
        "message": message
    })

def get_session(session_id):
    return sessions.get(session_id, [])

