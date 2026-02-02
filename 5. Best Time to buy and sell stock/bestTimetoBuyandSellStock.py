class Solution:
    from typing import List

    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            if prices[i] > bestBuy:
                maxprofit = max(maxprofit, prices[i] - bestBuy)
            else:
                bestBuy = prices[i]

        return maxprofit
