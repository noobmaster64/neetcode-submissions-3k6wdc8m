class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def recursion(i,j):
            if j == len(p):
                return i == len(s)
            if (i,j) in memo:
                return memo[(i,j)]
            firstmatch = i < len(s) and ( s[i] == p[j] or p[j]=='.')

            if len(p)>j+1 and p[j+1]=='*':
                res = recursion(i,j+2) or (firstmatch and recursion(i+1,j))
            else:
                res = recursion(i+1,j+1) and firstmatch 
        
            memo[(i,j)]= res
            return res
        return recursion(0,0) 
