
class Solution:
    y=20
    x=-20
    def isPowerOfThree(self, n: int) -> bool:
        return(self.binarySearch(self.x,self.y,n))
    def searchBetween(self,min,max):
        if int(max)-int(min)==1:
            return(False)
        else: 
            return(int(max-(max-min)/2))
    def binarySearch(self,min: int,max: int,n):
        if type(self.searchBetween(min,max))==bool:
            return(False)
        elif (3**self.searchBetween(min,max))>n:
            max=self.searchBetween(min,max)
            return(self.binarySearch(min,max,n))
        elif (3**self.searchBetween(min,max))<n:
            min=self.searchBetween(min,max)
            return(self.binarySearch(min,max,n))
        elif (3**self.searchBetween(min,max))==n:
            return(True)
        else:
            return(False)

a=Solution()
print(a.isPowerOfThree(1162261467))