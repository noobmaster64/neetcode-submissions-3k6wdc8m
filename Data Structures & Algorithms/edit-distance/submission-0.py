class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def check(i,j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i]==word2[j]:
                memo[(i,j)] = check(i+1,j+1)
                return  memo[(i,j)]
            else:
                insert = check(i+1,j)
                delete = check(i,j+1)
                replace= check(i+1,j+1)
                memo[(i,j)] = 1 + min(insert,delete,replace)
                return memo[(i,j)]

        return check(0,0)        