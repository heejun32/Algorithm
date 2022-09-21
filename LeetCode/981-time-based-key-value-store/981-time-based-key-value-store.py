import collections


class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        mini_map = self.time_map[key]
        left, right = 0, len(mini_map)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if mini_map[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        return "" if not right else mini_map[right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)