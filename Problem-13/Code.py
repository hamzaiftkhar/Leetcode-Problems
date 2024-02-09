class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroPointer = 0

        # Iterate through the array
        for nonZeroPointer in range(len(nums)):
            # If the current element is non-zero
            if nums[nonZeroPointer] != 0:
                # Swap the non-zero element with the element at zeroPointer
                nums[zeroPointer], nums[nonZeroPointer] = nums[nonZeroPointer], nums[zeroPointer]
                zeroPointer += 1

#test 
nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)
