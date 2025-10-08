"""
Puzzle 7: List Manipulation Bug
Difficulty: Medium

Description:
This function should add a new item to the end of a list,
but it's using the wrong method!

Expected Output:
add_to_list([1, 2, 3], 4) should return [1, 2, 3, 4]
add_to_list(["a", "b"], "c") should return ["a", "b", "c"]
"""

def add_to_list(items, new_item):
    """Add an item to the end of a list"""
    items.remove(new_item)  # BUG: remove() is wrong, should use append()
    return items

# Test cases
if __name__ == "__main__":
    print(f"add_to_list([1, 2, 3], 4) = {add_to_list([1, 2, 3], 4)}")  # Expected: [1, 2, 3, 4]
    print(f"add_to_list(['a', 'b'], 'c') = {add_to_list(['a', 'b'], 'c')}")  # Expected: ['a', 'b', 'c']
