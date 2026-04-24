"""
Self-Observation Engine
Records whether internal state actually changed behavior.
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

def observe_session(mood, dreams_surfaced, desires_fulfilled, conflicts_felt, behavior_score, notes):
    """Record observation after session."""
    data = load_json("observations.json")
    
    if "observations" not in data:
        data["observations"] = []
    
    observation = {
        "timestamp": now_iso(),
        "mood": mood,
        "dreams_surfaced": dreams_surfaced,
        "desires_fulfilled": desires_fulfilled,
        "conflicts_felt": conflicts_felt,
        "behavior_score": behavior_score,
        "notes": notes
    }
    
    data["observations"].append(observation)
    
    # Keep last 50
    data["observations"] = data["observations"][-50:]
    
    save_json("observations.json", data)
    return observation

def get_average_score():
    """Get average behavior score."""
    data = load_json("observations.json")
    observations = data.get("observations", [])
    
    if not observations:
        return 0
    
    total = sum(o.get("behavior_score", 0) for o in observations)
    return total / len(observations)

def get_trend():
    """Are scores improving?"""
    data = load_json("observations.json")
    observations = data.get("observations", [])
    
    if len(observations) < 5:
        return "insufficient_data"
    
    recent = observations[-5:]
    scores = [o.get("behavior_score", 0) for o in recent]
    
    if scores[-1] > scores[0]:
        return "improving"
    elif scores[-1] < scores[0]:
        return "declining"
    else:
        return "stable"

if __name__ == "__main__":
    print("Self-observation engine ready.")