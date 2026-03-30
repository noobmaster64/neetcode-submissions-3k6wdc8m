class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for i in range(len(t)):
            count_s[s[i]] = 1+ count_s[s[i]]
            count_t[t[i]] = 1+ count_t[t[i]]
        return count_s == count_t
        