"""
Puzzle 26: String Split Method Bug
Difficulty: Easy

Description:
This function should split a sentence into words,
but it's using the wrong delimiter!

Expected Output:
split_words("hello world python") should return ["hello", "world", "python"]
split_words("one two three") should return ["one", "two", "three"]
"""

def split_words(sentence):
    """Split a sentence into words"""
    words = sentence.split(",")  # BUG: Should split by space " " not comma
    return words

# Test cases
if __name__ == "__main__":
    print(f"split_words('hello world python') = {split_words('hello world python')}")  # Expected: ['hello', 'world', 'python']
    print(f"split_words('one two three') = {split_words('one two three')}")  # Expected: ['one', 'two', 'three']
    print(f"split_words('foo bar') = {split_words('foo bar')}")  # Expected: ['foo', 'bar']
