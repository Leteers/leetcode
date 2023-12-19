from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        revers_prices = list(reversed(prices))
        
        print(revers_prices)
sol = Solution()
prices = [7,1,5,3,6,4]
sol.maxProfit(prices)