"""
Puzzle 13: String Formatting Bug
Difficulty: Easy

Description:
This function should create a greeting message,
but the f-string formatting is incomplete!

Expected Output:
create_greeting("Alice") should return "Hello, Alice! Welcome!"
create_greeting("Bob") should return "Hello, Bob! Welcome!"
"""

def create_greeting(name):
    """Create a greeting message"""
    message = f"Hello, {name}! Welcome"  # BUG: Missing exclamation mark at the end
    return message

# Test cases
if __name__ == "__main__":
    print(f"create_greeting('Alice') = {create_greeting('Alice')}")  # Expected: Hello, Alice! Welcome!
    print(f"create_greeting('Bob') = {create_greeting('Bob')}")  # Expected: Hello, Bob! Welcome!
