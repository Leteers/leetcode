from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dicton = {x: nums.count(x) for x in set(nums)}
        maxim = max(dicton.values())
        res = 0
        for i in dicton.values():
            if i == maxim:
                res += i
        return res