from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        answer = []        
        for _ in range(k):
            answer.append(heapq.heappop(freqs_heap)[1])
        return answer
