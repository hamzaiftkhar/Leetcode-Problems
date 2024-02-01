# Solution-1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str, digits))) + 1
        return list(map(int, str(num)))
    

# Solution-2 (Recursive)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            else:
                digits[-1] = 0
                digits[:-1] = self.plusOne(digits[:-1])
                return digits
            
        else:
            digits[-1] += 1
            return digits
        
