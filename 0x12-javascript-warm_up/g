#!/bin/bash

# Array of random commit messages
messages=(
    "Fixed a bug"
    "Added new feature"
    "Updated documentation"
    "Refactored code"
    "Resolved merge conflict"
    "Implemented unit tests"
    "Optimized performance"
)

# Randomly select a message from the array
rand_index=$((RANDOM % ${#messages[@]}))
rand_message="${messages[$rand_index]}"

# Add all changes
git add .

# Commit with a random message
git commit -m "$rand_message"

# Push to the remote repository
git push

