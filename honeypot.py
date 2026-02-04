import random
import time

RESPONSES = [
    "Sorry, I don’t understand. Can you explain?",
    "Which bank is this regarding?",
    "I’m outside right now, message later?",
    "Is this really required?",
    "I already shared details earlier."
]

def fake_human_response():
    time.sleep(random.randint(1, 3))  # human delay
    return random.choice(RESPONSES)

from flask import Flask

# Assuming your app instance is named 'app'
# If it has a different name, replace 'app' with that name

@app.route("/")
def home():
    return "<h1>Welcome to the Honeypot Application!</h1>"
