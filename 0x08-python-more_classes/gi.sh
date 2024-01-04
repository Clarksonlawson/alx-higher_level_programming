#!/bin/bash

# Generate a random number for the commit message
random_number=$((1 + RANDOM % 1000))

# Add all changes
git add .

# Commit with a random message
git commit -m "Random commit message: $random_number"

# Push changes to the default branch (e.g., main or master)
git push origin HEAD

# Print a message indicating the successful operation
echo "Changes staged, committed, and pushed successfully."
