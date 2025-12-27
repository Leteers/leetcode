
class Solution:
    def longestConsecutive(self, nums: list) -> int:
        nums = list(sorted(set(nums)))
        x = 1
        max_len = 0
        cur_len = 1
        while x < len(nums):
            
            if nums[x]-nums[x-1] == 1:
                cur_len += 1
            else:
                if max_len < cur_len:
                    max_len = cur_len
                cur_len = 1
            x+=1
        else:
            if len(nums) ==0:
                return max_len
            if cur_len > max_len:
                max_len = cur_len

        return max_len

s = Solution()

print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))