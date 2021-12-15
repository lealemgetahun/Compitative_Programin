class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        out = []
        i = 0
        while i < len(intervals):
            first = intervals[i][0]
            last = intervals[i][1]
            i += 1
            while i < len(intervals) and intervals[i][0] <= last:
                if last < intervals[i][1]:
                    last = intervals[i][1]
                i += 1
            out.append([first, last])
        
        
        return out