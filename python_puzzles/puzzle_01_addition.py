"""
Puzzle 1: Basic Addition Bug
Difficulty: Easy

Description:
This function should add two numbers together, but there's a bug!
Find and fix the error.

Expected Output:
add_numbers(5, 3) should return 8
add_numbers(10, 20) should return 30
"""

def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b  # BUG: Wrong operator used
    return result

# Test cases
if __name__ == "__main__":
    print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")  # Expected: 8
    print(f"add_numbers(10, 20) = {add_numbers(10, 20)}")  # Expected: 30
    print(f"add_numbers(100, 50) = {add_numbers(100, 50)}")  # Expected: 150
