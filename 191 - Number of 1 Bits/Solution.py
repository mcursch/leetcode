class Solution:
    def hammingWeight(self, n: int) -> int:
        #how to get number of ones
        #ex: 1011, we could just keep shifting it until the number is 0, and increment a count each time
        # need to track if we have a 1, can just mod the number, if != 0, its odd, so the last is a 1

        #establish count = 0
        count = 0
        # while the count is not equal to 0
        while n != 0:
            #if n is odd (n mod 2 equals 1), increement the counter (last bit must be a 1)
            if n % 2 != 0:
                count +=1
            # shift right once (want to make sure we dont keep sign bit here, so >>, if we did > we will infinite loop)
            n = n >> 1
        return count





