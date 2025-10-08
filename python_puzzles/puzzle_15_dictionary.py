"""
Puzzle 15: Dictionary Operations Bug
Difficulty: Medium

Description:
This function should count the frequency of each character in a string,
but the increment logic is wrong!

Expected Output:
count_characters("hello") should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}
count_characters("aaa") should return {'a': 3}
"""

def count_characters(text):
    """Count frequency of each character in a string"""
    freq = {}
    for char in text:
        if char in freq:
            freq[char] = 1  # BUG: Should be freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Test cases
if __name__ == "__main__":
    print(f"count_characters('hello') = {count_characters('hello')}")  # Expected: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(f"count_characters('aaa') = {count_characters('aaa')}")  # Expected: {'a': 3}
    print(f"count_characters('python') = {count_characters('python')}")  # Expected: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
