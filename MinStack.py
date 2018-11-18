class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []
        self.last = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        if len(self.stack1) == 0:
            self.stack1.append(number)
            self.last.append(1)

        elif number <= self.stack1[-1]:
            self.stack1.append(number)
            self.last.append(1)
        else:
            self.stack2.append(number)
            self.last.append(2)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        label = self.last.pop()
        if label == 1:
            return self.stack1.pop()
        if label == 2:
            return self.stack2.pop()

    """
    @return: An integer
    """

    def min(self):
        # write your code here

        return self.stack1[-1]