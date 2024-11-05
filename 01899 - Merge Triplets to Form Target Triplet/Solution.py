class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # go through each triplet. Ignore the bad ones that have vals > target, because they cant be combined to get target
        # go through each value in the good ones. if they match a val in target, add the index to the set. use a set to avoid repeats and duplicates
        # if len(set) is 3, then it contains all 3 indices of the triplet, which means there exists 3 good triplets who each have a val in target
        # so, they can be combined in some way to give us target

        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            # go through each value in good triplet
            for i, v in enumerate(t):
                # if the value of the triplet is equal to a value in the target
                if v == target[i]:
                    # add the index to the set. This means the set will only be full when 0,1,2 are inside of it for final check
                    good.add(i)
        return len(good) == 3

