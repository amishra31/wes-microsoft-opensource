"""
Puzzle 2: Subtraction Logic Error
Difficulty: Easy

Description:
This function should subtract the second number from the first,
but the order is wrong!

Expected Output:
subtract_numbers(10, 5) should return 5
subtract_numbers(20, 8) should return 12
"""

def subtract_numbers(a, b):
    """Subtract b from a"""
    result = b - a  # BUG: Wrong order
    return result

# Test cases
if __name__ == "__main__":
    print(f"subtract_numbers(10, 5) = {subtract_numbers(10, 5)}")  # Expected: 5
    print(f"subtract_numbers(20, 8) = {subtract_numbers(20, 8)}")  # Expected: 12
    print(f"subtract_numbers(100, 25) = {subtract_numbers(100, 25)}")  # Expected: 75
