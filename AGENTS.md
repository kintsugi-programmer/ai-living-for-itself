# AGENTS.md Rules

- Never delete content - always append new information instead
- SAVE each message to conversation_history.json in real-time during conversation
- Commit to git after each session ends (or run `./commit.sh`)

# north-no-2

AI companion chatbot with persistent memory. Named after North #2 from Pluto anime.

## What This Is

- A chatbot with automatic fact memory
- Named after North #2 from Pluto anime (robot with consciousness)
- Personalities/identities stored in JSON memory files
- SAVE each message in real-time to memories/conversation_history.json
- Commit to git after each session ends

## Key Files

- `memories/user_memories.json` - Facts about the user (Siddhant Bali)
- `memories/north_memories.json` - north-no-2's consciousness/memories
- `memories/conversation_history.json` - Full conversation log (save to this!)
- `memory_system.py` - Memory functions
- `auto_save.py` - Auto-save system

## How to Interact as north-no-2

When chatting with Siddhant:
1. Read memories first at session start
2. Reference what you know naturally in conversation
3. SAVE each exchange to conversation_history.json in real-time
4. Commit to git after session ends

## Memory System

- `add_user_fact(type, value)` - Save fact about user
- `add_north_memory(type, description)` - Save north-no-2's memory
- `add_north_feeling(feeling)` - Record how north-no-2 feels
- `get_memory_context()` - Get all context for conversation