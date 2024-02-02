# Pascal's Triangle

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

Example 2:

```
Input: numRows = 1
Output: [[1]]
```

Constraints:

- 1 <= numRows <= 30

# Solution

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Pascal's Triangle is a way of representing combinations or binomial coefficients. Starting with the number 1 in the first row, each subsequent row is built by adding the two adjacent numbers from the row above. The resulting triangular structure holds valuable information about combinations, and each number signifies the ways of selecting elements from a set.

First thoughts of solution include: 

- Formation of Triangle.
- Iterate through each row, starting from the third row.
- Update each element by adding the adjacent elements in the row above.
- Return the completed Pascal's Triangle.

## Approach
<!-- Describe your approach to solving the problem. -->

1. **Initialization:**
   - The algorithm begins by creating an empty 2D list named `pascal`, which will represent Pascal's Triangle.
   - Each row is initialized with `i+1` elements, where `i` is the row index, and all elements are set to 1.
   - This step effectively sets up the initial structure of the triangle with all 1s.

```python
pascal = [[1] * (i + 1) for i in range(numRows)]
```

2. **Iterative Update:**
   - The algorithm then uses nested loops to iterate through each row (`i`) and each element in that row (`j`).
   - The outer loop (`for i in range(numRows)`) iterates over each row of the triangle.
   - The inner loop (`for j in range(1, i)`) iterates over each element in the current row, excluding the first and last elements.

```python
for i in range(numRows):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
```

3. **Element Update Formula:**
   - The code updates each element `pascal[i][j]` by summing the corresponding elements from the previous row (`pascal[i-1][j-1]` and `pascal[i-1][j]`).
   - This update follows the principle of Pascal's Triangle, where each number is the sum of the two numbers directly above it in the previous row.

4. **Result:**
   - Finally, the completed Pascal's Triangle (`pascal`) is returned.


## Complexity
- Time complexity:  O(numRows^2)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(numRows^2)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
