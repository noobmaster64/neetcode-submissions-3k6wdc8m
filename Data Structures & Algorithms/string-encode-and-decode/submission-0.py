from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        if not strs:
            return ""
        
        result = []
        for s in strs:
            # For each string: length + delimiter + string
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        if not s:
            return []
        
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            # Find the length
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            # Extract the string of that length
            word = s[j + 1 : j + 1 + length]
            result.append(word)
            
            # Move pointer to next number
            i = j + 1 + length
        
        return result