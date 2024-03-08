from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        revers_prices = list(reversed(prices))
        maxim = 0
        for i in range(len(revers_prices)):
            for j in range(len(prices)-i):
                if (revers_prices[i] - prices[j]) > maxim:
                    revers_index = i
                    prices_index = j
                    print(revers_prices[i] - prices[j])
                    maxim = revers_prices[i] - prices[j]
        return(maxim)
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))