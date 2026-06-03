class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: Only one house in the entire circle
        if len(nums) == 1:
            return nums[0]
            
        # Your exact House Robber 1 logic as a helper function
        def rob_linear(arr: List[int]) -> int:
            n = len(arr)
            if n < 3:
                if n == 1:
                    return arr[0]
                return max(arr[0], arr[1])
            
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = arr[1]
            dp[2] = dp[0] + arr[2]
            
            for i in range(3, n):
                dp[i] = arr[i] + max(dp[i-2], dp[i-3])
            
            return max(dp[n-1], dp[n-2])

        # Scenario A: Skip the last house (nums[:-1])
        # Scenario B: Skip the first house (nums[1:])
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))