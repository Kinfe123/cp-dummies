# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack:
            # we have to add the right node first and then the left node to 
            # the stack to pop the last and visit it which is the left one
            curr = stack.pop()
            if curr:
                result.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return result
                
            
                