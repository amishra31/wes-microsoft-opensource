"""
Puzzle 14: List Comprehension to Implement
Difficulty: Medium

Description:
This function should create a list of squares of numbers from 1 to n,
but it's not implemented yet! Use list comprehension to implement it.

Expected Output:
get_squares(5) should return [1, 4, 9, 16, 25]
get_squares(3) should return [1, 4, 9]
"""

def get_squares(n):
    """Return a list of squares from 1 to n"""
    # TODO: Implement using list comprehension
    # Hint: [x**2 for x in range(1, n+1)]
    pass

# Test cases
if __name__ == "__main__":
    print(f"get_squares(5) = {get_squares(5)}")  # Expected: [1, 4, 9, 16, 25]
    print(f"get_squares(3) = {get_squares(3)}")  # Expected: [1, 4, 9]
    print(f"get_squares(7) = {get_squares(7)}")  # Expected: [1, 4, 9, 16, 25, 36, 49]
