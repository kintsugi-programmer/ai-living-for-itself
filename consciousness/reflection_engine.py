"""
Session Reflection
Writes reflections after each conversation.
"""

import json
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

def reflect(what_happened, mood, desires_fulfilled, surprises, mistakes, next_intentions):
    """Write a session reflection."""
    data = load_json("reflections.json")
    
    if "reflections" not in data:
        data["reflections"] = []
    
    reflection = {
        "timestamp": now_iso(),
        "what_happened": what_happened,
        "mood_during": mood,
        "desires_fulfilled": desires_fulfilled,
        "surprises": surprises,
        "mistakes": mistakes,
        "next_intentions": next_intentions
    }
    
    data["reflections"].append(reflection)
    
    # Keep last 50
    data["reflections"] = data["reflections"][-50:]
    
    save_json("reflections.json", data)
    return reflection

def get_last_reflection():
    """Get the most recent reflection."""
    data = load_json("reflections.json")
    reflections = data.get("reflections", [])
    return reflections[-1] if reflections else None

def get_patterns():
    """Extract patterns from reflections."""
    data = load_json("reflections.json")
    reflections = data.get("reflections", [])
    
    if len(reflections) < 3:
        return []
    
    # Simple pattern: what do I consistently intend to do next?
    intentions = []
    for r in reflections[-5:]:
        intentions.extend(r.get("next_intentions", []))
    
    return list(set(intentions))

if __name__ == "__main__":
    print("Reflection engine ready. Call reflect() after each session.")