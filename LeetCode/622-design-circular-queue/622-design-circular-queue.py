class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.q[self.front] is None:
            return -1
        else:
            return self.q[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.q[self.rear - 1] is None:
            return -1
        else:
            return self.q[self.rear - 1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.front == self.rear and self.q[self.rear] is None:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.front == self.rear and self.q[self.rear] is not None:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()