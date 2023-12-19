from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=0
        purchase=prices[0]
        for i in range(1,len(prices)):
            minimum=max(minimum,prices[i]-purchase)
            purchase=min(purchase,prices[i])
        return(abs(minimum))