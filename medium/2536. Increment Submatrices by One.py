from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        for i in range(n):
            l = [[0] * n for i in range(n)]
        for q in queries:
            for i in range(q[0],q[2]+1):
                for j in range(q[1],q[3]+1):
                    l[i][j] += 1
        return l
    
if __name__ == '__main__':
    s = Solution()
    print(s.rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]))