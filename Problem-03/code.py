class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # removing the given number from the list
        # num_copy = nums[:]
        while val in nums:
            nums.remove(val)
        print(len(nums), nums)
    
if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 5, 3, 6, 7, 3, 8]
    val = 3
    obj = Solution()
    obj.removeElement(nums, val)
