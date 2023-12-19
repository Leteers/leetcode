class Solution:
    def mySqrt(self, x: int) -> int:
        max=50000
        min=0
        return(self.binarySearch(min,max,x))
    def searchBetween(self,min,max):
        if int(max)-int(min)==1:
            return(False)
        else: 
            return(int(max-(max-min)/2))
    def binarySearch(self,min: int,max: int,n):
        if type(self.searchBetween(min,max))==bool:
            print(f'Result3 {min}')
            return(min)
        elif (self.searchBetween(min,max)*self.searchBetween(min,max))>n:
            max=self.searchBetween(min,max)
            return(self.binarySearch(min,max,n))
        elif (self.searchBetween(min,max)*self.searchBetween(min,max))<n:
            min=self.searchBetween(min,max)
            return(self.binarySearch(min,max,n))
        elif (self.searchBetween(min,max)*self.searchBetween(min,max))==n:
            print(f'Result1 {max-min}')
            return(self.searchBetween(min,max))
        else:
            print(f'Result2 {min}')
            return(min)
        
a=Solution()
print(a.mySqrt(125))