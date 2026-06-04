class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res =nums[0]
        maxc = nums[0]
        minc  = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <0:
                maxc,minc = minc,maxc
            maxc= max(nums[i],nums[i]*maxc)
            minc = min(nums[i],nums[i]*minc)

            res= max(res,maxc)
        
        return res 

