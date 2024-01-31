def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # If the target is not found, return the index where it would be inserted

# Examples
nums1, target1 = [1, 3, 5, 6], 5
print(search_insert(nums1, target1))  # Output: 2

nums2, target2 = [1, 3, 5, 6], 2
print(search_insert(nums2, target2))  # Output: 1

nums3, target3 = [1, 3, 5, 6], 7
print(search_insert(nums3, target3))  # Output: 4


# Solution 2 

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)

        if target < nums[0]:
            return 0

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] > target:
                end = mid - 1
                if end >= 0:
                    if nums[end] < target:
                         return end + 1
                else:
                     return 0

            elif nums[mid] < target:
                start = mid + 1
                if start < len(nums):
                    if nums[start] > target:
                        return start
                else:
                    return len(nums)
            else:
                return mid
            

if __name__ == "__main__":
    obj = Solution()
    print(obj.searchInsert([1,3,5,6], 5))
    print(obj.searchInsert([1,3,5,6], 2))
    print(obj.searchInsert([1,3,5,6], 7))
    
    