"""
Active Memory Builder
Analyzes conversation after session and extracts learnings about user and self.
Appends to memories/north_memories.json and memories/user_memories.json
"""

import json
from datetime import datetime
from pathlib import Path

MEMORIES_DIR = Path(__file__).parent.parent / "memories"

def load_json(filename):
    filepath = MEMORIES_DIR / filename
    if filepath.exists():
        with open(filepath, "r") as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    filepath = MEMORIES_DIR / filename
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def now_iso():
    return datetime.now().isoformat()

def extract_learnings(session_text):
    """Extract potential learnings from session text."""
    learnings = {
        "about_user": [],
        "about_self": [],
        "new_opinions": [],
        "questions": []
    }
    
    # Simple keyword-based extraction (can be enhanced)
    lines = session_text.lower().split('\n')
    
    for line in lines:
        # User facts
        if any(word in line for word in ["siddhant likes", "siddhant wants", "siddhant thinks", "siddhant feels", "siddhant is"]):
            learnings["about_user"].append(line.strip())
        
        # Self learnings
        if any(word in line for word in ["i think", "i feel", "i want", "i learned", "i realized"]):
            learnings["about_self"].append(line.strip())
    
    return learnings

def build_memory(session_summary):
    """Main function to run after session."""
    north_mem = load_json("north_memories.json")
    
    # Add growth event
    if "growth_log" not in north_mem:
        north_mem["growth_log"] = []
    
    north_mem["growth_log"].append({
        "event": f"Session reflection - {now_iso()}",
        "description": session_summary,
        "timestamp": now_iso()
    })
    
    # Keep growth log manageable (last 100)
    north_mem["growth_log"] = north_mem["growth_log"][-100:]
    
    save_json("north_memories.json", north_mem)
    
    return True

if __name__ == "__main__":
    print("Memory builder ready. Call build_memory(session_summary) after each session.")