''' 
# Two Sum

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
```

You can save this content in a file named `readme.md` and use it for your project or documentation.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}  # Dictionary to store the indices of elements

        for i, num in enumerate(nums):
            complement = target - num

        # Check if the complement exists in the dictionary
            if complement in index_dict:
                return index_dict[complement], i

        # Add the current element and its index to the dictionary
            index_dict[num] = i

    # If no such pair is found
        return None
    
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# Link: https://leetcode.com/problems/two-sum/
