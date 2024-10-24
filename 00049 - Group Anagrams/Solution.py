from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # get res hashtable
        res = {}
        # go through each string
        for s in strs:
            # sort the string, put its sorted value as a key in hashmap
            # value will be all strings that match that sorted hash (all anagrams)
            key = "".join(sorted(s))
            # if the key is in the hash, append cur string to it, if not, set cur string inside an arr as only value
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())

        # ans = defaultdict(list)

        # for s in strs:
        #     key = "".join(sorted(s))
        #     ans[key].append(s)

        # return list(ans.values())