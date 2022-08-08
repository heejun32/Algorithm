class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res, deque = [], collections.deque()
        for i in range(len(nums)):
            while deque and deque[0] <= i-k:
                deque.popleft()
            while deque and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)
            res.append(nums[deque[0]])
            
        
        return res[k-1:]