from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = len(digits)
        digits[x-1] +=1
        while x >=0:
            x-=1
            if x >= 1:
                if digits[x] > 9:
                    digits[x] = 0
                    digits[x-1] +=1
            else:
                if digits[x] > 9:
                    digits[x] = 0
                    digits.insert(0,1)
        return digits