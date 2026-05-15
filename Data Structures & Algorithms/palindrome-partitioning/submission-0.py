class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def backtrack(current_path, i):
            if i == len(s):
                res.append(current_path.copy())
                return
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                
                if substring == substring[::-1]:
                    current_path.append(substring)
                    backtrack(current_path, j + 1)
                    current_path.pop()

        backtrack([], 0)
        return res