class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            # if you have an operation
            if t in ops:
                # pop the last two nums off the stack
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                # perform whatever op is needed
                if t == '+':
                    res = num2 + num1
                if t == '-':
                    res = num2 - num1
                if t == '*':
                    res = num2 * num1
                if t == '/':
                    res = math.trunc(num2 / num1)
                # append the result to the stack
                stack.append(res)
            else:
                # if its just a number, apppend it
                stack.append(t)

        # get the last value, it will be the result
        return int(stack.pop())
