class MyQueue(object):

    def __init__(self):
        self.x = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.x.insert(0, x)
        

    def pop(self):
        """
        :rtype: int
        """
        y = self.x.pop()
        return y

    def peek(self):
        """
        :rtype: int
        """
        return self.x[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.x) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()