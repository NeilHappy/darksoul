#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root: TreeNode):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)

        result = list()
        postorder(root)
        return result
        """
        if root is None:
            return []
        root.left = self.postorderTraversal(root.left)
        root.right = self.postorderTraversal(root.right)
        return root.left+root.right+[root.val]
        """

# @lc code=end
