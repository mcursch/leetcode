class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #utilize a hashtable for constant lookup access
        numMap = {}

        #iterate through each number in the given array
        for i in range(len(nums)):

            #if the target value - the current number (referred to as diff) is in our hash table, 
            #then we know cur + diff = target, so we have found the answer, return it
            diff = target - nums[i]
            if diff in numMap:
                return [numMap[diff], i]

            #if its not, add the current number to the hashtable, mapped to its index (for easy return)
            numMap[nums[i]] = i

        #return nothing if no solutions found
        return []