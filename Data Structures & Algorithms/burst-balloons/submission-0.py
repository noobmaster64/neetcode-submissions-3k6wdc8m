class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def get_max_coins(left,right):
            if left > right:
                return 0
            if (left,right) in memo:
                return memo[(left,right)]
            best_score = 0
            for i in range(left,right+1):
                left_score = get_max_coins(left,i-1)
                right_score = get_max_coins(i+1,right)
                pop_score = nums[left-1]*nums[i]*nums[right+1]
                total = left_score + right_score + pop_score

                if total> best_score:
                    best_score = total
            memo[(left,right)] = best_score
            return best_score

        return get_max_coins(1,len(nums)-2) 
            