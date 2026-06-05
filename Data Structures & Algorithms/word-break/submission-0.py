

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] will be True if s[0:i] can be segmented into words from the dictionary
        dp = [False] * (len(s) + 1)
        
        # Base case: An empty string can always be segmented
        dp[0] = True
        
        # Iterate through all lengths of substrings from 1 to len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                word_len = len(word)
                
                # Check if the word can fit into the current substring s[0:i]
                if i >= word_len:
                    # 1. Does the previous substring s[0:i-word_len] form valid words?
                    # 2. Does the current slice match the word?
                    if dp[i - word_len] and s[i - word_len:i] == word:
                        dp[i] = True
                        break # Found a match for s[0:i], no need to check other words
                        
        return dp[len(s)]