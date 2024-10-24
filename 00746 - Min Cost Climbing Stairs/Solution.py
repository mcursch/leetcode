class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            # get current end value (where we will start iterating)
            end = len(cost)-1
            # extend array to add two 0's, allows us to not worry about oob in loop
            cost.extend([0,0])
            # start from end and go backwards
            for i in range(end, -1, -1):
                # current cost is the smallest value of cost of taking 1 or 2 steps
                cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

            # 0 will hold min cost starting at 0, 1 holds min cost starting at 1
            # return the smaller value
            return min(cost[0], cost[1])