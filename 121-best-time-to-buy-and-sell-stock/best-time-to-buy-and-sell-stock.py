class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_seen=float('inf')
        max_profit=0
        for price_current in prices:
            min_price_seen = min(min_price_seen,price_current)
            profit=price_current-min_price_seen
            max_profit=max(max_profit,profit)

        return max_profit
        