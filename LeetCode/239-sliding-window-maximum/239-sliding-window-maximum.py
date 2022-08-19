import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = collections.deque()
        result = []
        for index, value in enumerate(nums):
            # print("queue {0}".format(queue))
            # print("result {0}".format(result))

            if queue and index - queue[0] == k:
                queue.popleft()
            while queue and nums[queue[-1]] < value:
                queue.pop()
            
            queue.append(index)
            result.append(nums[queue[0]])
        return result[k - 1:]