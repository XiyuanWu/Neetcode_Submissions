class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        temp = []

        while len(self.s) > 1:
            temp.append(self.s.pop())
        result = self.s.pop()
        while temp:
            self.s.append(temp.pop())
        return result

    def peek(self) -> int:
        temp = []

        while len(self.s) > 1:
            temp.append(self.s.pop())
        result = self.s[-1]
        while temp:
            self.s.append(temp.pop())
        return result

    def empty(self) -> bool:
        return not self.s


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()