from typing import List
class Solution:
    def isHappy(self, n: int) -> bool:
        global hset
        hset=set()
        return(self.cnt(n))
        
    def cnt(self,n):
        n = sum([int(x) ** 2 for x in str(n)])
        if n in hset: return False
        elif(n==1): return(True)
        else: 
            hset.add(n)
            return(self.cnt(n))

a=Solution()
print(a.isHappy(13))