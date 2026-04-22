# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while(queue):
            level = []
            for n in range(len(queue)):
                x = queue.popleft()
                if n ==0:
                    y=(x.val)
                if x.right:
                    queue.append(x.right)
                    
                if x.left:
                    queue.append(x.left)
            
            res.append(y)
        
        return res
        
        