class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==0:
            return ""
        start =0
        end =0
        for i in range(len(s)):
            l1 = self.palindrome(s,i,i)
            l2 = self.palindrome(s,i,i+1)
            max_len = max(l1,l2)
            if max_len > end - start:
                end = i + max_len // 2
                start = i -(max_len - 1) // 2
        
        return s[start:end + 1]
        
    def palindrome(self, s, left,right):
        while left>=0 and right < len(s) and s[left] == s[right]:
            left -=1
            right+=1
        return right - left -1 
        