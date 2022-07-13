from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = deque()
        while head.next:
            queue.append(head.val)
            head = head.next
        queue.append(head.val)
        
        
        while queue:
            if len(queue) == 1:
                return True
            if queue.popleft() != queue.pop():
                return False
        
        return True