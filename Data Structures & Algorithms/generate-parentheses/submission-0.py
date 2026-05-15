class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_count, close_count, path):
            if open_count ==0 and close_count ==0:
                res.append("".join(path))
            
            if open_count>0:
                path.append("(")
                backtrack(open_count-1,close_count +1,path)
                path.pop()
            if close_count>0:
                path.append(")")
                backtrack(open_count,close_count - 1,path)
                path.pop()
        backtrack(n, 0, [])
        return res
            
        