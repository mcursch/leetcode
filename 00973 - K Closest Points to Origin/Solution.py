class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # My solution. Works well and passes tests
        heap = []
        res = []
        dMap = {}
        # go through points one at a time
        # calc distance of point, place it into a hash of dist: points, then place dist in the minheap
        # when we get the k closest, we'll just pop the minheap until lenth of res = k.
        # add hash[popped] to res. this way, if we have duplicates, theyre also added ((2,3) and (3,2) will have same distance)

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            if distance not in dMap:
                dMap[distance] = []
            dMap[distance].append((x, y))
            heapq.heappush(heap, distance)

        # extract while res size != k

        while len(res) != k:
            d = heapq.heappop(heap)

            for item in dMap[d]:
                print(item)
                res.append(item)

        return res

        # More optimal solution. Didnt know you can store lists in a heap
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res

