class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # exception
        if key not in self.time_map:
            return ""
        
        array = self.time_map[key]
        left, right = 0, len(array)
        
        while left < right:
            mid = left + (right - left) // 2
            if array[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
                
        return "" if right == 0 else array[right - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)