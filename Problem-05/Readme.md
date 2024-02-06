# Plus One

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Examples

### Example 1:

**Input:**
```python
digits = [1,2,3]
```
**Output:**
```python
[1,2,4]
```
**Explanation:**
The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

### Example 2:

**Input:**
```python
digits = [4,3,2,1]
```
**Output:**
```python
[4,3,2,2]
```
**Explanation:**
The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus, the result should be [4,3,2,2].

### Example 3:

**Input:**
```python
digits = [9]
```
**Output:**
```python
[1,0]
```
**Explanation:**
The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be [1,0].

## Constraints

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- `digits` does not contain any leading 0's.


# Solution
## Intuition
The first thoughts on solving this problem involve recognizing that incrementing a large integer by one involves adjusting the digits, considering potential carry overs.

## Approach
1. **Convert array to an integer:**
   - The code concatenates the digits in the array into a single integer by joining them as strings and converting them to an integer.
   ```python
   num = int(''.join(map(str, digits)))
   ```

2. **Increment the integer:**
   - Add 1 to the obtained integer.
   ```python
   num = num + 1
   ```

3. **Convert back to array of digits:**
   - Convert the incremented integer back to an array of digits by converting it to a string and then mapping each character back to an integer.
   ```python
   return list(map(int, str(num)))
   ```

Now, let's provide a line-by-line explanation of the code:

```python
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # Convert array to an integer
    num = int(''.join(map(str, digits)))

    # Increment the integer
    num = num + 1

    # Convert back to array of digits
    return list(map(int, str(num)))
```

- The function `plusOne` takes an array of digits as input.

- `map(str, digits)` converts each digit in the array to a string.

- `''.join(...)` concatenates these strings into a single string representing the integer.

- `int(...)` converts the string back to an integer.

- `num = num + 1` increments the integer by 1.

- `str(num)` converts the incremented integer back to a string.

- `map(int, ...)` maps each character of the string back to an integer.

- `list(...)` converts the result to a list of integers.

- The final list of integers is returned as the result.

## Complexity
- Time complexity: O(n), where n is the length of the input array `digits`. The algorithm iterates through the array once.
  
- Space complexity: O(1), as the space used is constant, independent of the input size. The array `digits` is modified in place, and no additional data structures are used.
