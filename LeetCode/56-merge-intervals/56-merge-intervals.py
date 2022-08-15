class Solution(object):
    def merge(self, intervals):
        merged = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged