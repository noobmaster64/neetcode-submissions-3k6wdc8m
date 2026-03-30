class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(day,buying):
            if day >= len(prices):
                return 0
            if (day,buying) in dp:
                return dp[(day,buying)]
            if buying:
                buy = dfs(day +1, not buying) - prices[day]
                cooldown = dfs(day +1, buying)
                dp[(day,buying)] = max(buy, cooldown)
            else:
                sell = dfs(day +2, not buying) + prices[day]
                cooldown = dfs(day +1,  buying)
                dp[(day,buying)] = max(sell, cooldown)
            return dp[(day,buying)]
        return dfs(0,True)
