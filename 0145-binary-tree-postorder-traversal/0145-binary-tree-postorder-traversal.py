# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def postTr(root):
            if root is None:
                return
            postTr(root.left)
            postTr(root.right)
            answer.append(root.val)
        postTr(root)
        return answer
        