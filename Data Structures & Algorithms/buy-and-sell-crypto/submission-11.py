class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP: int = 0
        buy: int = prices[0]
        
        for sell in prices:
            buy = min(buy, sell)
            maxP = max(maxP, sell - buy)

        return maxP


