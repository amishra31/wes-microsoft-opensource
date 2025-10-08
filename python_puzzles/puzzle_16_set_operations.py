"""
Puzzle 16: Set Operations to Implement
Difficulty: Medium

Description:
This function should return the common elements between two lists,
but it's not implemented yet! Use set operations to find the intersection.

Expected Output:
find_common([1, 2, 3, 4], [3, 4, 5, 6]) should return {3, 4}
find_common(["a", "b", "c"], ["b", "c", "d"]) should return {"b", "c"}
"""

def find_common(list1, list2):
    """Find common elements between two lists"""
    # TODO: Implement using set intersection
    # Hint: set(list1) & set(list2) or set(list1).intersection(set(list2))
    pass

# Test cases
if __name__ == "__main__":
    print(f"find_common([1, 2, 3, 4], [3, 4, 5, 6]) = {find_common([1, 2, 3, 4], [3, 4, 5, 6])}")  # Expected: {3, 4}
    print(f"find_common(['a', 'b', 'c'], ['b', 'c', 'd']) = {find_common(['a', 'b', 'c'], ['b', 'c', 'd'])}")  # Expected: {'b', 'c'}
