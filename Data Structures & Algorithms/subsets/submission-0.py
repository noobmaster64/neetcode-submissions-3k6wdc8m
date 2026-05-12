class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        substack =[]
        def backtrack(i):
            if i == len(nums):
                res.append(substack.copy())
                return
            substack.append(nums[i])
            backtrack(i+1)
            substack.pop()
            backtrack(i+1)
        backtrack(0)

        return res