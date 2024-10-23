class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # establish empty dict to use as hash table
        items = {}
        # go through each number in nums
        for n in nums:
            # if the number is in the items hash, that means we have added it, meaning it has been seen before
            if n in items:
                return True
            # if not, its a unique number so far, so add it to the hash
            else:
                items[n] = n
        # return false if we go through the entire array
        return False
