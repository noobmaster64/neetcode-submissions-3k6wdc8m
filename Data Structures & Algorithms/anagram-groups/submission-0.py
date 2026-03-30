class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rest = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch) - ord('a')] +=1
            print(count)
            rest[tuple(count)].append(s)
        return list(rest.values())

        