"""
Puzzle 11: Variable Scope Issue
Difficulty: Medium

Description:
This function should calculate the area of a rectangle,
but there's a variable scope issue with the indentation!

Expected Output:
calculate_area(5, 10) should return 50
calculate_area(3, 7) should return 21
"""

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    if length > 0 and width > 0:
        area = length * width
    return area  # BUG: area is only defined inside if block, causes UnboundLocalError

# Test cases
if __name__ == "__main__":
    print(f"calculate_area(5, 10) = {calculate_area(5, 10)}")  # Expected: 50
    print(f"calculate_area(3, 7) = {calculate_area(3, 7)}")  # Expected: 21
