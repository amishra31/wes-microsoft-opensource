#!/usr/bin/env python3
"""
Script to create GitHub issues for Python puzzles
This script reads all puzzle files and creates corresponding GitHub issues
with difficulty labels.
"""

import os
import re
import sys

def extract_puzzle_info(filepath):
    """Extract title, difficulty, description, and expected output from puzzle file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract from docstring at the top
    lines = content.split('\n')
    
    title = None
    difficulty = None
    description_lines = []
    expected_lines = []
    
    in_description = False
    in_expected = False
    
    for line in lines:
        # Look for title
        if line.startswith('Puzzle ') and ':' in line:
            title = line.replace('"""', '').strip()
        
        # Look for difficulty
        elif line.startswith('Difficulty:'):
            difficulty = line.replace('Difficulty:', '').strip()
        
        # Look for description section
        elif line.startswith('Description:'):
            in_description = True
            in_expected = False
        
        # Look for expected output section
        elif line.startswith('Expected Output:'):
            in_description = False
            in_expected = True
        
        # End of docstring
        elif '"""' in line and (in_description or in_expected):
            break
        
        # Collect description lines
        elif in_description and line.strip():
            description_lines.append(line.strip())
        
        # Collect expected output lines
        elif in_expected and line.strip():
            expected_lines.append(line.strip())
    
    description = '\n'.join(description_lines)
    expected_output = '\n'.join(expected_lines)
    
    return {
        'title': title,
        'difficulty': difficulty,
        'description': description,
        'expected_output': expected_output
    }

def get_all_puzzles():
    """Get information for all puzzles."""
    puzzles_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'python_puzzles')
    
    # List from check_puzzles.py
    puzzle_files = [
        ("puzzle_01_addition.py", "Basic Addition Bug", "Easy"),
        ("puzzle_02_subtraction.py", "Subtraction Logic Error", "Easy"),
        ("puzzle_03_multiplication.py", "Multiplication with String", "Easy"),
        ("puzzle_04_division.py", "Division by Zero Handling", "Medium"),
        ("puzzle_05_string_concat.py", "String Concatenation Bug", "Easy"),
        ("puzzle_06_string_slicing.py", "String Slicing Error", "Medium"),
        ("puzzle_07_list_manipulation.py", "List Manipulation Bug", "Medium"),
        ("puzzle_08_loop_logic.py", "Loop Logic Error", "Medium"),
        ("puzzle_09_conditional.py", "Conditional Statement Bug", "Easy"),
        ("puzzle_10_function_return.py", "Function Return Value Bug", "Easy"),
        ("puzzle_11_variable_scope.py", "Variable Scope Issue", "Medium"),
        ("puzzle_12_type_conversion.py", "Type Conversion Error", "Easy"),
        ("puzzle_13_string_formatting.py", "String Formatting Bug", "Easy"),
        ("puzzle_14_list_comprehension.py", "List Comprehension to Implement", "Medium"),
        ("puzzle_15_dictionary.py", "Dictionary Operations Bug", "Medium"),
        ("puzzle_16_set_operations.py", "Set Operations to Implement", "Medium"),
        ("puzzle_17_exception_handling.py", "Exception Handling Bug", "Medium"),
        ("puzzle_18_logical_operators.py", "Logical Operators Error", "Medium"),
        ("puzzle_19_string_methods.py", "String Methods Bug", "Easy"),
        ("puzzle_20_average.py", "Mathematical Formula Implementation", "Medium"),
    ]
    
    puzzles = []
    for filename, short_title, difficulty in puzzle_files:
        filepath = os.path.join(puzzles_dir, filename)
        if os.path.exists(filepath):
            info = extract_puzzle_info(filepath)
            puzzle_num = filename.split('_')[1]
            puzzles.append({
                'number': int(puzzle_num),
                'filename': filename,
                'title': info['title'] or f"Puzzle {puzzle_num}: {short_title}",
                'short_title': short_title,
                'difficulty': info['difficulty'] or difficulty,
                'description': info['description'],
                'expected_output': info['expected_output'],
                'filepath': f"python_puzzles/{filename}"
            })
    
    return sorted(puzzles, key=lambda x: x['number'])

def generate_issue_body(puzzle):
    """Generate the issue body for a puzzle."""
    body = f"""## 🧩 {puzzle['short_title']}

**Difficulty:** {puzzle['difficulty']}  
**File:** [`{puzzle['filepath']}`](https://github.com/amishra31/wes-microsoft-opensource/blob/main/{puzzle['filepath']})

### 📝 Description

{puzzle['description']}

### ✅ Expected Output

```
{puzzle['expected_output']}
```

### 🎯 Your Task

1. Open the file: `{puzzle['filepath']}`
2. Read the description and understand what the function should do
3. Find and fix the bug or implement the missing code
4. Run the file to test your solution: `python {puzzle['filename']}`
5. Verify the output matches the expected output above

### 💡 Tips

- Read error messages carefully - Python error messages are very helpful
- Look for comments marked with `BUG` or `TODO`
- Test your changes incrementally
- Check `SOLUTIONS.md` if you get stuck

### 📚 Resources

- [Python Puzzles README](https://github.com/amishra31/wes-microsoft-opensource/blob/main/python_puzzles/README.md)
- [Solutions Guide](https://github.com/amishra31/wes-microsoft-opensource/blob/main/python_puzzles/SOLUTIONS.md)

---

**Good luck and happy coding! 🐍✨**
"""
    return body

def main():
    """Main function to display puzzle information for issue creation."""
    puzzles = get_all_puzzles()
    
    print("=" * 80)
    print("PYTHON PUZZLES - GITHUB ISSUES TO CREATE")
    print("=" * 80)
    print()
    print(f"Total puzzles found: {len(puzzles)}")
    print()
    
    for puzzle in puzzles:
        print(f"Puzzle {puzzle['number']:2d}: {puzzle['short_title']}")
        print(f"  Title: {puzzle['title']}")
        print(f"  Difficulty: {puzzle['difficulty']}")
        print(f"  File: {puzzle['filepath']}")
        print()
    
    print("=" * 80)
    print("\nTo create issues, this data will be used with the GitHub API.")
    print("Issue titles will be in format: 'Puzzle {number}: {short_title}'")
    print("Labels will be: 'puzzle', 'difficulty:{Easy|Medium}'")
    print("=" * 80)
    
    # Return puzzles for external use
    return puzzles

if __name__ == "__main__":
    puzzles = main()
    
    # Print sample issue for verification
    if puzzles:
        print("\n\nSample Issue Body (Puzzle 1):")
        print("=" * 80)
        print(generate_issue_body(puzzles[0]))
