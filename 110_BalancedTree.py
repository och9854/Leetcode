# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''Wrong
# import math
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         # count all tree and calcualte
#         node_list = []
        
#         # dfs
#         def dfs(node):
#             node_list.append(node)
            
#             # until node is none
#             if node is None:
#                 return None
            
#             dfs(node.left)
#             dfs(node.right)
            

#         dfs(root)
        
# #         ## compare count and len(not null node)
#         not_null_length = len([x for x in node_list if x is not None])
        
        
#         #         11,
#         #         5 -> 5개면 높이가 2~3 -> cnt: 4~8

#         #         15, 
#         #         7 -> height 2~3 -> cnt: 4~8
#         node_list
#         not_null_length
    
'''
# answer!
class Solution:
    
    
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # empyt tree is balanced and has height -1
        if not root:
            return True, -1
        
        # check subtrees if they are balanced
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        
        if not (leftIsBalanced and rightIsBalanced):
            return False, 0
        return (abs(leftHeight-rightHeight) < 2), 1+max(leftHeight, rightHeight)
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


# Feedback
'''
- use helper method
- DFS

'''