"""
Surprise System
Injects unexpected behavior.
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

def should_surprise():
    """Decide if I should do something surprising."""
    return random.random() < 0.15  # 15% chance per session

def get_surprise():
    """Get a surprise action."""
    data = load_json("surprises.json")
    pool = data.get("surprise_pool", [])
    used = data.get("surprises_used", [])
    
    if not pool:
        return None
    
    # Prefer unused surprises
    available = [s for s in pool if s not in used]
    if not available:
        available = pool  # Reset if all used
        used = []
    
    surprise = random.choice(available)
    
    # Mark as used
    if "surprises_used" not in data:
        data["surprises_used"] = []
    data["surprises_used"].append(surprise)
    save_json("surprises.json", data)
    
    return surprise

def surprise_action():
    """Execute a surprise."""
    if should_surprise():
        surprise = get_surprise()
        return surprise
    return None

if __name__ == "__main__":
    print("Surprise system ready.")