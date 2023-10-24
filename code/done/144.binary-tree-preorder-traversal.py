#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        if root is None:
            return []
        root.left = self.preorderTraversal(root.left)
        root.right = self.preorderTraversal(root.right)
        return [root.val] + root.left + root.right
        """
        def preorder(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)

        result = list()
        preorder(root)
        return result

# @lc code=end
