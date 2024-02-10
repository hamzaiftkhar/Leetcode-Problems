class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = [0]  # Initialize prefix sum with 0 at the beginning
        for num in nums:
            # Calculate the cumulative sum and store it in the prefix_sum array
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Calculate the sum of elements between indices left and right (inclusive)
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left, right)

# test
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3