"""
Puzzle 10: Function Return Value Bug
Difficulty: Easy

Description:
This function should return the maximum of two numbers,
but it's returning the minimum instead!

Expected Output:
get_max(10, 20) should return 20
get_max(50, 30) should return 50
"""

def get_max(a, b):
    """Return the maximum of two numbers"""
    if a > b:
        return b  # BUG: Should return a
    else:
        return a  # BUG: Should return b

# Test cases
if __name__ == "__main__":
    print(f"get_max(10, 20) = {get_max(10, 20)}")  # Expected: 20
    print(f"get_max(50, 30) = {get_max(50, 30)}")  # Expected: 50
    print(f"get_max(100, 100) = {get_max(100, 100)}")  # Expected: 100
