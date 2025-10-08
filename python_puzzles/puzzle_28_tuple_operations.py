"""
Puzzle 28: Tuple Operations Bug
Difficulty: Medium

Description:
This function should swap two values and return them as a tuple,
but the return statement is incorrect!

Expected Output:
swap_values(5, 10) should return (10, 5)
swap_values("a", "b") should return ("b", "a")
"""

def swap_values(a, b):
    """Swap two values and return as tuple"""
    temp = a
    a = b
    b = temp
    return (a, a)  # BUG: Should return (a, b) not (a, a)

# Test cases
if __name__ == "__main__":
    print(f"swap_values(5, 10) = {swap_values(5, 10)}")  # Expected: (10, 5)
    print(f"swap_values('a', 'b') = {swap_values('a', 'b')}")  # Expected: ('b', 'a')
    print(f"swap_values(100, 200) = {swap_values(100, 200)}")  # Expected: (200, 100)
