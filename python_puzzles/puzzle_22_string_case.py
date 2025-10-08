"""
Puzzle 22: String Case Conversion Bug
Difficulty: Easy

Description:
This function should convert a string to title case (first letter capitalized),
but it's using the wrong method!

Expected Output:
make_title("hello world") should return "Hello World"
make_title("python programming") should return "Python Programming"
"""

def make_title(text):
    """Convert string to title case"""
    result = text.lower()  # BUG: Should use title() instead of lower()
    return result

# Test cases
if __name__ == "__main__":
    print(f"make_title('hello world') = {make_title('hello world')}")  # Expected: Hello World
    print(f"make_title('python programming') = {make_title('python programming')}")  # Expected: Python Programming
    print(f"make_title('data science') = {make_title('data science')}")  # Expected: Data Science
