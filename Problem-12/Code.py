class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate the expected sum of the first n natural numbers
        n = len(nums)
        expected_sum = n * (n + 1) // 2
    
        # Calculate the actual sum of the elements in the array
        actual_sum = sum(nums)
    
        # The missing number is the difference between the expected and actual sums
        return expected_sum - actual_sum

#test 
s = Solution()
print(s.missingNumber([3,0,1])) #2
print(s.missingNumber([9,6,4,2,3,5,7,0,1])) #8
print(s.missingNumber([0])) #1
