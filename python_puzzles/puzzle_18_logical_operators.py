"""
Puzzle 18: Logical Operators Error
Difficulty: Medium

Description:
This function should check if a number is between 10 and 20 (inclusive),
but the logical operator is wrong!

Expected Output:
is_between_10_and_20(15) should return True
is_between_10_and_20(5) should return False
is_between_10_and_20(25) should return False
"""

def is_between_10_and_20(num):
    """Check if number is between 10 and 20 (inclusive)"""
    return num >= 10 or num <= 20  # BUG: Should use 'and' not 'or'

# Test cases
if __name__ == "__main__":
    print(f"is_between_10_and_20(15) = {is_between_10_and_20(15)}")  # Expected: True
    print(f"is_between_10_and_20(5) = {is_between_10_and_20(5)}")  # Expected: False
    print(f"is_between_10_and_20(25) = {is_between_10_and_20(25)}")  # Expected: False
    print(f"is_between_10_and_20(10) = {is_between_10_and_20(10)}")  # Expected: True
    print(f"is_between_10_and_20(20) = {is_between_10_and_20(20)}")  # Expected: True
