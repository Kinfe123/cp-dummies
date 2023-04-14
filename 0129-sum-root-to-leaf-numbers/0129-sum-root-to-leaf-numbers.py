
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        def dfs(node  , val):
            nonlocal result
            if node.right or node.left:
                if node.right:
                    dfs(node.right , val * 10 + node.val)
                if node.left:
                    dfs(node.left , val * 10 + node.val)
            else:
                #base case 
                result += val*10 + node.val
                return 
        
        dfs(root , 0)
            
        return result
    
                
            
                
            
        