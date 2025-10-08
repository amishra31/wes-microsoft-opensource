#!/usr/bin/env python3
"""
Generate JSON data for creating GitHub issues for all Python puzzles.
This script creates a JSON file that can be used with GitHub CLI or API to bulk create issues.
"""

import json
import os
import sys

# Add parent directory to path to import create_puzzle_issues
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from create_puzzle_issues import get_all_puzzles, generate_issue_body

def generate_issues_json():
    """Generate JSON data for all puzzle issues."""
    puzzles = get_all_puzzles()
    
    issues_data = []
    
    for puzzle in puzzles:
        issue_data = {
            "title": f"Puzzle {puzzle['number']}: {puzzle['short_title']}",
            "body": generate_issue_body(puzzle),
            "labels": ["puzzle", "good-first-issue", f"difficulty:{puzzle['difficulty'].lower()}"],
            "assignees": []
        }
        issues_data.append(issue_data)
    
    return issues_data

def main():
    """Generate and save issues JSON."""
    issues = generate_issues_json()
    
    # Save to JSON file
    output_file = 'puzzle_issues.json'
    with open(output_file, 'w') as f:
        json.dump(issues, f, indent=2)
    
    print(f"✅ Generated {len(issues)} issue definitions")
    print(f"📄 Saved to: {output_file}")
    print()
    print("To create these issues using GitHub CLI, run:")
    print()
    for i, issue in enumerate(issues, 1):
        print(f"  gh issue create --repo amishra31/wes-microsoft-opensource \\")
        print(f"    --title \"{issue['title']}\" \\")
        print(f"    --body-file <(jq -r '.[{i-1}].body' puzzle_issues.json) \\")
        print(f"    --label {','.join(issue['labels'])}")
        if i < len(issues):
            print()
    
    print()
    print("=" * 80)
    print("Or use the batch creation script: ./create_all_issues.sh")
    print("=" * 80)

if __name__ == "__main__":
    main()
