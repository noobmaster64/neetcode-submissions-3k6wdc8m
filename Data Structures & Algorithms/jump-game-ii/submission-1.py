class Solution:
    def jump(self, nums: List[int]) -> int:
        current_point =0
        farthest_point = 0
        jumps =0 
        for i in range(len(nums)-1):
            if farthest_point < i + nums[i]:
                farthest_point = i + nums[i]
            if current_point == i:
                jumps += 1
                current_point = farthest_point
                if current_point >= len(nums) - 1:
                    break
        return jumps 
            