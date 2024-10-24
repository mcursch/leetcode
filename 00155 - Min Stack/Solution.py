class MinStack:

    # use two lists, one to track values, one to track mins
    def __init__(self):
        self.stack = []
        self.minStack = []

    # push value onto normal stack
    # if the value is smaller than the curMin, append it to the top, else just append the curMin to the top
    # when the getmin is called we always want to return curMin
    # however, curMin can get replaced, meaning if we replace then pop, we still want our old curMin to be returnable
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    # pop both stacks
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # return the top (last value) in normal stack
    def top(self) -> int:
        return self.stack[-1]

    # return the top (last value) in min stack
    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()