from typing import List
class Solution:
 	def majorityElement(self, nums: List[int]) -> int:
            numsxd=nums.copy()
            length=len(nums)
            nums[:] = sorted(set(nums))
            for num in nums:
                if(numsxd.count(num)>=length/2):
                    return(num)
s=Solution()
print(s.majorityElement([3,2,3]))