from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1.pop()
        for item in nums2:
            nums1.append(item)
        nums1.sort()

a=Solution()
a.merge([1,2,3],1,[1,2],2)