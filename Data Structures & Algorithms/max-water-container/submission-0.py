class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        area = 0
        current_area = 0
        while l < r:
            current_area = (r-l)*(min (heights[l],heights[r]))
            print(heights[l],heights[r])
            area = max(area,current_area)
            if heights[r]<heights[l]:
                r-=1
            else:
                l +=1
        
        return area 
        