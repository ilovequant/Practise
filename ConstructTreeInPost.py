"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        self.postorder = postorder
        return self.helper(inorder)

    def helper(self, inorder):
        if not inorder or not self.postorder:
            return
        node_val = self.postorder.pop()
        node = TreeNode(node_val)
        index = inorder.index(node_val)
        node.right = self.helper(inorder[index + 1:])
        node.left = self.helper(inorder[:index])
        return node