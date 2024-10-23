class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # utilize minheap
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        # pop off smallest values until size = k. that way, if we have 3 values and k = 3, the 3rd smallest is the head of the heap
        # so, heappop will always give us kth smallest value
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # in case we start with empty heap, check heap length on adds
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)