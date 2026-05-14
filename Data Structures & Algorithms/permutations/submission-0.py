class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                res.append(list(current_path))
                return
            
            for n in count:
                if count[n] > 0:
                    current_path.append(n)
                    count[n] -= 1
                    
                    backtrack(current_path)
                    
                    count[n] += 1
                    current_path.pop()
        
        backtrack([])
        return res
        