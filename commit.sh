#!/bin/bash
# north-no-2 auto-commit helper
# Run this to commit current session

cd "$(dirname "$0")"

# Add all changes
git add -A

# Commit with timestamp
git commit -m "Auto-commit $(date '+%Y-%m-%d %H:%M')"

echo "Committed!"