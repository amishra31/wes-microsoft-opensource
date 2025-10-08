"""
Puzzle 12: Type Conversion Error
Difficulty: Easy

Description:
This function should calculate the sum of string numbers,
but it's concatenating them instead of adding! Convert strings to integers.

Expected Output:
sum_string_numbers("10", "20") should return 30
sum_string_numbers("5", "15") should return 20
"""

def sum_string_numbers(str_num1, str_num2):
    """Add two numbers provided as strings"""
    result = str_num1 + str_num2  # BUG: Concatenates strings instead of adding numbers
    return result

# Test cases
if __name__ == "__main__":
    print(f"sum_string_numbers('10', '20') = {sum_string_numbers('10', '20')}")  # Expected: 30
    print(f"sum_string_numbers('5', '15') = {sum_string_numbers('5', '15')}")  # Expected: 20
    print(f"sum_string_numbers('100', '50') = {sum_string_numbers('100', '50')}")  # Expected: 150
