class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        i = 0
        n = len(intervals)
        result = []
        intervals.sort( key = lambda x:x[0])
        while i < n-1:
            current = intervals[i]
            next_entry = intervals[i+1]
            if current[1] >= next_entry[0]:
                merged_start = current[0]
                merged_end = max(current[1],next_entry[1])
                intervals[i+1] = [merged_start,merged_end]
            else:
                result.append(current)
            i +=1
        
        result.append(intervals[-1])

        return result 