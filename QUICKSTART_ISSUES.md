# Quick Start: Creating Puzzle Issues

## 🚀 Fastest Way (Recommended)

### GitHub Actions Workflow

1. **Go to Actions tab**: https://github.com/amishra31/wes-microsoft-opensource/actions/workflows/create-puzzle-issues.yml

2. **Click "Run workflow"** (green button on the right)

3. **Click "Run workflow"** again in the dropdown

4. **Wait ~2 minutes** for all 20 issues to be created

5. **View your issues**: https://github.com/amishra31/wes-microsoft-opensource/issues?q=label:puzzle

That's it! ✅

---

## 📊 What Gets Created

**20 GitHub Issues**, each with:
- ✅ Clear title: "Puzzle X: [Name]"
- ✅ Three labels: `puzzle`, `good-first-issue`, `difficulty:easy/medium`
- ✅ Detailed description with:
  - What the puzzle is about
  - Expected output
  - Step-by-step instructions
  - Tips and resources

---

## 🔍 Finding Issues

After creation, students can:

**Browse all puzzles:**
https://github.com/amishra31/wes-microsoft-opensource/issues?q=label:puzzle

**Filter by difficulty:**
- Easy: https://github.com/amishra31/wes-microsoft-opensource/issues?q=label:puzzle+label:difficulty:easy
- Medium: https://github.com/amishra31/wes-microsoft-opensource/issues?q=label:puzzle+label:difficulty:medium

---

## 🎓 For Students

Once issues are created, you can:

1. **Browse** the puzzle issues
2. **Pick one** that matches your skill level
3. **Comment** on the issue to claim it
4. **Solve** the puzzle
5. **Share** your solution in the comments (or submit a PR!)

---

## 📚 More Information

- **Detailed documentation**: See `CREATING_ISSUES.md`
- **Implementation details**: See `IMPLEMENTATION_SUMMARY.md`
- **Manual checklist**: See `ISSUES_CHECKLIST.md`

---

## 🐛 Troubleshooting

**If the workflow fails:**
1. Check the workflow run logs
2. Ensure the repository has `issues: write` permission
3. Try running the Python script manually (see `CREATING_ISSUES.md`)

**If issues already exist:**
- The workflow will create duplicates if run multiple times
- Delete existing puzzle issues before re-running if needed

---

**Ready to create issues? [Click here to start!](https://github.com/amishra31/wes-microsoft-opensource/actions/workflows/create-puzzle-issues.yml)** 🚀
