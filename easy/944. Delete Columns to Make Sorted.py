#https://leetcode.com/problems/delete-columns-to-make-sorted
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        wrong = set()
        for i in range(len(strs[0])):
            prev = 0
            for j,st in enumerate(strs):
                if ord(st[i]) < prev:
                    wrong.add(j)
                else:
                    prev = ord(st[i])
        return len(wrong)
    
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    res += 1
                    break

        return res

if __name__ == '__main__':
    s = Solution()
    # print(s.minDeletionSize(strs = ["cba","daf","ghi"]))#1
    print(s.minDeletionSize(["zyx","wvu","tsr"]))#3