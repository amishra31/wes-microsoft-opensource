"""
Puzzle 5: String Concatenation Bug
Difficulty: Easy

Description:
This function should concatenate (join) two strings with a space,
but there's a typo in the variable name!

Expected Output:
join_strings("Hello", "World") should return "Hello World"
join_strings("Python", "Programming") should return "Python Programming"
"""

def join_strings(str1, str2):
    """Join two strings with a space"""
    result = str1 + " " + str3  # BUG: str3 doesn't exist, should be str2
    return result

# Test cases
if __name__ == "__main__":
    print(f"join_strings('Hello', 'World') = {join_strings('Hello', 'World')}")  # Expected: Hello World
    print(f"join_strings('Python', 'Programming') = {join_strings('Python', 'Programming')}")  # Expected: Python Programming
