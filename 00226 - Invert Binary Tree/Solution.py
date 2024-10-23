# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # check if current node is valid (either empty tree of at null children)
            # return nothing if not
            if not node:
                return None
            # swap children, assuming current node is valid (note kids could be null here, but still swap)
            node.left, node.right = node.right, node.left

            # recursively call on left and right subtree
            dfs(node.left)
            dfs(node.right)

            # return the current node to its previous function call, though this really only matters in the end
            return node

        return dfs(root)


