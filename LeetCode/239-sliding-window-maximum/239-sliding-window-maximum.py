import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        results = []
        # queue[0]에는 매 윈도우마다 가장 큰 값의 인데스만 저장!
        queue = collections.deque()
        for i in range(len(nums)):
            # 인덱스 k 만큼 유지
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            results.append(nums[queue[0]])

        return results[k - 1:]


# nums = [1,3,1,2,0,5]
# k = 3

# sol = Solution()
# print(sol.maxSlidingWindow(nums, k))
