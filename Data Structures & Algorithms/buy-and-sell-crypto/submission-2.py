class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        res = 0
        while r < len(prices):
            current = 0
            if prices[l] < prices[r]:
                current = prices[r] - prices[l]
                res = max(res,current)

            else:
                l = r
            r +=1 
        return res





        