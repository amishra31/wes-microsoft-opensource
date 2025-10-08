#!/usr/bin/env python3
"""
Test Runner for Python Puzzles
This script shows the status of all 30 puzzles
"""

import os
import sys

def main():
    puzzles_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List of all puzzles
    puzzles = [
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
        ("puzzle_21_modulo.py", "Modulo Operator Bug", "Easy"),
        ("puzzle_22_string_case.py", "String Case Conversion Bug", "Easy"),
        ("puzzle_23_list_indexing.py", "List Indexing Error", "Easy"),
        ("puzzle_24_boolean_logic.py", "Boolean Logic Bug", "Easy"),
        ("puzzle_25_increment.py", "Increment Operator Bug", "Easy"),
        ("puzzle_26_string_split.py", "String Split Method Bug", "Easy"),
        ("puzzle_27_nested_loops.py", "Nested Loop Logic Error", "Medium"),
        ("puzzle_28_tuple_operations.py", "Tuple Operations Bug", "Medium"),
        ("puzzle_29_recursive_function.py", "Recursive Function Implementation", "Hard"),
        ("puzzle_30_sorting_algorithm.py", "Sorting Algorithm Bug", "Hard"),
    ]
    
    print("=" * 80)
    print("PYTHON CODING PUZZLES - STATUS CHECK")
    print("=" * 80)
    print()
    
    # Check if all puzzles exist
    missing = []
    for filename, title, difficulty in puzzles:
        filepath = os.path.join(puzzles_dir, filename)
        exists = os.path.isfile(filepath)
        status = "✓" if exists else "✗"
        
        if not exists:
            missing.append(filename)
        
        print(f"{status} {filename:<35} {title:<45} [{difficulty}]")
    
    print()
    print("=" * 80)
    print(f"Total Puzzles: {len(puzzles)}")
    print(f"Present: {len(puzzles) - len(missing)}")
    print(f"Missing: {len(missing)}")
    
    if missing:
        print("\nMissing files:")
        for f in missing:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("\n✓ All puzzles are present!")
        print("\nTo get started:")
        print("  1. Choose a puzzle file")
        print("  2. Read the description and expected output")
        print("  3. Fix the bug or implement the missing code")
        print("  4. Run: python <puzzle_file>.py")
        print("  5. Check if output matches expected output")
        print("\nFor solutions, see SOLUTIONS.md")
    
    print("=" * 80)

if __name__ == "__main__":
    main()
