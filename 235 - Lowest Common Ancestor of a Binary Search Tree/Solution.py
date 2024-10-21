# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # since the tree is a BST, the LCA will always be the node with the value inbetween p and q

        # we know that p and q exist, so there will be an LCA, so we can do while True
        while True:
            # if the value > both, the LCA is to the left
            if root.val < p.val and root.val < q.val:
                root = root.right

            # if the value < both, the LCA is to the right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

