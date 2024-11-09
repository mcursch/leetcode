class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap q.nlargest gives k largest vals, with the largest at the beginning in descending order.
        # so just acces -1 to get last value

        return heapq.nlargest(k, nums)[-1]

        # more optimal solution involving quick select is possible. need to learn that
