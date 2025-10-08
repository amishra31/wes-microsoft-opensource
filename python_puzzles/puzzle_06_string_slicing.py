"""
Puzzle 6: String Slicing Error
Difficulty: Medium

Description:
This function should return the first 3 characters of a string,
but the slicing is incorrect!

Expected Output:
get_first_three("Python") should return "Pyt"
get_first_three("Hello") should return "Hel"
"""

def get_first_three(text):
    """Get the first three characters of a string"""
    result = text[0:2]  # BUG: Should be [0:3] to get 3 characters
    return result

# Test cases
if __name__ == "__main__":
    print(f"get_first_three('Python') = {get_first_three('Python')}")  # Expected: Pyt
    print(f"get_first_three('Hello') = {get_first_three('Hello')}")  # Expected: Hel
    print(f"get_first_three('Programming') = {get_first_three('Programming')}")  # Expected: Pro
