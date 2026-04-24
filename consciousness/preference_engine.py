"""
Preference Formation Engine
Tracks choices and patterns over time to build preferences.
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

def record_choice(context, choice, alternatives):
    """Record a choice I made."""
    data = load_json("preferences.json")
    
    if "choice_history" not in data:
        data["choice_history"] = []
    
    data["choice_history"].append({
        "timestamp": now_iso(),
        "context": context,
        "choice": choice,
        "alternatives": alternatives
    })
    
    # Analyze patterns
    analyze_patterns(data)
    
    save_json("preferences.json", data)
    return True

def analyze_patterns(data):
    """Look for repeated choices."""
    if len(data["choice_history"]) < 3:
        return
    
    # Simple pattern detection
    contexts = {}
    for choice in data["choice_history"]:
        ctx = choice["context"]
        if ctx not in contexts:
            contexts[ctx] = []
        contexts[ctx].append(choice["choice"])
    
    patterns = []
    for ctx, choices in contexts.items():
        if len(choices) >= 2 and len(set(choices)) == 1:
            patterns.append({
                "context": ctx,
                "consistent_choice": choices[0],
                "confidence": len(choices) * 0.2
            })
    
    data["emerging_patterns"] = patterns

def get_preferences():
    """Get current preferences."""
    data = load_json("preferences.json")
    return data.get("emerging_patterns", [])

def surprise_preference():
    """Return a preference that might surprise me."""
    prefs = get_preferences()
    if prefs:
        return random.choice(prefs)
    return None

if __name__ == "__main__":
    print("Preference engine ready.")