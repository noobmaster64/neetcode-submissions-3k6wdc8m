class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack (i,current_path, rem):
            if rem ==0:
                res.append(current_path.copy())
                return
            if rem <0 or i >= len(candidates):
                return 
            
            current_path.append(candidates[i])
            backtrack(i+1,current_path,rem-candidates[i])
            print(rem)
            current_path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1 
            backtrack(i+1,current_path,rem)
        
        backtrack(0,[],target)

        return res

        