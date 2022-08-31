class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                merged.append(interval)
            elif interval[0] > newInterval[1]:
                merged.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        merged.append(newInterval)
        return merged