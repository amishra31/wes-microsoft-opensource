"""
Puzzle 8: Loop Logic Error
Difficulty: Medium

Description:
This function should count how many even numbers are in a list,
but the condition is wrong!

Expected Output:
count_evens([1, 2, 3, 4, 5, 6]) should return 3
count_evens([2, 4, 6, 8]) should return 4
"""

def count_evens(numbers):
    """Count how many even numbers are in the list"""
    count = 0
    for num in numbers:
        if num % 2 == 1:  # BUG: This checks for odd, should be == 0 for even
            count += 1
    return count

# Test cases
if __name__ == "__main__":
    print(f"count_evens([1, 2, 3, 4, 5, 6]) = {count_evens([1, 2, 3, 4, 5, 6])}")  # Expected: 3
    print(f"count_evens([2, 4, 6, 8]) = {count_evens([2, 4, 6, 8])}")  # Expected: 4
    print(f"count_evens([1, 3, 5, 7]) = {count_evens([1, 3, 5, 7])}")  # Expected: 0
