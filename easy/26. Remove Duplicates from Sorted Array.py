from typing import List
class Solution:
 	def removeDuplicates(self, nums: List[int]) -> int:
            nums[:] = sorted(set(nums))
            return len(nums)
s=Solution()
print(s.removeDuplicates([1,1]))