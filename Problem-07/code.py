class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Merge both arrays and assign the result to nums1
        nums1[:m + n] = sorted(nums1[:m] + nums2[:n])
        return nums1
    
# Test
s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # [1, 2, 2, 3, 5, 6]
print(s.merge([1], 1, [], 0)) # [1]
print(s.merge([0], 0, [1], 1)) # [1]
 