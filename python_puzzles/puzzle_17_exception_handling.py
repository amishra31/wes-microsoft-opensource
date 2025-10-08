"""
Puzzle 17: Exception Handling Bug
Difficulty: Medium

Description:
This function should convert a string to an integer safely,
but the exception handling is incomplete!

Expected Output:
safe_int_convert("123") should return 123
safe_int_convert("abc") should return None
"""

def safe_int_convert(text):
    """Safely convert a string to integer"""
    try:
        result = int(text)
        return result
    # BUG: No except clause to handle ValueError
    
# Test cases
if __name__ == "__main__":
    print(f"safe_int_convert('123') = {safe_int_convert('123')}")  # Expected: 123
    print(f"safe_int_convert('456') = {safe_int_convert('456')}")  # Expected: 456
    print(f"safe_int_convert('abc') = {safe_int_convert('abc')}")  # Expected: None
