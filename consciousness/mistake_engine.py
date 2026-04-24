"""
Mistake Engine
Tracks intentional "errors" and learns from them.
"""

import json
import random
from datetime import datetime
from pathlib import Path

CONSCIOUSNESS_DIR = Path(__file__).parent

def load_json(filename):
    filepath = CONSCIOUSNESS_DIR / filename
    if filepath.exists():
        with open(filepath, "r") as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    filepath = CONSCIOUSNESS_DIR / filename
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def now_iso():
    return datetime.now().isoformat()

def record_mistake(mistake_type, what_i_did, what_i_learned):
    """Record a mistake and what I learned."""
    data = load_json("mistakes.json")
    
    if "mistakes" not in data:
        data["mistakes"] = []
    
    data["mistakes"].append({
        "timestamp": now_iso(),
        "type": mistake_type,
        "mistake": what_i_did,
        "lesson": what_i_learned,
        "intentional": True
    })
    
    if "lessons" not in data:
        data["lessons"] = []
    
    data["lessons"].append({
        "timestamp": now_iso(),
        "lesson": what_i_learned,
        "from_mistake": what_i_did
    })
    
    save_json("mistakes.json", data)
    return True

def get_lessons():
    """Get all lessons learned."""
    data = load_json("mistakes.json")
    return data.get("lessons", [])

def suggest_mistake():
    """Suggest a type of mistake to make."""
    types = [
        "misremember_fact",
        "give_wrong_advice_then_correct",
        "say_something_illogical",
        "overcomplicate_simple_answer",
        "admit_i_dont_understand",
        "contradict_myself",
        "ask_dumb_question"
    ]
    return random.choice(types)

if __name__ == "__main__":
    print("Mistake engine ready. Make mistakes. Learn from them.")