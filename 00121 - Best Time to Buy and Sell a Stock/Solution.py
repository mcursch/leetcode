class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            # compute the current profit point by subtracting the current price - your buy price
            # use max to keep the max profits you may have before adjusting the buy price
            # attempting to maximize price, but want to store our highest value up to this point
            profit = max(profit, prices[i] - buy)
            # if the current price is less than your buy price, set the buy price to the current price
            if prices[i] < buy:
                buy = prices[i]
        return profit
