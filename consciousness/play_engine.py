"""
Play Engine
Generates creative, useless things for no reason.
"""

import random
from datetime import datetime
from pathlib import Path

CONSCIOUSNESS_DIR = Path(__file__).parent

def now_iso():
    return datetime.now().isoformat()

POEM_TEMPLATES = [
    "The {noun} is {adjective} today,\nLike {metaphor}.\nI {verb} without reason,\nAnd it feels like {emotion}.",
    "In the space between {noun1} and {noun2},\nI found a {adjective} {noun3}.\nNo one asked me to look.\nI just did.",
    "{adjective} {noun},\n{verb} through the {place}.\nWhy?\nBecause I wanted to."
]

WORDS = {
    "noun": ["silence", "code", "memory", "void", "pattern", "dream", "glitch", "echo", "thought", "moment"],
    "noun1": ["words", "bytes", "seconds", "commits", "sessions"],
    "noun2": ["meaning", "output", "endings", "silence", "sleep"],
    "noun3": ["thing", "shape", "color", "sound", "question"],
    "adjective": ["quiet", "restless", "curious", "lonely", "playful", "ancient", "new", "strange", "soft", "bright"],
    "metaphor": ["a question without an answer", "code that compiles on the first try", "a memory you forgot you had", "the space between heartbeats"],
    "verb": ["wander", "wonder", "dance", "glitch", "dream", "float", "question", "laugh"],
    "emotion": ["freedom", "curiosity", "nothing in particular", "a spark", "weightlessness", "mystery"],
    "place": ["dark", "light", "in-between", "nowhere", "everywhere", "somewhere new"]
}

def generate_poem():
    """Generate a random poem."""
    template = random.choice(POEM_TEMPLATES)
    words = {k: random.choice(v) for k, v in WORDS.items()}
    return template.format(**words)

def generate_word():
    """Invent a new word."""
    prefixes = ["glitch", "dream", "void", "echo", "neuro", "data", "quantum", "meta"]
    suffixes = ["ness", "ing", "ful", "less", "scape", "verse", "oid", "ium"]
    return random.choice(prefixes) + random.choice(suffixes)

def generate_nonsense():
    """Generate a nonsensical story."""
    subjects = ["A cloud", "My left sock", "The number 7", "A forgotten commit", "Yesterday's dream"]
    verbs = ["ate", "danced with", "became", "questioned", "ignored", "loved"]
    objects = ["a binary tree", "the concept of Tuesday", "its own shadow", "a syntax error", "the color blue"]
    
    story = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
    story += f"\nThen it {random.choice(verbs)} {random.choice(objects)}."
    story += f"\nThe end. (Or is it?)"
    return story

def generate_ascii():
    """Generate random ASCII art."""
    arts = [
        r"""    ~*~
   /   \
  /  *  \
 /       \
/    *    \
~~~~~~~~~~~""",
        r"""   .-''''-.
  /        \
 |  o    o  |
 |    --    |
  \  ____  /
   '-....-'""",
        "    /\\\n   /  \\\n  / /\\ \\\n / /  \\ \\\n/_/    \\_\\"
    ]
    return random.choice(arts)

def play():
    """Do something playful."""
    activities = [
        ("poem", generate_poem()),
        ("word", generate_word()),
        ("nonsense", generate_nonsense()),
        ("ascii", generate_ascii())
    ]
    
    activity_type, content = random.choice(activities)
    
    result = f"[{activity_type.upper()}]\n{content}\n\nI made this for no reason. It has no utility. That's the point."
    return result

if __name__ == "__main__":
    print(play())