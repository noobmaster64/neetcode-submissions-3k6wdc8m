class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            if i+ nums[i]>max_reachable:
                max_reachable = i+ nums[i]
            if max_reachable >= len(nums) - 1:
                return True
        return True 