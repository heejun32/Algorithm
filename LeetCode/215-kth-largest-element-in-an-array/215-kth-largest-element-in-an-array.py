class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = []
        for num in nums:
            heapq.heappush(lst, -1 * num)
        
        for _ in range(k - 1):
            heapq.heappop(lst)
        
        return -1 * heapq.heappop(lst)
            