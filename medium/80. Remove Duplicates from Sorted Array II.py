from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         index = -1
#         nums_count = {nums.count(num): num  for num in set(nums)}
#         print(nums_count)
#         for k in nums_count.keys():
#             index+=k
#             if k>2:
#                 for i in range(k-2):
#                     nums.pop(index)
#                     index-=1
            # for i in range(nums_count[k]):                
            #     if i > 1:
            #         nums.pop(index)
            #     index += 1
        # return len(nums)
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k  
    
nums = [0,0,1,1,1,1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2,3,3]
s = Solution()
print(s.removeDuplicates(nums))
print(nums)