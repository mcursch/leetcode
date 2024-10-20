class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # if no node, return 0
            # catches null children and empty tree
            if not node:
                return 0
            #else, we have at least one level, so return 1 + the max of the subtree depth
            return max(1 + dfs(node.right), 1+ dfs(node.left))
        # return called on root
        return dfs(root)



