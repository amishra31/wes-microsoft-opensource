"""
Puzzle 23: List Indexing Error
Difficulty: Easy

Description:
This function should return the last element of a list,
but the index is wrong!

Expected Output:
get_last_element([1, 2, 3, 4, 5]) should return 5
get_last_element(["a", "b", "c"]) should return "c"
"""

def get_last_element(items):
    """Return the last element of a list"""
    return items[0]  # BUG: Should use index -1 for last element

# Test cases
if __name__ == "__main__":
    print(f"get_last_element([1, 2, 3, 4, 5]) = {get_last_element([1, 2, 3, 4, 5])}")  # Expected: 5
    print(f"get_last_element(['a', 'b', 'c']) = {get_last_element(['a', 'b', 'c'])}")  # Expected: c
    print(f"get_last_element([10, 20, 30]) = {get_last_element([10, 20, 30])}")  # Expected: 30
