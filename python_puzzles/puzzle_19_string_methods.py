"""
Puzzle 19: String Methods Bug
Difficulty: Easy

Description:
This function should convert a string to uppercase,
but it's using the wrong method!

Expected Output:
to_uppercase("hello") should return "HELLO"
to_uppercase("python") should return "PYTHON"
"""

def to_uppercase(text):
    """Convert a string to uppercase"""
    result = text.lower()  # BUG: Should use upper() not lower()
    return result

# Test cases
if __name__ == "__main__":
    print(f"to_uppercase('hello') = {to_uppercase('hello')}")  # Expected: HELLO
    print(f"to_uppercase('python') = {to_uppercase('python')}")  # Expected: PYTHON
    print(f"to_uppercase('world') = {to_uppercase('world')}")  # Expected: WORLD
