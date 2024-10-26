class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n pairs means n opening, n closing parentheses
        # cant start with a closing parenth
        # we can only add a closing parenth if open count > closing count
        # when we have an open and no close, we have two choices: add another open or add a close
        # if we have limit of opening paren, then must close
        # valid only iff open == closed == n
        # use recursion to make decision tree
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                # finished, stack has proper paren
                res.append("".join(stack))
                return
            if openN < n:
                # append an open paren if we can
                # backtracking requires we pop it off after were done
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                # append closing paren if we can
                # backtracking pop it off after wards
                # only add if close < open
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

