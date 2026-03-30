class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n:
            r += (n &1)
            n = n>>1
        return r
        