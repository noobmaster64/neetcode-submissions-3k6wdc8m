class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        founda= foundb = foundc = False
        for a,b,c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                founda= True
            if b == target[1]:
                foundb= True
            if c == target[2]:
                foundc = True
        
        return founda and foundb and foundc