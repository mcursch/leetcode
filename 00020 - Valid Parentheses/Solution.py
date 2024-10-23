class Solution:
    def isValid(self, s: str) -> bool:
        # establish a set of value pairs to match eachother
        match = {'(': ')', '{': '}', '[': ']'}
        # utilize a stack, which is just a list in python
        # because values have to match and close eachother (cant be nested), a stack can be used
        stack = []

        # go through each character
        for c in s:
            # if the character is a closing shape
            if c in ')}]':
                # check if the length of stack is valid
                if len(stack) == 0:
                    return False
                # if it is, pop the top, and make sure the closer matches to the proper opener
                else:
                    char = stack.pop()
                    if c != match[char]:
                        return False
            # if its not, it must be an opener, append it (add to top of stack)
            else:
                stack.append(c)

        # if we finish and the stack is not empty, return false
        return len(stack) == 0
