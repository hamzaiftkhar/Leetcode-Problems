class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        start = end = nums[0]
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                result.append(self.format_range(start, end))
                start = end = num
        result.append(self.format_range(start, end))
        return result

    def format_range(self, start, end):
        if start == end:
            return str(start)
        else:
            return "{}->{}".format(start, end)

s = Solution()
nums = [0, 1, 2, 4, 5, 7]
s.summaryRanges(nums)