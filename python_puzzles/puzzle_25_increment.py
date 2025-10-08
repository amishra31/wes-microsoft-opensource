"""
Puzzle 25: Increment Operator Bug
Difficulty: Easy

Description:
This function should count from 0 to n-1 and return the count,
but the increment is wrong!

Expected Output:
count_to(5) should return 5
count_to(10) should return 10
"""

def count_to(n):
    """Count from 0 to n-1 and return final count"""
    count = 0
    for i in range(n):
        count = count - 1  # BUG: Should be count + 1
    return count

# Test cases
if __name__ == "__main__":
    print(f"count_to(5) = {count_to(5)}")  # Expected: 5
    print(f"count_to(10) = {count_to(10)}")  # Expected: 10
    print(f"count_to(3) = {count_to(3)}")  # Expected: 3
