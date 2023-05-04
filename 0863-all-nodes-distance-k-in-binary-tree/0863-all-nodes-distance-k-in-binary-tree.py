# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentNode = []
      
        def findParent(curr , parent=None):
            if curr:
                
                curr.parent = parent 
                findParent(curr.left , curr)
                findParent(curr.right, curr)
                
            
            
             
                
        findParent(root)

    
        q = deque([(target)])
        result = []
        visited = set()
        visited.add(target)
        distance = 0
        while q:
            for _ in range(len(q)):
                
           
                if distance == k:
                   
                    result = [node.val for node in q]
                    return result 
                else:
                    curr = q.popleft()
                    
                        
                   
                    for branch in [curr.right , curr.left, curr.parent]:
                        #to avoid NoneType Objects
                        if branch and branch not in visited :
                            visited.add(branch)
                            q.append(branch)
                    
            distance += 1
        return []
                        
                
                    
                
            
                
                