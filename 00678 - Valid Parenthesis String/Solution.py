class Solution:
    def checkValidString(self, s: str) -> bool:
        # use two trackers to account for * wildcard
        leftMin, leftMax = 0, 0
        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False

            # we assume * is either an lparen or an rparen. if its an lparen or empty string, then subtracting 1 from leftmin is the wrong choice, so
            # rectify that by setting it to 0.
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
