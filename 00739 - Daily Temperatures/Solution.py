class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Optimal Solution, O(n) space and time
        # Monotonic Decreasing Stack: all the values in the stack will be decreasing
        # when we get a larger value, we pop everything thats less than that value
        # go through each temp, when u get a higher one, pop and fill the res of the lower indexes
        # if u get to the end, those vals get 0, hence why res is 0 array to start
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # while we have a stack and the last val in the stack is greater than the current temp
            while stack and t > stack[-1][0]:
                # pop the value off, add it to the res based on position
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res

        # # first solution, takes too long O(n^2) time
        # res = []
        # for i in range(len(temperatures)):
        #     count = 0

        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] <= temperatures[i]:
        #             if j == len(temperatures) -1:
        #                 res.append(0)
        #                 break
        #             else:
        #                 count +=1
        #         else:
        #             res.append(1 + count)
        #             break
        # res.append(0)
        # return res




