class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            # Decision 1: Include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
            # Decision 2: Skip nums[i] and all its duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, path)
            
        backtrack(0, [])
        return res