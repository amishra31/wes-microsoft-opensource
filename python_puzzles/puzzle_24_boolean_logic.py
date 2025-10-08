"""
Puzzle 24: Boolean Logic Bug
Difficulty: Easy

Description:
This function should return True if a number is positive,
but the comparison operator is wrong!

Expected Output:
is_positive(5) should return True
is_positive(-3) should return False
"""

def is_positive(num):
    """Check if a number is positive"""
    return num < 0  # BUG: Should be > 0 for positive numbers

# Test cases
if __name__ == "__main__":
    print(f"is_positive(5) = {is_positive(5)}")  # Expected: True
    print(f"is_positive(-3) = {is_positive(-3)}")  # Expected: False
    print(f"is_positive(0) = {is_positive(0)}")  # Expected: False
