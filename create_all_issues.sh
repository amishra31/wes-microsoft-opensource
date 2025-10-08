#!/bin/bash
# Script to create all puzzle issues using GitHub CLI
# This script reads the puzzle_issues.json file and creates issues for each puzzle

set -e

REPO="amishra31/wes-microsoft-opensource"
ISSUES_FILE="puzzle_issues.json"

if [ ! -f "$ISSUES_FILE" ]; then
    echo "Error: $ISSUES_FILE not found!"
    echo "Please run: python generate_issues_json.py"
    exit 1
fi

# Check if gh is authenticated
if ! gh auth status &> /dev/null; then
    echo "Error: GitHub CLI is not authenticated"
    echo "Please run: gh auth login"
    exit 1
fi

# Count total issues
TOTAL=$(jq '. | length' "$ISSUES_FILE")
echo "Creating $TOTAL puzzle issues..."
echo

# Create each issue
for i in $(seq 0 $((TOTAL - 1))); do
    TITLE=$(jq -r ".[$i].title" "$ISSUES_FILE")
    BODY=$(jq -r ".[$i].body" "$ISSUES_FILE")
    LABELS=$(jq -r ".[$i].labels | join(\",\")" "$ISSUES_FILE")
    
    echo "Creating issue $((i + 1))/$TOTAL: $TITLE"
    
    # Create the issue
    gh issue create \
        --repo "$REPO" \
        --title "$TITLE" \
        --body "$BODY" \
        --label "$LABELS"
    
    echo "✅ Created"
    echo
    
    # Small delay to avoid rate limiting
    sleep 1
done

echo "=" $(printf '=%.0s' {1..80})
echo "✅ All $TOTAL issues created successfully!"
echo "View them at: https://github.com/$REPO/issues"
echo "=" $(printf '=%.0s' {1..80})
