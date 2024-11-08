class TimeMap:

    def __init__(self):
        # timeMap to be an empty dict
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if not in, add a blank, if it is, append the value timestamp arr to it
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # perform binary search to get the value whos timestamp matches target
        # each key holds a list, so get that list first
        # then BS that list

        res = ""
        arr = self.timeMap.get(key, [])
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)