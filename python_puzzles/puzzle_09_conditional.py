"""
Puzzle 9: Conditional Statement Bug
Difficulty: Easy

Description:
This function should check if a number is positive, negative, or zero,
but the conditions are incorrect!

Expected Output:
check_number(5) should return "Positive"
check_number(-3) should return "Negative"
check_number(0) should return "Zero"
"""

def check_number(num):
    """Check if a number is positive, negative, or zero"""
    if num < 0:
        return "Negative"  # BUG: Should return "Negative"
    elif num > 0:
        return "Positive"  # BUG: Should return "Positive"
    else:
        return "Zero"

# Test cases
if __name__ == "__main__":
    print(f"check_number(5) = {check_number(5)}")  # Expected: Positive
    print(f"check_number(-3) = {check_number(-3)}")  # Expected: Negative
    print(f"check_number(0) = {check_number(0)}")  # Expected: Zero
