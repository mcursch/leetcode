class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        #combine two arrays together
        pair = [[p,s] for p,s in zip(position, speed)]

        # sort pair array (sorting by position)
        # go through arr in reverse sorted order
        for p,s in sorted(pair)[::-1]:
            # append the time it would tkae the current car to reach dest to stack
            stack.append((target-p)/s)
            # if that car shares a time with a previous car in the stack, they become a fleet
            # so pop the stack (combine them into a fleet)
            # go through in reverse sorted order so we track the closest cars first
            # closest cars cannot be passed, so they will also set the speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # return the length of the stack (the number of fleets)
        return len(stack)