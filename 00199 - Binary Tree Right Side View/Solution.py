# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            # get qLen to ensure were taking right side node in for loop
            # default rightside to null in case we dont loop at all ( last level all nulls perhaps)
            rightside = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    # set rightside to node, this wont matter until the last right most value (last iteration in for loop)
                    rightside = node
                    # make sure to append node.right last, so that it ends up on right most side
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)
        return res
