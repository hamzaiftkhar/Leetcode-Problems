class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

            prev_row = [1]

        for i in range(1, rowIndex + 1):
            current_row = [1]  # First element is always 1

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)  # Last element is always 1
            prev_row = current_row

        return prev_row
        
# test
s = Solution()
print(s.getRow(3))  # [1,3,3,1]
print(s.getRow(0))  # [1]
print(s.getRow(1))  # [1,1]