class MyQueue:

    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        length = len(self.stack_in) - 1
        for _ in range(length):
            self.stack_out.append(self.stack_in.pop())
        front_value = self.stack_in.pop()
        for _ in range(length):
            self.stack_in.append(self.stack_out.pop())   
        return front_value

    def peek(self) -> int:
        return self.stack_in[0]

    def empty(self) -> bool:
        if self.stack_in:
            return False
        return True
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()