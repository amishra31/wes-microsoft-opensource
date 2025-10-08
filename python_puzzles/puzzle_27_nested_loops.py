"""
Puzzle 27: Nested Loop Logic Error
Difficulty: Medium

Description:
This function should create a multiplication table (list of lists),
but the inner loop variable is wrong!

Expected Output:
multiplication_table(3) should return [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
multiplication_table(2) should return [[1, 2], [2, 4]]
"""

def multiplication_table(n):
    """Create an n x n multiplication table"""
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * i)  # BUG: Should be i * j, not i * i
        table.append(row)
    return table

# Test cases
if __name__ == "__main__":
    print(f"multiplication_table(3) = {multiplication_table(3)}")  # Expected: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    print(f"multiplication_table(2) = {multiplication_table(2)}")  # Expected: [[1, 2], [2, 4]]
    print(f"multiplication_table(4) = {multiplication_table(4)}")  # Expected: [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
