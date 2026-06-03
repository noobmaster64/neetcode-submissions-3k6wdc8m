class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n< 3:
            if  n==1:
                return nums[0]
            return max(nums[0],nums[1])
        dp = [0]*n
        dp[0]=nums[0]
        dp[1] = nums[1]
        dp[2]= dp[0] + nums[2]
        for i in range(3,n):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        return max(dp[n-1],dp[n-2])
        