"""
Puzzle 30: Sorting Algorithm Bug
Difficulty: Hard

Description:
This function implements bubble sort to sort a list in ascending order,
but there's a logic error in the comparison!

Expected Output:
bubble_sort([64, 34, 25, 12, 22]) should return [12, 22, 25, 34, 64]
bubble_sort([5, 1, 4, 2, 8]) should return [1, 2, 4, 5, 8]
"""

def bubble_sort(arr):
    """Sort array using bubble sort algorithm"""
    n = len(arr)
    # Make a copy to avoid modifying original
    arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # BUG: Should be > for ascending order, not <
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Test cases
if __name__ == "__main__":
    print(f"bubble_sort([64, 34, 25, 12, 22]) = {bubble_sort([64, 34, 25, 12, 22])}")  # Expected: [12, 22, 25, 34, 64]
    print(f"bubble_sort([5, 1, 4, 2, 8]) = {bubble_sort([5, 1, 4, 2, 8])}")  # Expected: [1, 2, 4, 5, 8]
    print(f"bubble_sort([3, 0, -1, 8, 7]) = {bubble_sort([3, 0, -1, 8, 7])}")  # Expected: [-1, 0, 3, 7, 8]
