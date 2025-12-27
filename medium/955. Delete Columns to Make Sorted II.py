#https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/
from typing import List
from collections import defaultdict

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        is_lexo = lambda x,j: [True if x[i][j:j+1]<=x[i+1][j:j+1] else False for i in range(len(x) - 1)]
        def are_duplicates(x,j):
            res = []
            dup_indicies = []
            for i in range(len(x)-1):
                if x[i][j:j+1]<x[i+1][j:j+1]:
                    res.append(True)
                elif x[i][j:j+1]==x[i+1][j:j+1]:
                    dup_indicies.append(i)
                    res.append('Duplicate')
                else:
                    res.append(False)
            print(dup_indicies)
            print(res)
            for id in dup_indicies:
                res.pop(id)
            if all(res):
                return(True)
            else:
                return(False)
        
        cnt = 0
        true_cnt = 0

        while ((not(all(is_lexo(strs,cnt)))) or are_duplicates(strs,cnt)) and cnt < len(strs[0]):
            if are_duplicates(strs,cnt):
                cnt +=1
            else:
                true_cnt+=1
                cnt+=1
        return true_cnt

if __name__ == '__main__':
    s = Solution()
    print(s.minDeletionSize(["xc","yb","za"]))#0

    print(s.minDeletionSize(["xga","xfb","yfa"]))#1