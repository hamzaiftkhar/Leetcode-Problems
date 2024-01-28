


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
