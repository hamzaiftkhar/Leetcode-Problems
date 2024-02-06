class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
    
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
    
        return candidate
        
        # test code
s = Solution()
print(s.majorityElement([3,2,3])) # 3
print(s.majorityElement([2,2,1,1,1,2,2])) # 2

