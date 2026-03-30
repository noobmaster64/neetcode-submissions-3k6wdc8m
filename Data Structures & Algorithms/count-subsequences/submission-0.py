class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def check(i,j):
            if j == len(t):
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            total_ways = 0 

            for k in range(i,len(s)):
                if s[k]==t[j]:
                    total_ways = total_ways + check(k+1,j+1)
            memo[(i,j)]= total_ways 

            return total_ways

        return check(0,0)    