class MinStack:

    def __init__(self):
        self.mini = []
        

    def push(self, val: int) -> None:
        self.mini.append(val)

    def pop(self) -> None:
        return self.mini.pop()
        

    def top(self) -> int:
        return self.mini[-1]
        

    def getMin(self) -> int:
        return min(self.mini)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()