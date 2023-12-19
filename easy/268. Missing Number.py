from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # lst=list(range(0, len(nums)+1))
        # res = [x for x in nums + lst if x not in lst or x not in nums]
        # return(res[0])
        seq = range(len(nums) + 1)
        s = sum(seq)
        result=s-sum(nums)
        return(result)

a=Solution()
print(a.missingNumber([1,2]))