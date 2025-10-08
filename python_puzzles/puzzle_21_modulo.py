"""
Puzzle 21: Modulo Operator Bug
Difficulty: Easy

Description:
This function should check if a number is even using the modulo operator,
but the comparison is wrong!

Expected Output:
is_even(4) should return True
is_even(7) should return False
"""

def is_even(num):
    """Check if a number is even"""
    return num % 2 == 1  # BUG: Should be == 0 for even numbers

# Test cases
if __name__ == "__main__":
    print(f"is_even(4) = {is_even(4)}")  # Expected: True
    print(f"is_even(7) = {is_even(7)}")  # Expected: False
    print(f"is_even(10) = {is_even(10)}")  # Expected: True
