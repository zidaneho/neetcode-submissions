class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        for i,price in enumerate(prices):
            maxProfit = max(maxProfit, price - prices[buy])
            if price < prices[buy]:
                buy = i
        return maxProfit