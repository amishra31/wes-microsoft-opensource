# Puzzle Issues Creation Checklist

This checklist helps track the creation of all 20 puzzle issues.

## Quick Start

**Easiest Method**: Use the [GitHub Actions Workflow](https://github.com/amishra31/wes-microsoft-opensource/actions/workflows/create-puzzle-issues.yml)
- Click "Run workflow" button
- All issues will be created automatically

## Manual Creation Tracking

If creating issues manually, use this checklist:

### Easy Puzzles (9 total)

- [ ] **Issue 1**: Puzzle 1: Basic Addition Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 2**: Puzzle 2: Subtraction Logic Error
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 3**: Puzzle 3: Multiplication with String
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 5**: Puzzle 5: String Concatenation Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 9**: Puzzle 9: Conditional Statement Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 10**: Puzzle 10: Function Return Value Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 12**: Puzzle 12: Type Conversion Error
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 13**: Puzzle 13: String Formatting Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`
  
- [ ] **Issue 19**: Puzzle 19: String Methods Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:easy`

### Medium Puzzles (11 total)

- [ ] **Issue 4**: Puzzle 4: Division by Zero Handling
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 6**: Puzzle 6: String Slicing Error
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 7**: Puzzle 7: List Manipulation Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 8**: Puzzle 8: Loop Logic Error
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 11**: Puzzle 11: Variable Scope Issue
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 14**: Puzzle 14: List Comprehension to Implement
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 15**: Puzzle 15: Dictionary Operations Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 16**: Puzzle 16: Set Operations to Implement
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 17**: Puzzle 17: Exception Handling Bug
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 18**: Puzzle 18: Logical Operators Error
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`
  
- [ ] **Issue 20**: Puzzle 20: Mathematical Formula Implementation
  - Labels: `puzzle`, `good-first-issue`, `difficulty:medium`

## Automated Creation

### Using Scripts

1. **Bash Script** (requires `gh` CLI):
   ```bash
   ./create_all_issues.sh
   ```

2. **Python API Script** (requires `requests` and GitHub token):
   ```bash
   export GITHUB_TOKEN=your_token
   python create_issues_via_api.py
   ```

3. **Dry Run** (to preview without creating):
   ```bash
   python create_issues_via_api.py --dry-run
   ```

## Verification

After creation, verify all issues at:
- https://github.com/amishra31/wes-microsoft-opensource/issues?q=is%3Aissue+label%3Apuzzle

Expected results:
- ✅ 20 total issues
- ✅ 9 with `difficulty:easy` label
- ✅ 11 with `difficulty:medium` label
- ✅ All with `puzzle` and `good-first-issue` labels

## Issue Body Template

Each issue uses this template (from `puzzle_issues.json`):

```markdown
## 🧩 [Puzzle Name]

**Difficulty:** Easy/Medium  
**File:** [Link to puzzle file]

### 📝 Description
[Description from puzzle file]

### ✅ Expected Output
[Expected output from test cases]

### 🎯 Your Task
1. Open the file
2. Read the description
3. Find and fix the bug
4. Run and test
5. Verify output

### 💡 Tips
- Read error messages
- Look for BUG/TODO comments
- Test incrementally
- Check SOLUTIONS.md if stuck

### 📚 Resources
- Python Puzzles README
- Solutions Guide
```
