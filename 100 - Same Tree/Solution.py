# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if both p and q are null
        # acts as base case and catches empty tree edge case
        if not q and not p:
            return True
        # make sure both p and q exist before checking their value (one could be null)
        # if they both exist and are equal, return the and of their subtrees (both must be true to return true)
        if p and q and p.val == q.val:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        # if something failed, they arent equal, so return False.
        else:
            return False
