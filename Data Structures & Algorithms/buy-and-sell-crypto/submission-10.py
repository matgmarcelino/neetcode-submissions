class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res: int = 0

        buy: int = prices[0]
        for sell in prices:
            buy = min(buy, sell)
            res = max(res, sell - buy)

        return res
