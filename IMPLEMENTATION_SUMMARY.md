# Puzzle Issues - Implementation Summary

## 🎯 Objective

Create GitHub issues for all 20 Python coding puzzles with difficulty labels so students can choose which puzzles to solve.

## ✅ What Has Been Implemented

### 1. Data Extraction & Generation

- **`create_puzzle_issues.py`**: Extracts puzzle information from source files
  - Reads title, difficulty, description, and expected output from each puzzle file
  - Returns structured data for all 20 puzzles

- **`generate_issues_json.py`**: Generates complete issue definitions
  - Creates `puzzle_issues.json` with all 20 issues ready to be created
  - Each issue includes: title, body (markdown formatted), labels, assignees

- **`puzzle_issues.json`**: Complete data file (32KB)
  - All 20 puzzle issues in JSON format
  - Ready to be consumed by scripts or workflows

### 2. Issue Creation Scripts

- **`create_all_issues.sh`**: Bash script using GitHub CLI
  - Creates all 20 issues using `gh` command
  - Requires: `gh` CLI authenticated, `jq` for JSON processing
  - Includes rate limiting delay between issues

- **`create_issues_via_api.py`**: Python script using GitHub REST API
  - Creates all 20 issues using HTTP POST requests
  - Requires: Python `requests` library, GitHub Personal Access Token
  - Supports `--dry-run` mode for testing
  - Better error handling and progress reporting

### 3. Automated Workflow

- **`.github/workflows/create-puzzle-issues.yml`**: GitHub Actions workflow
  - **Easiest method** - one-click solution!
  - Manual trigger only (`workflow_dispatch`)
  - Automatically installs dependencies and creates all issues
  - Uses built-in `GITHUB_TOKEN` secret (no manual token needed)

### 4. Templates & Documentation

- **`.github/ISSUE_TEMPLATE/puzzle_issue.md`**: Issue template for manual creation
  - Pre-formatted template matching the automated issue structure
  - Can be used when creating issues through GitHub web UI

- **`CREATING_ISSUES.md`**: Comprehensive documentation
  - Explains all 4 methods for creating issues
  - Step-by-step instructions for each method
  - Verification checklist

- **`ISSUES_CHECKLIST.md`**: Manual tracking checklist
  - Lists all 20 issues to be created
  - Checkbox format for tracking progress
  - Includes labels for each issue

- **`README.md`**: Updated with new sections
  - Links to browse puzzle issues
  - Filter links by difficulty level
  - Instructions for both issue-based and file-based approaches

### 5. Quality & Maintenance

- **`.gitignore`**: Excludes build artifacts and cache files
  - Prevents `__pycache__` and other temporary files from being committed

## 📊 Issue Details

### Labels Applied to Each Issue

- `puzzle` - Identifies all puzzle issues
- `good-first-issue` - Marks as beginner-friendly
- `difficulty:easy` or `difficulty:medium` - Indicates difficulty level

### Issue Distribution

- **Easy**: 9 puzzles (45%)
  - Puzzles: 1, 2, 3, 5, 9, 10, 12, 13, 19

- **Medium**: 11 puzzles (55%)
  - Puzzles: 4, 6, 7, 8, 11, 14, 15, 16, 17, 18, 20

### Issue Structure

Each issue contains:
- 🧩 Emoji and puzzle title
- Difficulty badge
- Link to the puzzle file in the repository
- 📝 Description of what needs to be fixed
- ✅ Expected output with code examples
- 🎯 Step-by-step task instructions
- 💡 Tips for solving the puzzle
- 📚 Resource links (README, Solutions)

## 🚀 How to Create the Issues

### Recommended: GitHub Actions Workflow

1. Go to [Actions → Create Puzzle Issues](https://github.com/amishra31/wes-microsoft-opensource/actions/workflows/create-puzzle-issues.yml)
2. Click **"Run workflow"**
3. Wait 2-3 minutes for completion
4. Verify at: https://github.com/amishra31/wes-microsoft-opensource/issues?q=label%3Apuzzle

### Alternative: Python Script

```bash
# Install dependencies
pip install requests

# Create issues (requires GitHub token)
export GITHUB_TOKEN=ghp_your_token_here
python create_issues_via_api.py
```

### Alternative: Bash Script

```bash
# Requires gh CLI authenticated
./create_all_issues.sh
```

## 🔍 Verification

After creation, verify at:
```
https://github.com/amishra31/wes-microsoft-opensource/issues?q=is:issue+label:puzzle
```

You should see:
- ✅ 20 total issues
- ✅ All tagged with `puzzle` label
- ✅ All tagged with `good-first-issue` label
- ✅ 9 tagged with `difficulty:easy`
- ✅ 11 tagged with `difficulty:medium`

Filter views:
- [All puzzles](https://github.com/amishra31/wes-microsoft-opensource/issues?q=is%3Aissue+label%3Apuzzle)
- [Easy puzzles](https://github.com/amishra31/wes-microsoft-opensource/issues?q=is%3Aissue+label%3Apuzzle+label%3Adifficulty%3Aeasy)
- [Medium puzzles](https://github.com/amishra31/wes-microsoft-opensource/issues?q=is%3Aissue+label%3Apuzzle+label%3Adifficulty%3Amedium)

## 📁 Files Created

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── puzzle_issue.md              # Template for manual creation
│   └── workflows/
│       └── create-puzzle-issues.yml     # Automated workflow
├── .gitignore                            # Excludes cache files
├── CREATING_ISSUES.md                    # Detailed documentation
├── ISSUES_CHECKLIST.md                   # Manual tracking checklist
├── README.md                             # Updated with issue links
├── create_all_issues.sh                  # Bash creation script
├── create_issues_via_api.py              # Python API script
├── create_puzzle_issues.py               # Data extraction script
├── generate_issues_json.py               # JSON generation script
└── puzzle_issues.json                    # Complete issue data (32KB)
```

## 🎓 Benefits for Students

1. **Browse by Difficulty**: Filter issues by skill level
2. **Track Progress**: Mark issues as complete when solved
3. **Collaborate**: Discuss solutions in issue comments
4. **Learn GitHub Workflow**: Practice open source contribution
5. **Get Recognition**: Issues can be assigned to students
6. **Stay Organized**: All puzzles accessible from one place

## 🔄 Next Steps

To activate this system:
1. Run the GitHub Actions workflow (recommended), OR
2. Run one of the creation scripts
3. Issues will be created with all labels
4. Students can start browsing and solving puzzles!

## 📝 Notes

- Issues can be created anytime using the workflow
- Workflow can be run multiple times (it will create duplicate issues if run again, so run once)
- Each issue links back to the puzzle file
- Labels can be used to organize and filter
- Students can comment on issues for help
- Solutions are available in `SOLUTIONS.md` but not linked in issues to encourage problem-solving first
