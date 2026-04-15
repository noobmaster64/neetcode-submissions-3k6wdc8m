class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1 
        n = len(nums)
        l,r = 0, n-1
        while l<r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid

        pivot  = l
        
        print (pivot)
        if pivot ==0:
            l,r = 0, len(nums)-1
        elif nums[pivot] <= target <= nums[n-1]:
            l,r= pivot, n-1
        else:
            l,r = 0, pivot -1
        
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        
        return -1

        