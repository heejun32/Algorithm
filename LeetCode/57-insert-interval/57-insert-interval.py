class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        
        merged = []
        for interval in intervals:
            if merged:
                # not overlapping
                if merged[-1][1] >= interval[0]:
                    merged[-1][1] = max(merged[-1][1], interval[1])
                else:
                    merged.append(interval)   
            else:
                merged.append(interval)
                
        return merged