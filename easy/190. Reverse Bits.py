class Solution:
    def reverseBits(self, n: int) -> int:
         return(int(str(n)[::-1],2))
    
a=Solution()
print(a.reverseBits(000010100101000001111010011100))#XDSXDXDXDX