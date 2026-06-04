class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindromes(left: int, right: int) -> int:
            count = 0
            # Keep expanding as long as it's a valid palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # We found one! Increment the count.
                left -= 1
                right += 1
            return count
        total_palindromes = 0

        for i in range(len(s)):
            # Count odd-length palindromes (center is at character i)
            total_palindromes += count_palindromes(i, i)
            
            # Count even-length palindromes (center is between i and i+1)
            total_palindromes += count_palindromes(i, i + 1)
            
        return total_palindromes
        