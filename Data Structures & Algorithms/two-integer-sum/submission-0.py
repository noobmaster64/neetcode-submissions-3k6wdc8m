class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = defaultdict(int)
        i = 0
        for num in nums:
            diff = target - num
            if diff in dicti:
                return [dicti[diff],i]
            dicti[num] = i
            i += 1
        