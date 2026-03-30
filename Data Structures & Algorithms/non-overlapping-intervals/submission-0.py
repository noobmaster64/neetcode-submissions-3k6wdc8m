class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x[1])
        removed_count = 0
        last_kept_end = intervals[0][1]
        for i in range(1, len(intervals)):
            current_state = intervals[i][0]
            current_end = intervals[i][1]

            if last_kept_end > current_state:
                removed_count +=1
            else:
                last_kept_end = current_end
        
        return removed_count

        