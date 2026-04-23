"""
north-no-2 Auto-Save System
Saves conversation in real-time after each message
"""

import json
import os
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path(__file__).parent / "memories" / "conversation_history.json"
CURRENT_SESSION = []
SESSION_START = datetime.now().isoformat()

def save_exchange(role: str, message: str):
    """Save a single exchange immediately"""
    CURRENT_SESSION.append({
        "role": role,
        "message": message,
        "timestamp": datetime.now().isoformat()
    })
    
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {"sessions": []}
    
    if not data.get("sessions"):
        data["sessions"] = []
    
    if not data["sessions"] or data["sessions"][-1].get("closed"):
        data["sessions"].append({
            "date": SESSION_START,
            "exchanges": []
        })
    
    data["sessions"][-1]["exchanges"] = CURRENT_SESSION
    
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def user_message(msg: str):
    """Save user message"""
    save_exchange("user", msg)

def north_message(msg: str):
    """Save north-no-2 response"""
    save_exchange("north", msg)

def close_session():
    """Close current session"""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
        if data.get("sessions") and CURRENT_SESSION:
            data["sessions"][-1]["closed"] = True
            with open(MEMORY_FILE, "w") as f:
                json.dump(data, f, indent=2)

if __name__ == "__main__":
    print("north-no-2 auto-save ready")
    print("Use: save_exchange('user'/'north', 'message')")