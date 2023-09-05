class MyQueue(object):

    def __init__(self):
        self.a = list()
        self.b = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.a.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.a.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.a[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.a) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()