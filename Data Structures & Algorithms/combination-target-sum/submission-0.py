class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]


        def backtrack(i, current_sum, current_path):
            if current_sum == target:
                res.append(current_path.copy())
                return
            if current_sum > target or i >= len(nums):
                return 
            current_path.append(nums[i])
            backtrack(i, current_sum + nums[i], current_path)

            current_path.pop()
            backtrack(i+1, current_sum, current_path)

        backtrack(0,0,[])

        return res
            
        

        