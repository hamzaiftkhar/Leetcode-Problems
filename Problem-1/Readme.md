# Two Sum Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example 1:

```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Example 2:

```python
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

## Example 3:

```python
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints:

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## Follow-up:

Can you come up with an algorithm that is less than O(n^2) time complexity?


# Solution 

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The idea was to iterate through pairs of indices in an array and check if the sum of the elements at those indices equals a given target value. If a pair is found, you return the indices.

Here is a summary of your initial approach:

1. Use a nested loop structure to iterate through pairs of indices (i, j) in the array.
2. Check if the sum of elements at indices i and j is equal to the target value.
3. If a pair is found, return the indices i and j.

But later on we implement a beter approch as listed below.

## Approach
<!-- Describe your approach to solving the problem. -->
The step-by-step explanation of the final approach (Python with Hash Map) is descibed below:

- **Initialize a Dictionary (`index_dict`):**
  - Create an empty dictionary to store elements and their corresponding indices.

- **Iterate Through the Array:**
  - Use a `for` loop to iterate through the array, obtaining both the index `i` and the element `num` using `enumerate(arr)`.

- **Calculate Complement:**
  - Calculate the complement by subtracting the current element (`num`) from the target value. Let's call this `complement`.

- **Check if Complement Exists in Dictionary:**
  - Check if the `complement` exists in the dictionary (`complement in index_dict`).
  - If yes, return the indices stored in the dictionary for the complement and the current element.

- **Add Element and Index to Dictionary:**
  - If the complement is not found, add the current element and its index to the dictionary (`index_dict[num] = i`).

- **Return Result:**
  - If no pair is found after iterating through the array, return `None` or an appropriate indicator.

This approach uses a dictionary to keep track of elements encountered so far, allowing for a single pass through the array and efficient identification of pairs that sum up to the target.


## Complexity
- Time complexity: O(n)

- Space complexity: O(n)

This is the approach we implemented in the solution. It is a very efficient approach, with a time complexity of O(n) and a space complexity of O(n).