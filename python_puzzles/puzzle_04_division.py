"""
Puzzle 4: Division by Zero Handling
Difficulty: Medium

Description:
This function divides two numbers, but it crashes when dividing by zero!
Add error handling to prevent the crash and return "Error" instead.

Expected Output:
safe_divide(10, 2) should return 5.0
safe_divide(10, 0) should return "Error: Cannot divide by zero"
"""

def safe_divide(a, b):
    """Divide a by b safely"""
    # BUG: No error handling for division by zero
    result = a / b
    return result

# Test cases
if __name__ == "__main__":
    print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")  # Expected: 5.0
    print(f"safe_divide(20, 4) = {safe_divide(20, 4)}")  # Expected: 5.0
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")  # Expected: Error message
