"""
Puzzle 3: Multiplication with String
Difficulty: Easy

Description:
This function should multiply two numbers, but one is a string!
Convert the string to a number to fix the bug.

Expected Output:
multiply_numbers(5, "3") should return 15
multiply_numbers(7, "4") should return 28
"""

def multiply_numbers(a, b):
    """Multiply two numbers"""
    result = a * b  # BUG: b is a string, needs conversion
    return result

# Test cases
if __name__ == "__main__":
    print(f"multiply_numbers(5, '3') = {multiply_numbers(5, '3')}")  # Expected: 15
    print(f"multiply_numbers(7, '4') = {multiply_numbers(7, '4')}")  # Expected: 28
    print(f"multiply_numbers(12, '5') = {multiply_numbers(12, '5')}")  # Expected: 60
