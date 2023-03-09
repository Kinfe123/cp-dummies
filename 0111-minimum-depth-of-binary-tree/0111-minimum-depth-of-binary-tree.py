# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if root is None:
        #     return 0
        # return 1 + min(self.minDepth(root.left) , self.minDepth(root.right))
        self.min_d = float('inf')
        self.dfs(root , 0)
        return self.min_d

    def dfs(self,root , curr):
        if not root:
            return 0
        if not root.left and not root.right:
            self.min_d = min(self.min_d , curr+1)
        self.dfs(root.left , curr+1)
        self.dfs(root.right , curr+1)
            
        