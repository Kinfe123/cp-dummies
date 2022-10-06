# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        #Can be solved with linear space - extra memory
        node_value = []
        #Inorder traversal
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
        
            node_value.append(root.val)
            dfs(root.right)
        dfs(root)
        def buildingBalanced(i , j):
            if i > j: return 
            middle_val = (i+j)//2
            return TreeNode(node_value[middle_val] , buildingBalanced(i , middle_val-1) , buildingBalanced(middle_val+1 , j) )
        return buildingBalanced(0 , len(node_value)-1)
       
            
                