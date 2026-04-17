class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = 0
        best = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                diff = prices[r] - prices[l]
                if diff > best:
                    best = diff
        return best