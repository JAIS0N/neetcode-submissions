# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        # Stores the largest diameter found
        diameter = 0

        def height(node):
            nonlocal diameter

            # Empty node has height 0
            if not node:
                return 0

            # Find height of left subtree
            left_height = height(node.left)

            # Find height of right subtree
            right_height = height(node.right)

            # Path through current node
            # = left edges + right edges
            diameter = max(
                diameter,
                left_height + right_height
            )

            # Return height of current node
            # We can only continue through one side upward
            return 1 + max(left_height, right_height)

        height(root)

        return diameter