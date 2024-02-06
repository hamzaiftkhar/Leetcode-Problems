class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]*(i+1) for i in range(numRows)]   # 
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
    
# Test cases
test = Solution()
print(test.generate(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(test.generate(1)) # [[1]]
print(test.generate(2)) # [[1],[1,1]]
print(test.generate(3)) # [[1],[1,1],[1,2,1]]

