class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            #shift array to clear space for next bit
            res = res << 1
            # get next bit
            bit = n % 2
            # add bit to value
            res += bit
            # shift the numb so we can get the next bit
            n = n >> 1
            print(res)
        return res

