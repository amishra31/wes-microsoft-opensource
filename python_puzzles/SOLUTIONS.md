# Solutions to Python Coding Puzzles

This file contains solutions and explanations for all 30 puzzles.

---

## Puzzle 1: Basic Addition Bug
**Problem**: Wrong operator used (subtraction instead of addition)

**Solution**:
```python
def add_numbers(a, b):
    result = a + b  # Changed from a - b
    return result
```

**Explanation**: The function was using the subtraction operator (-) instead of the addition operator (+).

---

## Puzzle 2: Subtraction Logic Error
**Problem**: Parameters in wrong order

**Solution**:
```python
def subtract_numbers(a, b):
    result = a - b  # Changed from b - a
    return result
```

**Explanation**: The function was subtracting in reverse order. To subtract b from a, use a - b.

---

## Puzzle 3: Multiplication with String
**Problem**: String needs to be converted to integer

**Solution**:
```python
def multiply_numbers(a, b):
    result = a * int(b)  # Convert b to integer
    return result
```

**Explanation**: The parameter b is a string and must be converted to an integer before multiplication.

---

## Puzzle 4: Division by Zero Handling
**Problem**: No error handling for division by zero

**Solution**:
```python
def safe_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    result = a / b
    return result
```

**Explanation**: Check if the divisor is zero before performing division to prevent runtime errors.

---

## Puzzle 5: String Concatenation Bug
**Problem**: Variable name typo (str3 instead of str2)

**Solution**:
```python
def join_strings(str1, str2):
    result = str1 + " " + str2  # Changed str3 to str2
    return result
```

**Explanation**: The variable str3 doesn't exist - it should be str2.

---

## Puzzle 6: String Slicing Error
**Problem**: Slice index is wrong

**Solution**:
```python
def get_first_three(text):
    result = text[0:3]  # Changed from [0:2]
    return result
```

**Explanation**: In Python slicing, [0:3] gets indices 0, 1, and 2 (three characters). [0:2] only gets two characters.

---

## Puzzle 7: List Manipulation Bug
**Problem**: Using remove() instead of append()

**Solution**:
```python
def add_to_list(items, new_item):
    items.append(new_item)  # Changed from remove()
    return items
```

**Explanation**: The append() method adds an item to the end of a list, while remove() deletes an item.

---

## Puzzle 8: Loop Logic Error
**Problem**: Checking for odd numbers instead of even

**Solution**:
```python
def count_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:  # Changed from == 1
            count += 1
    return count
```

**Explanation**: A number is even if num % 2 == 0 (remainder is 0), not == 1.

---

## Puzzle 9: Conditional Statement Bug
**Problem**: Return values are swapped

**Solution**:
```python
def check_number(num):
    if num < 0:
        return "Negative"  # Changed from "Positive"
    elif num > 0:
        return "Positive"  # Changed from "Negative"
    else:
        return "Zero"
```

**Explanation**: The return values were backwards - negative numbers should return "Negative" and positive should return "Positive".

---

## Puzzle 10: Function Return Value Bug
**Problem**: Returning minimum instead of maximum

**Solution**:
```python
def get_max(a, b):
    if a > b:
        return a  # Changed from b
    else:
        return b  # Changed from a
```

**Explanation**: When a is greater, return a (not b). When b is greater, return b (not a).

---

## Puzzle 11: Variable Scope Issue
**Problem**: Variable defined inside if block but used outside

**Solution**:
```python
def calculate_area(length, width):
    area = 0  # Initialize before if block
    if length > 0 and width > 0:
        area = length * width
    return area
```

**Explanation**: Initialize the variable before the if block so it's always defined when the return statement executes.

---

## Puzzle 12: Type Conversion Error
**Problem**: Concatenating strings instead of adding numbers

**Solution**:
```python
def sum_string_numbers(str_num1, str_num2):
    result = int(str_num1) + int(str_num2)  # Convert to int
    return result
```

**Explanation**: Convert both strings to integers before adding them together.

---

## Puzzle 13: String Formatting Bug
**Problem**: Missing exclamation mark at the end

**Solution**:
```python
def create_greeting(name):
    message = f"Hello, {name}! Welcome!"  # Added ! at the end
    return message
```

**Explanation**: The expected output has an exclamation mark after "Welcome" - add it to the string.

---

## Puzzle 14: List Comprehension to Implement
**Problem**: Function not implemented

**Solution**:
```python
def get_squares(n):
    return [x**2 for x in range(1, n+1)]
```

**Explanation**: List comprehension creates a list by applying an expression (x**2) to each element in a range.

---

## Puzzle 15: Dictionary Operations Bug
**Problem**: Not incrementing the count, just setting to 1

**Solution**:
```python
def count_characters(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1  # Changed from = 1
        else:
            freq[char] = 1
    return freq
```

**Explanation**: When a character already exists in the dictionary, increment its count (+=) instead of resetting to 1.

---

## Puzzle 16: Set Operations to Implement
**Problem**: Function not implemented

**Solution**:
```python
def find_common(list1, list2):
    return set(list1) & set(list2)
    # Or: return set(list1).intersection(set(list2))
```

**Explanation**: Convert lists to sets and use the & operator (or intersection method) to find common elements.

---

## Puzzle 17: Exception Handling Bug
**Problem**: Missing except clause

**Solution**:
```python
def safe_int_convert(text):
    try:
        result = int(text)
        return result
    except ValueError:
        return None
```

**Explanation**: Add an except clause to catch ValueError exceptions when conversion fails.

---

## Puzzle 18: Logical Operators Error
**Problem**: Using OR instead of AND

**Solution**:
```python
def is_between_10_and_20(num):
    return num >= 10 and num <= 20  # Changed or to and
```

**Explanation**: For a number to be between 10 and 20, BOTH conditions must be true (use AND), not just one (OR).

---

## Puzzle 19: String Methods Bug
**Problem**: Using lower() instead of upper()

**Solution**:
```python
def to_uppercase(text):
    result = text.upper()  # Changed from lower()
    return result
```

**Explanation**: The upper() method converts to uppercase, while lower() converts to lowercase.

---

## Puzzle 20: Mathematical Formula Implementation
**Problem**: Function not implemented

**Solution**:
```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

**Explanation**: Average is calculated by dividing the sum of all numbers by the count of numbers.

---

## Puzzle 21: Modulo Operator Bug
**Problem**: Wrong comparison for even numbers

**Solution**:
```python
def is_even(num):
    return num % 2 == 0  # Changed from == 1
```

**Explanation**: A number is even if the remainder when divided by 2 is 0, not 1.

---

## Puzzle 22: String Case Conversion Bug
**Problem**: Using lower() instead of title()

**Solution**:
```python
def make_title(text):
    result = text.title()  # Changed from lower()
    return result
```

**Explanation**: The title() method converts to title case (first letter of each word capitalized), while lower() converts all to lowercase.

---

## Puzzle 23: List Indexing Error
**Problem**: Using index 0 instead of -1 for last element

**Solution**:
```python
def get_last_element(items):
    return items[-1]  # Changed from items[0]
```

**Explanation**: In Python, index -1 refers to the last element, while index 0 refers to the first element.

---

## Puzzle 24: Boolean Logic Bug
**Problem**: Using < instead of > for positive check

**Solution**:
```python
def is_positive(num):
    return num > 0  # Changed from num < 0
```

**Explanation**: A number is positive if it's greater than 0, not less than 0.

---

## Puzzle 25: Increment Operator Bug
**Problem**: Decrementing instead of incrementing

**Solution**:
```python
def count_to(n):
    count = 0
    for i in range(n):
        count = count + 1  # Changed from count - 1
    return count
```

**Explanation**: To count up, we need to add 1, not subtract 1.

---

## Puzzle 26: String Split Method Bug
**Problem**: Splitting by comma instead of space

**Solution**:
```python
def split_words(sentence):
    words = sentence.split(" ")  # Changed from ","
    return words
```

**Explanation**: To split a sentence into words, we need to split by space " ", not comma.

---

## Puzzle 27: Nested Loop Logic Error
**Problem**: Using i * i instead of i * j in nested loop

**Solution**:
```python
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)  # Changed from i * i
        table.append(row)
    return table
```

**Explanation**: For a multiplication table, we need to multiply the row number (i) by the column number (j), not i by itself.

---

## Puzzle 28: Tuple Operations Bug
**Problem**: Returning (a, a) instead of (a, b)

**Solution**:
```python
def swap_values(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)  # Changed from (a, a)
```

**Explanation**: After swapping, we need to return both swapped values (a, b), not the same value twice.

---

## Puzzle 29: Recursive Function Implementation
**Problem**: Function not implemented

**Solution**:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

**Explanation**: Factorial is defined recursively: factorial(0) = 1 (base case), and factorial(n) = n * factorial(n-1) for n > 0.

---

## Puzzle 30: Sorting Algorithm Bug
**Problem**: Using < instead of > for ascending sort

**Solution**:
```python
def bubble_sort(arr):
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Changed from <
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
```

**Explanation**: For ascending order (smallest to largest), we swap if the current element is greater than the next element. Using < would give descending order.

---

## General Debugging Tips

1. **Read error messages**: They tell you what went wrong and where
2. **Check variable names**: Typos are common bugs
3. **Verify operators**: Make sure you're using +, -, *, / correctly
4. **Test edge cases**: Test with different inputs including 0, negative numbers, empty strings
5. **Use type conversion**: Convert between int, str, float as needed
6. **Initialize variables**: Declare variables before using them
7. **Check logic**: Make sure conditions and loops do what you intend
8. **Handle exceptions**: Use try-except for operations that might fail

Happy coding! 🎉
