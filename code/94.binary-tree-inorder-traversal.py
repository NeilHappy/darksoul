#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        result = list()

        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result
        """
        if root is None:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left+[root.val] + right

# @lc code=end
