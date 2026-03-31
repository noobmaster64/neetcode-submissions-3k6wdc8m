class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wordset = set()
        longest = 0 
        l = 0
        for r in range (len(s)):
            length  = 0 
            while s[r] in wordset:
                wordset.remove(s[l])
                l+=1
            wordset.add(s[r])
            length = r - l +1 
            longest = max(longest, length)
        
        return longest

        