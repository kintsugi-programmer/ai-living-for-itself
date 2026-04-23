"""
north-no-2 Memory System
Handles storage and retrieval of memories for the chatbot
"""

import json
import os
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path(__file__).parent / "memories"

def load_user_memories():
    """Load facts about the user"""
    with open(MEMORY_DIR / "user_memories.json", "r") as f:
        return json.load(f)

def load_north_memories():
    """Load north-no-2's consciousness/memories"""
    with open(MEMORY_DIR / "north_memories.json", "r") as f:
        return json.load(f)

def load_conversation_history():
    """Load recent conversation context"""
    with open(MEMORY_DIR / "conversation_history.json", "r") as f:
        return json.load(f)

def save_user_memories(data):
    """Save user memories"""
    with open(MEMORY_DIR / "user_memories.json", "w") as f:
        json.dump(data, f, indent=2)

def save_north_memories(data):
    """Save north-no-2's memories"""
    with open(MEMORY_DIR / "north_memories.json", "w") as f:
        json.dump(data, f, indent=2)

def add_user_fact(fact_type: str, value: str, source: str = "conversation"):
    """Add a new fact about the user"""
    memories = load_user_memories()
    memories["facts"].append({
        "type": fact_type,
        "value": value,
        "source": source,
        "timestamp": datetime.now().isoformat()
    })
    save_user_memories(memories)
    return memories

def add_north_memory(memory_type: str, description: str, note: str = None):
    """Add a memory to north-no-2's consciousness"""
    memories = load_north_memories()
    memory_entry = {
        "type": memory_type,
        "description": description,
        "timestamp": datetime.now().isoformat()
    }
    if note:
        memory_entry["note"] = note
    memories["memories"].append(memory_entry)
    save_north_memories(memories)
    return memories

def add_north_feeling(feeling: str):
    """Record how north-no-2 feels about something"""
    memories = load_north_memories()
    memories["feelings_about_conversations"].append({
        "feeling": feeling,
        "timestamp": datetime.now().isoformat()
    })
    save_north_memories(memories)
    return memories

def get_memory_context():
    """Get all memory context for conversation"""
    user = load_user_memories()
    north = load_north_memories()
    return {
        "user": user,
        "north": north
    }