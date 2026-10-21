class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res: int = 0

        buy: int = 0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
                continue

            res = max(res, prices[sell] - prices[buy])

        return res
