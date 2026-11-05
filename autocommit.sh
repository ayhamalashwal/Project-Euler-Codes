#!/bin/bash

# Navigate to repository directory
REPO_DIR="/home/ayhamalashwal/Desktop/project_euler"
cd "$REPO_DIR" || exit

echo "Watching $REPO_DIR for changes..."

# Loop indefinitely, waiting for files to be written, created, deleted, or moved
while inotifywait -r -e close_write,create,delete,moved_to --exclude '\.git' .; do
    # Stage the changes
    git add .
    
    # Check if there are changes to commit
    if ! git diff-index --quiet HEAD --; then
        git commit -m "Update project euler code"
        git push origin main
        echo "Changes pushed to GitHub"
    fi
done
