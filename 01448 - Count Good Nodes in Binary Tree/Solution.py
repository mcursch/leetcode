# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs through all nodes
        def dfs(node, maxVal):
            # if at null node, return 0
            if not node:
                return 0
            # if increasing order
            res = 1 if node.val >= maxVal else 0
            # set maxVal to new max
            # in python, recursive calls have their own stack frames
            # meaning if max val changes in left tree to something huge, it wont affect
            # right subtree because right subtree has its own stack fram value saved from here
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

