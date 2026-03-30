class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapi = defaultdict(int)
        frq = [[] for i in range (len(nums) +1)]
        for n in nums:
            mapi[n] +=1
        for n,c in mapi.items():
            frq[c].append(n)
           
        res = []
        for i in range (len(frq)-1,0,-1):
            for n in frq[i]:
                res.append(n)
                if len(res)==k:
                    return res
                
        