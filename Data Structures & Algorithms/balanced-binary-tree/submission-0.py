# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):

            # Empty tree has height 0
            if not node:
                return 0

            # Get height of left subtree
            left_height = height(node.left)

            # If left subtree is already unbalanced
            if left_height == -1:
                return -1

            # Get height of right subtree
            right_height = height(node.right)

            # If right subtree is already unbalanced
            if right_height == -1:
                return -1

            # If height difference is more than 1,
            # this tree is not balanced
            if abs(left_height - right_height) > 1:
                return -1

            # Otherwise return current node's height
            return 1 + max(left_height, right_height)

        # -1 means we found an unbalanced node
        return height(root) != -1