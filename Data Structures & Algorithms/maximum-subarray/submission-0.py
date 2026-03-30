class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        current_sum = 0
        for t in nums:
            current_sum = current_sum +t
            maxsum = max(current_sum,maxsum)
            if current_sum<0:
                current_sum =0

        return maxsum