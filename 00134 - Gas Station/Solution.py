class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # important condition check. if this passes, we are guarenteed to have a solution
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        # go through each value
        # when you finish the array, since we are guarenteed a solution, the answer is the valid total spot
        for i in range(len(gas)):
            total  += gas[i] - cost[i]
            if total < 0:
                total = 0
                res =  i + 1
        return res