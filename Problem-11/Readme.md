# **Problem:**
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

- "a->b" if a != b
- "a" if a == b

# **Examples:**
## Example 1:

Input: nums = [0,1,2,4,5,7]

Output: ["0->2","4->5","7"]

Explanation: The ranges are:

[0,2] --> "0->2"

[4,5] --> "4->5"

[7,7] --> "7"

## Example 2:

Input: nums = [0,2,3,4,6,8,9]

Output: ["0","2->4","6","8->9"]

Explanation: The ranges are:

[0,0] --> "0"

[2,4] --> "2->4"

[6,6] --> "6"

[8,9] --> "8->9"
 

# **Constraints:**

- 0 <= nums.length <= 20
- -231 <= nums[i] <= 231 - 1
- All the values of nums are unique.
- nums is sorted in ascending order.

# **Solution:**

## Approach

1. **Check for Empty Input:**
   - If the input array `nums` is empty, return an empty list since there are no ranges to form.

2. **Initialize Variables:**
   - Initialize an empty list `result` to store the final ranges.
   - Initialize `start` and `end` to the first element of `nums`.

3. **Iterate Through the Array:**
   - Loop through the elements of `nums` starting from the second element.
   - Check if the current number is consecutive to the current range (i.e., `num == end + 1`).
     - If true, update `end` to the current number.
     - If not true, the current range has ended, so append the formatted range to the result and update `start` and `end` to the current number.

4. **Handle the Last Range:**
   - After the loop, there might be one last range that needs to be added to the result.
   - Append the last formatted range to the result.

5. **Format Ranges:**
   - The `format_range` method is used to format the ranges as required.
   - If `start` is equal to `end`, return a string representation of `start`.
   - Otherwise, return a formatted string as "start->end".

6. **Return the Result:**
   - Return the list of formatted ranges as the final result.

**Example:**
For the input array `nums = [0, 1, 2, 4, 5, 7]`, the final result would be `["0->2", "4", "5", "7"]`, representing the smallest sorted list of ranges.

This approach efficiently iterates through the input array, identifies consecutive elements, and forms ranges accordingly. The result is a list of formatted ranges meeting the specified conditions.

## Complexity
### Time Complexity:
The time complexity of the provided code is O(N), where N is the number of elements in the input array `nums`. This is because the code iterates through each element of the array exactly once in a single pass. The loop that iterates through the array has a linear time complexity, and the additional operations inside the loop are constant time.

### Space Complexity:
The space complexity of the code is O(1), which means it is constant space. The primary space usage is for the `result` list, which stores the formatted ranges. However, the size of the `result` list is directly proportional to the number of ranges in the input array, and it does not depend on the total number of elements in the array. Therefore, the space complexity is constant, and it does not grow with the size of the input array. Other variables used in the code, such as `start`, `end`, and loop variables, also use constant space.
