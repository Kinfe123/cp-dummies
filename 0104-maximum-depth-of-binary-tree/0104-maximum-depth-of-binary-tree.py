# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive dSF
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        #iterative BFS 
        '''

        we used queue since we want to go level by level to access every level
        which have atmost two children 
        
        
        
        
        '''
        if root is None:
            return 0
        result = 1
        stack = [(root , result)]
        while stack:
            popped , depth = stack.pop()
            result = max(result , depth)
            if popped.right:
                stack.append((popped.right , depth+1))
            if popped.left:
                stack.append((popped.left , depth+1))
        return result
    
                
            
            
            
        