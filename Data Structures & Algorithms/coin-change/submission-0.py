class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize array with infinity
        dp = [float("inf")] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0 
        
        for i in range(1, amount + 1):
            for c in coins:
                # If the coin is less than OR EQUAL to the current amount
                if c <= i:
                    # Take the minimum of what we have, or using this coin + 1
                    dp[i] = min(dp[i], dp[i - c] + 1) 
        
        # Return -1 if we couldn't build the amount, otherwise return the answer
        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]