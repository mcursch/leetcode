# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we know both trees will have at least 1 node
        # if we get to not root, we know subroot cant be a subtree of this, so return false
        # shouldnt have to check if subroot is null
        if not root:
            return False
        # check if the current node is a subtree by utilizing same tree algo
        if self.isSameTree(root, subRoot):
            return True
        # if not the same tree, continue searching through the tree
        # return an or statement here because if either side is a subtree, we return true
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False