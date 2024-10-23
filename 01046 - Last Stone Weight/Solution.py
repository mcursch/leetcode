class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # take two largest stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # want to see if second is less than first because that means we have leftover
            # because we put all negatives into the array, we need to do the reverse, so check if second > first
            if second > first:
                heapq.heappush(stones, first - second)
        # append a zero in case all the stones got destroyed. could do a condition here, but this is less code
        stones.append(0)
        return stones[0] * - 1


