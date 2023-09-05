# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        # refered ans 1 : recursion
        
        ## get values
        root_val = root.val
        p_val = p.val
        q_val = q.val
        
        ## recursion
        # if both values are greater than root
        if (p_val > root_val) and (q_val > root_val):
            return self.lowestCommonAncestor(root.right, p, q)
        ## elif both are smaller than root
        elif (p_val < root_val) and (q_val < root_val):
            return self.lowestCommonAncestor(root.left, p, q)
        ## if they go to each other descendant
        else: 
            return root

## Feedback
'''
- Understood between binary tree and Binary Search Tree
- Feel DFS more
'''
        