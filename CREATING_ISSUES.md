# Creating Puzzle Issues

This directory contains scripts to create GitHub issues for all 20 Python coding puzzles.

## Overview

Each puzzle will get its own GitHub issue with:
- **Title**: "Puzzle X: [Puzzle Name]"
- **Labels**: 
  - `puzzle` - identifies it as a puzzle issue
  - `good-first-issue` - marks it as beginner-friendly
  - `difficulty:easy` or `difficulty:medium` - indicates difficulty level
- **Body**: Detailed description, expected output, tasks, tips, and resources

## Files

- **`create_puzzle_issues.py`**: Extracts puzzle information from puzzle files
- **`generate_issues_json.py`**: Generates JSON file with all issue data
- **`puzzle_issues.json`**: JSON file containing all 20 issue definitions
- **`create_all_issues.sh`**: Bash script to create all issues using GitHub CLI
- **`.github/ISSUE_TEMPLATE/puzzle_issue.md`**: Template for manual issue creation

## Method 1: Automated Creation (Recommended)

### Prerequisites
- GitHub CLI (`gh`) installed and authenticated
- `jq` for JSON processing

### Steps

1. **Generate the issues JSON** (already done if `puzzle_issues.json` exists):
   ```bash
   python generate_issues_json.py
   ```

2. **Create all issues at once**:
   ```bash
   ./create_all_issues.sh
   ```

This will create all 20 issues in sequence with appropriate labels.

## Method 2: Manual Creation via GitHub CLI

If you prefer to create issues one at a time:

```bash
# Example: Create Puzzle 1 issue
gh issue create --repo amishra31/wes-microsoft-opensource \
  --title "Puzzle 1: Basic Addition Bug" \
  --body-file <(jq -r '.[0].body' puzzle_issues.json) \
  --label puzzle,good-first-issue,difficulty:easy
```

## Method 3: Manual Creation via GitHub Web UI

1. Go to https://github.com/amishra31/wes-microsoft-opensource/issues/new
2. Choose "Python Puzzle" template
3. Fill in the details for each puzzle using information from the puzzle files
4. Add appropriate labels: `puzzle`, `good-first-issue`, and `difficulty:easy` or `difficulty:medium`

## Puzzle List

The following 20 puzzles will get issues created:

### Easy Difficulty (10 puzzles)
1. Puzzle 1: Basic Addition Bug
2. Puzzle 2: Subtraction Logic Error
3. Puzzle 3: Multiplication with String
4. Puzzle 5: String Concatenation Bug
5. Puzzle 9: Conditional Statement Bug
6. Puzzle 10: Function Return Value Bug
7. Puzzle 12: Type Conversion Error
8. Puzzle 13: String Formatting Bug
9. Puzzle 19: String Methods Bug

### Medium Difficulty (11 puzzles)
1. Puzzle 4: Division by Zero Handling
2. Puzzle 6: String Slicing Error
3. Puzzle 7: List Manipulation Bug
4. Puzzle 8: Loop Logic Error
5. Puzzle 11: Variable Scope Issue
6. Puzzle 14: List Comprehension to Implement
7. Puzzle 15: Dictionary Operations Bug
8. Puzzle 16: Set Operations to Implement
9. Puzzle 17: Exception Handling Bug
10. Puzzle 18: Logical Operators Error
11. Puzzle 20: Mathematical Formula Implementation

## Issue Format

Each issue will have this structure:

```markdown
## 🧩 [Puzzle Title]

**Difficulty:** Easy/Medium  
**File:** [Link to puzzle file]

### 📝 Description
[What the puzzle is about]

### ✅ Expected Output
[What the correct output should be]

### 🎯 Your Task
[Step-by-step instructions]

### 💡 Tips
[Helpful hints]

### 📚 Resources
[Links to README and solutions]
```

## Benefits

Creating these issues allows students to:
- **Choose puzzles by difficulty**: Filter issues by `difficulty:easy` or `difficulty:medium` labels
- **Track progress**: Mark issues as complete when solved
- **Collaborate**: Discuss solutions and ask questions in issue comments
- **Learn open source workflow**: Practice the process of working with GitHub issues
- **Get recognition**: Issues can be assigned to students who solve them

## Verification

After creating issues, verify them at:
https://github.com/amishra31/wes-microsoft-opensource/issues?q=is%3Aissue+label%3Apuzzle

You should see:
- 20 total issues
- All tagged with `puzzle` label
- 9 tagged with `difficulty:easy`
- 11 tagged with `difficulty:medium`
- All tagged with `good-first-issue`
