from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        return None

    def pop(self) -> int:
        if not self.queue:
            return None
        return self.queue.popleft()

    def peek(self) -> int:
        if not self.queue:
            return None
        return self.queue[0]

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
