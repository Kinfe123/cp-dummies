# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cached_ = defaultdict(int)
        max_ = float('-inf')
        def dp(root):
            if not root:
                return [0 ,0]
            
            left_one = dp(root.left)
            right_one = dp(root.right)
            
            
            
            op1 = root.val + left_one[1] + right_one[1]
            op2 = max(left_one) + max(right_one)
            
            
            return [op1 , op2]
        
        return max(dp(root))
            
            
        
        
        
    
    
        
     
    
        