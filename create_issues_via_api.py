#!/usr/bin/env python3
"""
Create GitHub issues for all puzzles using the GitHub REST API.

Usage:
    export GITHUB_TOKEN=your_token_here
    python create_issues_via_api.py

Or:
    python create_issues_via_api.py --token your_token_here
"""

import argparse
import json
import os
import sys
import time

try:
    import requests
except ImportError:
    print("Error: requests library not found")
    print("Install it with: pip install requests")
    sys.exit(1)


def create_issue(repo_owner, repo_name, title, body, labels, token):
    """Create a GitHub issue using the REST API."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        issue_data = response.json()
        return True, issue_data["number"], issue_data["html_url"]
    else:
        return False, None, response.text


def main():
    parser = argparse.ArgumentParser(description="Create GitHub issues for all puzzles")
    parser.add_argument("--token", help="GitHub personal access token")
    parser.add_argument("--repo-owner", default="amishra31", help="Repository owner")
    parser.add_argument("--repo-name", default="wes-microsoft-opensource", help="Repository name")
    parser.add_argument("--issues-file", default="puzzle_issues.json", help="JSON file with issue data")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually create issues, just show what would be created")
    
    args = parser.parse_args()
    
    # Get token
    token = args.token or os.environ.get("GITHUB_TOKEN")
    
    if not token and not args.dry_run:
        print("Error: GitHub token required")
        print("Provide via --token argument or GITHUB_TOKEN environment variable")
        print("\nTo create a token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select scope: 'repo' (Full control of private repositories)")
        print("4. Generate and copy the token")
        sys.exit(1)
    
    # Load issues data
    if not os.path.exists(args.issues_file):
        print(f"Error: {args.issues_file} not found")
        print("Run: python generate_issues_json.py")
        sys.exit(1)
    
    with open(args.issues_file, 'r') as f:
        issues = json.load(f)
    
    print(f"Found {len(issues)} issues to create")
    print(f"Repository: {args.repo_owner}/{args.repo_name}")
    print()
    
    if args.dry_run:
        print("DRY RUN MODE - No issues will be created")
        print()
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue['title']}")
            print(f"   Labels: {', '.join(issue['labels'])}")
        print()
        print(f"Total: {len(issues)} issues")
        return
    
    # Create issues
    created = 0
    failed = 0
    
    for i, issue in enumerate(issues, 1):
        print(f"Creating {i}/{len(issues)}: {issue['title']}")
        
        success, number, url = create_issue(
            args.repo_owner,
            args.repo_name,
            issue['title'],
            issue['body'],
            issue['labels'],
            token
        )
        
        if success:
            print(f"  ✅ Created issue #{number}: {url}")
            created += 1
        else:
            print(f"  ❌ Failed: {url}")
            failed += 1
        
        # Rate limiting: wait 1 second between requests
        if i < len(issues):
            time.sleep(1)
    
    print()
    print("=" * 80)
    print(f"✅ Created: {created}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Total: {len(issues)}")
    print()
    print(f"View issues at: https://github.com/{args.repo_owner}/{args.repo_name}/issues")
    print("=" * 80)


if __name__ == "__main__":
    main()
