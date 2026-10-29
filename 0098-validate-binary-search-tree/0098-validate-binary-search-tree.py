# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def bfs(node,low,high):
            if node is None:
                return True

            if(node.val<=low or node.val>=high):
                return False

            return bfs(node.left,low,node.val) and bfs(node.right,node.val,high)

        return bfs(root,float('-inf'),float('inf'))