"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """

    def upsideDownBinaryTree(self, root):
        # write your code here
        if root is None:
            return root

        if (root.left is None):
            return root

        new_root = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root

        root.left = root.right = None

        return new_root