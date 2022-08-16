class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        result = []
        counter = collections.Counter(nums)
        for key, value in counter.items():
            heapq.heappush(heap, (-1 * value, key))
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result