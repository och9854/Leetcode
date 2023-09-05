# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [[]]
        # edge
        if not root:
            return []

        # dfs
        def helper(root, level):
            if root is None:
                return None
            # if new level:
            if (len(res) < level+1):
                res.append([])
            
            # add curr value
            res[level].append(root.val)

            # go next
            helper(root.left, level +1)
            helper(root.right, level +1)

        helper(root, 0)
        return res



# Feedback
'''
- Wrong to check the level -> had empty list at last ex. [[1,3], [2,4], []]






'''