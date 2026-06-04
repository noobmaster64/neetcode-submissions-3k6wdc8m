class Solution:
    def numDecodings(self, s: str) -> int:
        # If the string is empty or starts with '0', it's instantly invalid.
        if not s or s[0] == '0':
            return 0

        # dp[i] represents the number of ways to decode a string of length i
        dp = [0] * (len(s) + 1)
        
        # Base cases
        dp[0] = 1  # 1 way to decode an empty string
        dp[1] = 1  # 1 way to decode a string of length 1 (we know it's not '0')

        # We start checking from the 2nd character (length 2) up to the end
        for i in range(2, len(s) + 1):
            
            # Check 1-digit jump: Is the single character valid? (1 through 9)
            # Notice we use i-1 because the string is 0-indexed, but our dp array is 1-indexed.
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Check 2-digit jump: Do the last two characters form a valid number? (10 through 26)
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]

        # The last element holds the total combinations for the full length of the string
        return dp[-1]