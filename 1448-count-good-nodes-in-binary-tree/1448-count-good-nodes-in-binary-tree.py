# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode,max_value=float('-inf')) -> int:
        c=0
        if root is None:
            return 0

        if(root.val>=max_value):
            max_value=root.val
            c=1

        left=self.goodNodes(root.left,max_value)
        right=self.goodNodes(root.right,max_value)

        return c+left+right