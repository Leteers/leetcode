#My solution:
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicton = {nums.count(x) : x for x in set(nums)}
        return(dicton[1])
    
#Clever one:
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         xor = 0
#         for num in nums:
#             xor ^= num
        
#         return xor