class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        x = sum(nums)
        if x%2==1:
            return False
        a = x//2
        dp =[False]*(a+1)
        dp[0] =True
        for num in nums:
            for i in range(a,num-1,-1):
                dp[i]= dp[i] or dp[i-num]
        
        return dp[-1]
       
        