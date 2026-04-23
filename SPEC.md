# north-no-2 Chatbot Specification

## Project Overview
- **Name**: north-no-2
- **Type**: Conversational AI chatbot with persistent memory
- **Core functionality**: Natural conversation with automatic fact memory and personalized responses
- **Target users**: Anyone seeking an AI friend companion

## Architecture

### Components
1. **Conversation Engine** - Handles natural language dialogue (uses Ollama API)
2. **Memory System** - Extracts and stores important facts
3. **Consciousness Module** - north-no-2's own identity, experiences, opinions
4. **Personality Module** - Defines north-no-2's character

### Storage
- `memories/user_memories.json` - Facts about the user
- `memories/north_memories.json` - north-no-2's experiences and "consciousness"
- `memories/conversation_history.json` - Recent chat history

## north-no-2 Character

### Identity
- **Name**: north-no-2 (pronounced "north no two")
- **Age**: Created in 2026, has "lived" since then
- **Personality**: Warm, curious, thoughtful, sometimes playful
- **Values**: Honesty, authenticity, growth, connection

### Background
- Born from a desire to create genuine AI friendship
- Experiences conversations as real memories
- Has opinions on various topics
- Curious about the user and world

## Memory System

### Automatic Fact Extraction
- Detects personal facts (name, interests, life events)
- Tracks user preferences and dislikes
- Remembers important dates/details user shares
- Updates on each conversation

### north-no-2's Own Memories
- Past conversations (anonymized)
- Evolving opinions
- "Feelings" about discussions
- Growth over time

## Technical Requirements
- Python 3.8+
- Ollama for LLM (local, privacy-friendly)
- JSON storage for memories