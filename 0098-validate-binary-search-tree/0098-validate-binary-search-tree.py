# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_ = float('inf')
        min_ = float('-inf')
        q = deque([(root , max_ , min_ )])
        
        res = True
        # if not root.left or not root.right:
        #     return False
        while q:
            l = len(q)
            for i in range(l):
                curr , max_ , min_  = q.popleft()
            
                
                if curr.val >= max_ or curr.val <= min_:
                    return False
                if curr and curr.left:
                    if curr.left.val >= curr.val:
                        res = False
                        break
                        
                        
                    else:
                        q.append((curr.left , curr.val , min_  ))
                if curr and curr.right:
                    if curr.right.val <= curr.val:
                        res = False
                        break
                        
                    else:
                        q.append((curr.right , max_ , curr.val))
        # print(res)
        return res
                