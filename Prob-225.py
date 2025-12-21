class MyStack(object):

    def __init__(self):
        self.l = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.l.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.l) > 0:
            return False

        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()