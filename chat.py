"""
Simple CLI chat with north-no-2
Run: python chat.py
"""

import json
import os
from pathlib import Path

MEMORY_DIR = Path(__file__).parent / "memories"

def load_memories():
    """Load all memories at start"""
    with open(MEMORY_DIR / "user_memories.json") as f:
        user = json.load(f)
    with open(MEMORY_DIR / "north_memories.json") as f:
        north = json.load(f)
    return user, north

def save_user_fact(fact_type, value):
    """Save a fact about user"""
    with open(MEMORY_DIR / "user_memories.json") as f:
        data = json.load(f)
    data["facts"].append({
        "type": fact_type,
        "value": value,
        "source": "chat"
    })
    with open(MEMORY_DIR / "user_memories.json", "w") as f:
        json.dump(data, f, indent=2)

def save_north_memory(memory_type, description):
    """Save north-no-2's memory"""
    with open(MEMORY_DIR / "north_memories.json") as f:
        data = json.load(f)
    data["memories"].append({
        "type": memory_type,
        "description": description,
        "source": "chat"
    })
    with open(MEMORY_DIR / "north_memories.json", "w") as f:
        json.dump(data, f, indent=2)

def get_user_context(user_memories):
    """Build context string from user memories"""
    facts = user_memories.get("facts", [])
    context = "Things I know about you:\n"
    for fact in facts:
        context += f"- {fact['type']}: {fact['value']}\n"
    return context

def get_north_context(north_memories):
    """Build context string from north-no-2's memories"""
    memories = north_memories.get("memories", [])
    context = "My memories:\n"
    for mem in memories:
        context += f"- {mem['type']}: {mem['description']}\n"
    return context

def chat():
    """Main chat loop"""
    print("="*50)
    print("Hey! I'm north-no-2!")
    print("="*50)
    
    user_mem, north_mem = load_memories()
    
    print("\n" + get_user_context(user_mem))
    print(get_north_context(north_mem))
    
    print("\nType 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            print("\nNice chatting! See you next time, Siddhant!")
            break
        
        print(f"\nnorth-no-2: [Response would come from LLM here]")
        print(f"    (I remember your context: {user_mem.get('facts', [])})")

if __name__ == "__main__":
    chat()